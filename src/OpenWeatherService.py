import requests

from icecream import ic


class WeatherService:

    def __init__(self):
        self.api_key_openweather = 'a3f7fc06b9c817195a3628e4ea5b3c26'

    def get_weather(self, city):
        params = {
            'q': city,
            'appid': self.api_key_openweather,
            'units': 'metric',

            }

        url = 'https://api.openweathermap.org/data/2.5/weather'
        response = requests.get(url, params=params)
        return response.json()


if __name__ == '__main__':
    service = WeatherService()

    print(service.get_weather('Moscow'))
