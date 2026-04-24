def format_weather(weather) -> str:
    return (
        f"\n📍 Ciudad: {weather.city}, {weather.country}\n"
        f"🌡 Temperatura: {weather.temperature}°C\n"
        f"💨 Viento: {weather.windspeed} km/h\n"
        f"🧭 Dirección del viento: {weather.winddirection}°\n"
        f"🔢 Código clima: {weather.weathercode}\n"
    )