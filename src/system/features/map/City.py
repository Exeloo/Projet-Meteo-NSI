from src.system.interface.weather.Weather import Weather, Hour
from src.utils.Config import GetConfig
from src.system.features.wind_function import get_force, get_direction

config = GetConfig()


class CurrentCity:
    def __init__(self, content: Weather):
        current = content.currentConditions
        self.weather = current.icon
        self.temp = current.temp
        hour = None
        for i in content.days[0].hours:
            if i.windspeed is not None:
                hour = i
                break
        if hour is None:
            return
        self.force = get_force(hour)
        self.direction = get_direction(hour)


class HourlyCity:
    def __init__(self, content: Weather, time: str):
        hour = get_hour(content, time)
        self.weather = hour.icon
        self.temp = hour.temp
        self.force = get_force(hour)
        self.direction = get_direction(hour)


def get_hour(content: Weather, time: str) -> Hour:
    return content.days[0].hours[8] if time == "TODAY_MORN" else \
        content.days[0].hours[15] if time == "TODAY_AFTER" else \
        content.days[1].hours[8] if time == "TOMORROW_MORN" else \
        content.days[1].hours[15] if time == "TOMORROW_AFTER" else \
        content.days[2].hours[11] if time == "AFTER_TOMORROW" else \
        content.days[3].hours[11]
