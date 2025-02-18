import pickle
import numpy as np

# Load Model & Encoders
with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

with open("models/label_encoders.pkl", "rb") as f:
    label_encoders = pickle.load(f)

# Prediction Function
def predict_soil_moisture(soil_moisture, sunlight_exposure, temperature, weather_condition):
    try:
        soil_moisture_encoded = label_encoders["soil_moisture"].transform([soil_moisture])[0]
        sunlight_encoded = label_encoders["sunlight_exposure"].transform([sunlight_exposure])[0]
        weather_encoded = label_encoders["weather_condition"].transform([weather_condition])[0]
    except ValueError:
        return {"error": "Invalid input values"}

    input_data = np.array([[soil_moisture_encoded, sunlight_encoded, temperature, weather_encoded]])
    prediction = model.predict(input_data)
    moisture_status = label_encoders["moisture_status"].inverse_transform(prediction)[0]

    return {"moisture_status": moisture_status}
