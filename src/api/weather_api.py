import requests
from src.config import BASE_URL, GEOCODING_URL


def get_coordinates(city_name: str):
    params = {
        "name": city_name,
        "count": 1
    }

    response = requests.get(GEOCODING_URL, params=params)
    data = response.json()

    if "results" not in data:
        raise ValueError("Ciudad no encontrada")

    result = data["results"][0]
    return result["latitude"], result["longitude"], result["name"], result["country"]


def get_weather(latitude: float, longitude: float):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    return data["current_weather"]