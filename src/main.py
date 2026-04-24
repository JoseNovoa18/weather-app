from src.services.weather_service import fetch_weather
from src.utils.formatter import format_weather


def main():
    print("🌤 Aplicación del Clima\n")

    city = input("Ingresa una ciudad: ")

    try:
        weather = fetch_weather(city)
        output = format_weather(weather)
        print(output)
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()