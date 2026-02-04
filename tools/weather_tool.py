import requests

def get_city_coordinates(city_name):
    """Get lat/long for a city to use in weather API."""
    try:
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
        response = requests.get(url).json()
        if "results" in response:
            return response["results"][0]["latitude"], response["results"][0]["longitude"]
        return None, None
    except Exception:
        return None, None

def get_weather(city: str):
    """Fetches current weather temperature and windspeed for a city."""
    lat, lon = get_city_coordinates(city)
    if not lat:
        return f"Error: Could not find coordinates for {city}."
    
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m"
        response = requests.get(url).json()
        current = response.get("current", {})
        
        return {
            "city": city,
            "temperature": f"{current.get('temperature_2m')} {response.get('current_units', {}).get('temperature_2m')}",
            "wind_speed": f"{current.get('wind_speed_10m')} {response.get('current_units', {}).get('wind_speed_10m')}"
        }
    except Exception as e:
        return f"Error fetching weather: {str(e)}"