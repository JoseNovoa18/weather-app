from dataclasses import dataclass


@dataclass
class Weather:
    city: str
    country: str
    temperature: float
    windspeed: float
    winddirection: float
    weathercode: int