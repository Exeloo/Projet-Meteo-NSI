from src.system.interface.weather.Weather import Hour, Forecast
from src.utils.Config import GetConfig


def get_force(hour: Hour or Forecast) -> str or None:
    return None if hour.windspeed is None else \
        "low" if hour.windspeed < GetConfig().wind_force.get("low") else \
        "mid" if hour.windspeed < GetConfig().wind_force.get("mid") else \
        "hard"


def get_direction(hour: Hour or Forecast) -> str or None:
    return None if hour.windspeed is None else \
        "N" if hour.winddir < 23 else \
        "NE" if hour.winddir < 68 else \
        "E" if hour.winddir < 113 else \
        "SE" if hour.winddir < 158 else \
        "S" if hour.winddir < 203 else \
        "SO" if hour.winddir < 248 else \
        "O" if hour.winddir < 293 else \
        "NO" if hour.winddir < 338 else "N"
