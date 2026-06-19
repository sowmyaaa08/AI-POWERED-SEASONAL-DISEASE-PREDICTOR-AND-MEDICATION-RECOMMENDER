import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import joblib
from data import DISEASE_DATA, ALL_SYMPTOMS

def create_dataset():
    data = []
    diseases = list(DISEASE_DATA.keys())
    
    # Generate synthetic data
    for disease, info in DISEASE_DATA.items():
        symptoms = info["symptoms"]
        # Create multiple samples for each disease to make the model robust
        for _ in range(100):
            row = {symptom: 0 for symptom in ALL_SYMPTOMS}
            # Always include core symptoms
            for s in symptoms:
                row[s] = 1
            
            # Randomly remove 1-2 symptoms (except if only 1 exists)
            if len(symptoms) > 2:
                num_to_remove = np.random.randint(0, 2)
                to_remove = np.random.choice(symptoms, num_to_remove, replace=False)
                for r in to_remove:
                    row[r] = 0
            
            # Randomly add 1-2 symptoms from other diseases as noise
            noise_symptoms = list(set(ALL_SYMPTOMS) - set(symptoms))
            num_noise = np.random.randint(0, 2)
            noise_to_add = np.random.choice(noise_symptoms, num_noise, replace=False)
            for n in noise_to_add:
                row[n] = 1
                
            row["disease"] = disease
            data.append(row)
            
    return pd.DataFrame(data)

def train_hybrid_model():
    df = create_dataset()
    X = df.drop("disease", axis=1)
    y = df["disease"]
    
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)
    
    # Random Forest
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    
    # XGBoost
    xgb = XGBClassifier(n_estimators=100, random_state=42, use_label_encoder=False, eval_metric='mlogloss')
    xgb.fit(X_train, y_train)
    
    # Save models and label encoder
    joblib.dump(rf, 'rf_model.pkl')
    joblib.dump(xgb, 'xgb_model.pkl')
    joblib.dump(le, 'label_encoder.pkl')
    joblib.dump(ALL_SYMPTOMS, 'symptoms_list.pkl')
    
    print("Models trained and saved successfully.")
    print(f"RF Accuracy: {rf.score(X_test, y_test)}")
    print(f"XGB Accuracy: {xgb.score(X_test, y_test)}")

if __name__ == "__main__":
    train_hybrid_model()
