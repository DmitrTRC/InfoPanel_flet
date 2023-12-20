import requests


class WeatherService:

    def __init__(self):
        self.api_key_openweather = 'a3f7fc06b9c817195a3628e4ea5b3c26'


def get_weather(self, city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key_openweather}&units=metric'
    response = requests.get(url)
    return response.json()
