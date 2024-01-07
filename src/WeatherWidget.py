import flet as ft

from src.OpenWeatherService import WeatherService

from pprint import pprint


class WeatherWidget(ft.UserControl):

    def __init__(self, page):

        super().__init__()

        self.page = page
        self.city_input = ft.TextField(label="Enter city name", width=300, value='Koltushi')
        self.view = None
        self.city = None
        self.weather_info = None
        self.weather_provider = WeatherService()
        self.get_weather_btn = None
        self.get_weather_btn = ft.TextButton(text="Get Weather", on_click=self.update_weather_info)
        self.weather_info = ft.Text()

    def build(self):

        # Layout
        self.view = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        self.city_input,
                        self.get_weather_btn
                        ],
                    alignment=ft.MainAxisAlignment.CENTER
                    ),
                self.weather_info
                ],
            alignment=ft.MainAxisAlignment.START
            )

        return self.view

    def update_weather_info(self, e=None):
        # Fetch weather data and update UI
        self.city = self.city_input.value
        weather_data = self.weather_provider.get_weather(self.city)

        pprint(weather_data)

        if weather_data:
            temperature = weather_data["main"]["temp"]
            condition = weather_data["weather"][0]["description"]
            self.weather_info.value = f"Weather in {self.city}: {condition}, Temperature: {temperature}°C"

        else:
            self.weather_info.value = "Weather data not available."

        self.page.update()
