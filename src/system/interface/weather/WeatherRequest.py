import requests

from src.utils.Config import GetConfig  # récupération de notre configuration
from src.system.interface.ip.request import get_ip_city  # récupération de la fonction qui nous permet de savoir ville où se trouve notre requête


class WeatherRequest:
    def __init__(self, city: str = get_ip_city()):  # str par défaut, prend la valeur de la ville (requête)
        assert city is not None, "None city"
        url: str = \
            f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?" \
            f"key={GetConfig().api_key}&unitGroup=metric&include=fcst%2Chours%2Ccurrent"
        try:  # évite erreurs si il y en a
            with requests.get(url) as request:  # request.get(url)=request
                self.request = request
                self.content = request.json()
                self.url = request.url
                self.status_code = request.status_code
                self.headers = request.headers
                self.cookies = request.cookies
        except requests.RequestException:  # renvoie None si erreur
            self.request = None
            self.content = None
            self.url = None
            self.status_code = "Request Error"
            self.headers = None
            self.cookies = None
            print("Request Error")


def request_weather(city: str) -> WeatherRequest:  # récupère la valeur de notre classe
    return WeatherRequest(city) if city is not None else WeatherRequest()
