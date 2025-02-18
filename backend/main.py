from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models.model_predict import predict_soil_moisture
from services.weather_service import get_weather
from services.data_processing import validate_plant_data

app = FastAPI()

# 📦 **Request Model**
class PlantData(BaseModel):
    plant_name: str
    soil_moisture: str  # "dry", "wet", "ideal"
    sunlight_exposure: str  # "low", "medium", "high"
    temperature: float  # In Celsius
    location: str  # City name

# 🔥 **Prediction Endpoint**
@app.post("/predict")
def predict(plant_data: PlantData):
    # Validate Data
    is_valid, message = validate_plant_data(plant_data.dict())
    if not is_valid:
        raise HTTPException(status_code=400, detail=message)

    # Get Weather Data
    weather = get_weather(plant_data.location)
    if not weather:
        raise HTTPException(status_code=400, detail="Invalid location or Weather API error")

    # Get ML Prediction
    result = predict_soil_moisture(plant_data.soil_moisture, plant_data.sunlight_exposure, weather["temperature"], weather["weather_condition"])
    
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])

    return {
        "plant_name": plant_data.plant_name,
        "soil_moisture": plant_data.soil_moisture,
        "sunlight_exposure": plant_data.sunlight_exposure,
        "temperature": weather["temperature"],
        "weather_condition": weather["weather_condition"],
        "moisture_status": result["moisture_status"]
    }

# Run with `uvicorn main:app --reload`
