from src.system.interface.ip.request import get_ip_city
from src.system.interface.weather.WeatherRequest import request_weather


class WeatherContainer:  # contient une classe
    def __init__(self, city: str):
        self.value: Weather = Weather(city)  # transforme dictionnaire en classe weather


class Weather:
    def __init__(self, city: str):  # on ne modifie, supprime,créé rien
        request = request_weather(city)
        self._content: dict = request.content

        self.queryCost: str = self._content.get("queryCost")
        self.latitude: int = self._content.get("latitude")
        self.longitude: int = self._content.get("longitude")
        self.resolvedAddress: int = self._content.get("resolvedAddress")
        self.address: str = self._content.get("address")
        self.timezone: int = self._content.get("timezone")
        self.tzoffset: str = self._content.get("tzoffset")
        self.description: int = self._content.get("latitude")

        self.currentConditions: CurrentConditions = CurrentConditions(self._content.get("currentConditions")) \
            if self._content.get(
            "currentConditions") is not None else None  # valeur particulière, attributs dans la classe CurrentConditions

        self.days: [Forecast] = [Forecast(item) for item in self._content.get("days")] \
            if self._content.get("days") is not None else None  # liste en compréhension de "days"

    def __str__(self) -> str:  # renvoie str du dictionnaire
        return str(self._content)


class CurrentConditions:
    def __init__(self, content):
        self._content = content
        self.datetime: str = self._content.get("datetime")
        self.datetimeEpoch: int = self._content.get("datetimeEpoch")
        self.temp: int = self._content.get("temp")
        self.feelslike: int = self._content.get("feelslike")
        self.humidity: int = self._content.get("humidity")
        self.dew: str = self._content.get("dew")
        self.precip: int = self._content.get("precip")
        self.precipprob: str = self._content.get("precipprob")
        self.snow: int = self._content.get("snow")
        self.snowdepth: str = self._content.get("snowdepth")
        self.preciptype: int = self._content.get("preciptype")
        self.windgust: int = self._content.get("windgust")
        self.windspeed: float = self._content.get("windspeed")
        self.winddir: float = self._content.get("winddir")
        self.pressure: float = self._content.get("pressure")
        self.visibility: str = self._content.get("visibility")
        self.cloudcover: int = self._content.get("cloudcover")
        self.solarradiation: str = self._content.get("solarradiation")
        self.solarenergy: int = self._content.get("solarenergy")
        self.uvindex: int = self._content.get("uvindex")
        self.conditions: int = self._content.get("conditions")
        self.icon: str = self._content.get("icon")
        self.sunrise: int = self._content.get("sunrise")
        self.sunriseEpoch: str = self._content.get("sunriseEpoch")
        self.sunset: int = self._content.get("sunset")
        self.sunsetEpoch: str = self._content.get("sunsetEpoch")
        self.moonphase: int = self._content.get("moonphase")

    def __str__(self) -> str:
        return str(self._content)


class Hour:
    def __init__(self, content):
        self._content = content
        self.datetime: str = self._content.get("datetime")
        self.datetimeEpoch: int = self._content.get("datetimeEpoch")
        self.temp: int = self._content.get("temp")
        self.feelslike: int = self._content.get("feelslike")
        self.dew: str = self._content.get("dew")
        self.humidity: str = self._content.get("")
        self.precip: int = self._content.get("precip")
        self.precipprob: str = self._content.get("precipprob")
        self.preciptype: int = self._content.get("preciptype")
        self.snow: int = self._content.get("snow")
        self.snowdepth: str = self._content.get("snowdepth")
        self.windgust: int = self._content.get("windgust")
        self.windspeed: int = self._content.get("windspeed")
        self.winddir: float = self._content.get("winddir")
        self.pressure: int = self._content.get("pressure")
        self.cloudcover: int = self._content.get("cloudcover")
        self.visibility: str = self._content.get("visibility")
        self.solarradiation: str = self._content.get("solarradiation")
        self.solarenergy: int = self._content.get("solarenergy")
        self.uvindex: int = self._content.get("uvindex")
        self.severerisk: str = self._content.get("severerisk")
        self.conditions: int = self._content.get("conditions")
        self.icon: str = self._content.get("icon")
        self.source: str = self._content.get("source")

    def __str__(self) -> str:
        return str(self._content)


class Forecast:
    def __init__(self, content):
        self._content = content
        self.datetime: str = self._content.get("datetime")
        self.datetimeEpoch: int = self._content.get("datetimeEpoch")
        self.tempmax: int = self._content.get("tempmax")
        self.tempmin: int = self._content.get("tempmin")
        self.temp: int = self._content.get("temp")
        self.feelslikemax: int = self._content.get("feelslikemax")
        self.feelslikemin: int = self._content.get("feelslikemin")
        self.feelslike: int = self._content.get("feelslike")
        self.dew: str = self._content.get("dew")
        self.humidity: str = self._content.get("")
        self.precip: int = self._content.get("precip")
        self.precipprob: str = self._content.get("precipprob")
        self.precipcover: str = self._content.get("precipcover")
        self.preciptype: int = self._content.get("preciptype")
        self.snow: int = self._content.get("snow")
        self.snowdepth: str = self._content.get("snowdepth")
        self.windgust: int = self._content.get("windgust")
        self.windspeed: int = self._content.get("windspeed")
        self.winddir: str = self._content.get("winddir")
        self.pressure: int = self._content.get("pressure")
        self.cloudcover: int = self._content.get("cloudcover")
        self.visibility: str = self._content.get("visibility")
        self.solarradiation: str = self._content.get("solarradiation")
        self.solarenergy: int = self._content.get("solarenergy")
        self.uvindex: int = self._content.get("uvindex")
        self.severerisk: str = self._content.get("severerisk")
        self.sunrise: int = self._content.get("sunrise")
        self.sunriseEpoch: str = self._content.get("sunriseEpoch")
        self.sunset: int = self._content.get("sunset")
        self.sunsetEpoch: str = self._content.get("sunsetEpoch")
        self.moonphase: int = self._content.get("moonphase")
        self.conditions: int = self._content.get("conditions")
        self.icon: str = self._content.get("icon")
        self.source: str = self._content.get("source")

        self.hours: [Hour] = [Hour(item) for item in self._content.get("hours")] \
            if self._content.get("hours") is not None else None

    def __str__(self) -> str:
        return str(self._content)


def get_weather(city: str or None) -> WeatherContainer:
    return WeatherContainer(city) if city is not None else WeatherContainer(get_ip_city())
