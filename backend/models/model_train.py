import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# 🌱 Sample Training Data (Can be replaced with real dataset)
data = pd.DataFrame({
    "soil_moisture": ["dry", "wet", "ideal", "dry", "wet", "ideal"],
    "sunlight_exposure": ["low", "high", "medium", "high", "low", "medium"],
    "temperature": [25, 35, 28, 22, 30, 26],  # Celsius
    "weather_condition": ["clear", "rainy", "cloudy", "rainy", "clear", "cloudy"],
    "moisture_status": ["increase", "decrease", "stable", "increase", "decrease", "stable"]
})

# Encode categorical data
label_encoders = {col: LabelEncoder() for col in ["soil_moisture", "sunlight_exposure", "weather_condition", "moisture_status"]}
for col, encoder in label_encoders.items():
    data[col] = encoder.fit_transform(data[col])

# Train a Random Forest model
X = data[["soil_moisture", "sunlight_exposure", "temperature", "weather_condition"]]
y = data["moisture_status"]
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save Model & Encoders
with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("models/label_encoders.pkl", "wb") as f:
    pickle.dump(label_encoders, f)

print("✅ Model trained and saved!")
