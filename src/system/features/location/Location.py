from datetime import datetime

from src.system.features.wind_function import get_direction
from src.system.interface.weather.Weather import Weather, Forecast, Hour, get_weather


class Location:
    def __init__(self, day: Forecast, hour: Hour or None):
        if hour is None:
            self.day = day.datetime
            self.hour = None
            self.weather = day.icon
            self.wind_dir = get_direction(day)
            self.wind_speed = day.windspeed
            self.temp = day.temp
            self.feel = day.feelslike
            self.pressure = day.pressure
            self.humidity = day.humidity
            self.precipprob = day.precipprob
            self.precip = day.precip
            self.snow = day.snow
            self.snowdepth = day.snowdepth
        else:
            self.day = day.datetime
            self.hour = hour.datetime
            self.weather = hour.icon
            self.wind_dir = get_direction(hour)
            self.wind_speed = hour.windspeed
            self.temp = hour.temp
            self.feel = hour.feelslike
            self.pressure = hour.pressure
            self.humidity = hour.humidity
            self.precipprob = hour.precipprob
            self.precip = hour.precip
            self.snow = hour.snow
            self.snowdepth = hour.snowdepth
        self.sunrise = day.sunrise
        self.sunset = day.sunset


def get_location(content: Weather, time: str) -> [Location]:
    if time == "WEEK":
        return [Location(content.days[i], None) for i in range(7)], content.address
    limit = 24 if time == "DAY" else 72
    now = datetime.now().timestamp()
    hours = []
    if content.days is None:
        return
    for day in content.days:
        if day.hours is not None:
            for hour in day.hours:
                if hour.datetimeEpoch is not None and hour.datetimeEpoch >= now:
                    hours.append(Location(day, hour))
                if len(hours) >= limit:
                    return [h for i, h in enumerate(hours) if i % (limit // 7) == 0 and i != 0], content.address

