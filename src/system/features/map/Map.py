from src.system.features.map.City import CurrentCity, HourlyCity
from src.system.interface.weather.Weather import Weather
from src.utils.Config import GetConfig


class Map:
    def __init__(self, content: {str, Weather}, map_time: str):
        assert map_time in {
            "CURRENT",
            "TODAY_MORN",
            "TODAY_AFTER",
            "TOMORROW_MORN",
            "TOMORROW_AFTER",
            "AFTER_TOMORROW",
            "AFTER_AFTER_TOMORROW",
        }
        for city in GetConfig().cities.keys():
            self.__setattr__(
                city,
                CurrentCity(content.get(city)) if map_time == "CURRENT" else HourlyCity(content.get(city), map_time)
            )


def get_map_temp(content: {str, Weather}, map_time: str) -> (Map, str, str):
    return Map(content, map_time), "temp", "weather"


def get_map_wind(content: {str, Weather}, map_time: str) -> (Map, str, str):
    return Map(content, map_time), "force", "direction"
