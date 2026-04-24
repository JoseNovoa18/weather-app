from src.api.weather_api import get_coordinates, get_weather
from src.models.weather_model import Weather


def fetch_weather(city_name: str) -> Weather:
    lat, lon, city, country = get_coordinates(city_name)
    weather_data = get_weather(lat, lon)

    return Weather(
        city=city,
        country=country,
        temperature=weather_data["temperature"],
        windspeed=weather_data["windspeed"],
        winddirection=weather_data["winddirection"],
        weathercode=weather_data["weathercode"]
    )