import requests


def get_ip_city() -> str:
    url = "http://ip-api.com/json/"
    return requests.get(url).json().get("city")
