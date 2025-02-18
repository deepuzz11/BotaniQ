def validate_plant_data(data):
    required_fields = ["plant_name", "soil_moisture", "sunlight_exposure", "temperature", "location"]
    
    for field in required_fields:
        if field not in data:
            return False, f"Missing field: {field}"

    return True, "Valid data"
