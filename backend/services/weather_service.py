import requests
from config import WEATHER_API_KEY, WEATHER_API_URL

# Fetch weather data for a given location
def get_weather(location):
    url = f"{WEATHER_API_URL}?key={WEATHER_API_KEY}&q={location}&aqi=no"
    response = requests.get(url)
    
    if response.status_code != 200:
        return None

    data = response.json()
    
    return {
        "temperature": data["current"]["temp_c"],  # Temperature in Celsius
        "weather_condition": data["current"]["condition"]["text"].lower()  # Example: "sunny", "cloudy", "rainy"
    }
