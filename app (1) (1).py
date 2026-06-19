from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import joblib
import numpy as np
import pandas as pd
import requests
import os
from data import DISEASE_DATA, ALL_SYMPTOMS

app = Flask(__name__)
CORS(app)

# Load models
rf_model = joblib.load('rf_model.pkl')
xgb_model = joblib.load('xgb_model.pkl')
le = joblib.load('label_encoder.pkl')
symptoms_list = joblib.load('symptoms_list.pkl')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

def get_weather_data():
    try:
        # Get location via IP
        ip_res = requests.get('http://ip-api.com/json/', timeout=5).json()
        if ip_res['status'] == 'success':
            lat, lon = ip_res['lat'], ip_res['lon']
            city = ip_res['city']
            
            # Get weather via Open-Meteo (No API key required)
            weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&hourly=temperature_2m,relative_humidity_2m,precipitation&past_days=3"
            weather_res = requests.get(weather_url, timeout=5).json()
            
            current = weather_res['current_weather']
            hourly = weather_res['hourly']
            
            # Check for sudden weather change (comparing current temp with average of past 3 days)
            past_temps = hourly['temperature_2m'][:72] # first 72 hours are past 3 days
            avg_past_temp = sum(past_temps) / len(past_temps)
            temp_diff = abs(current['temperature'] - avg_past_temp)
            
            is_sudden_change = temp_diff > 5 # 5 degrees threshold
            
            return {
                "city": city,
                "temp": current['temperature'],
                "condition": "Normal" if not is_sudden_change else "Sudden Change Detected",
                "is_sudden_change": is_sudden_change,
                "temp_diff": round(temp_diff, 2),
                "last_change": "within last 24-72 hours" if is_sudden_change else "Stable"
            }
    except Exception as e:
        print(f"Weather error: {e}")
    return None

@app.route('/symptoms', methods=['GET'])
def get_symptoms():
    return jsonify(ALL_SYMPTOMS)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    selected_symptoms = data.get('symptoms', [])
    
    if not selected_symptoms:
        return jsonify({"error": "No symptoms selected"}), 400
        
    # Prepare input for model
    input_vector = np.zeros(len(symptoms_list))
    for s in selected_symptoms:
        if s in symptoms_list:
            idx = symptoms_list.index(s)
            input_vector[idx] = 1
            
    input_df = pd.DataFrame([input_vector], columns=symptoms_list)
    
    # Hybrid prediction (Average probabilities)
    rf_probs = rf_model.predict_proba(input_df)[0]
    xgb_probs = xgb_model.predict_proba(input_df)[0]
    
    combined_probs = (rf_probs + xgb_probs) / 2
    top_idx = np.argmax(combined_probs)
    disease = le.inverse_transform([top_idx])[0]
    confidence = combined_probs[top_idx]
    
    # Get weather
    weather = get_weather_data()
    
    # Get recommendations
    info = DISEASE_DATA.get(disease, {})
    
    # Enhance diet/advice based on weather
    weather_advice = ""
    if weather:
        if weather['is_sudden_change']:
            weather_advice = f"The sudden weather change in {weather['city']} (temperature shifted by {weather['temp_diff']}°C recently) may have weakened your immune response. "
            if weather['temp'] < 20:
                weather_advice += "Since it's currently cool, prioritize warm soups, herbal teas, and stay warm."
            else:
                weather_advice += "Ensure you stay hydrated and maintain a light, nutritious diet."
        else:
            weather_advice = f"The weather in {weather['city']} is currently stable ({weather['temp']}°C). Your symptoms are likely due to typical seasonal or environmental factors."
    
    response = {
        "disease": disease,
        "confidence": round(float(confidence) * 100, 2),
        "medicines": info.get("medicines", []),
        "ayurvedic": info.get("ayurvedic", []),
        "diet": info.get("diet", []),
        "weather": weather,
        "weather_advice": weather_advice
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
