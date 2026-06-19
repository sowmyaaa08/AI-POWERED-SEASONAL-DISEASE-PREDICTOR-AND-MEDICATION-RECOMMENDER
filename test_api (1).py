import requests
import json

def test_prediction():
    url = "http://127.0.0.1:5001/predict"
    payload = {
        "symptoms": ["Fever", "Cough", "Sore throat", "Body pain", "Headache", "Fatigue"]
    }
    headers = {
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    if response.status_code == 200:
        print("Test Passed!")
        print(json.dumps(response.json(), indent=2))
    else:
        print(f"Test Failed with status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    test_prediction()
