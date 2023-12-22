import flet

from flet import (
    Page, UserControl, Column, Container, Row, Text, IconButton, NavigationRail, NavigationRailDestination, TextField,
    alignment, border_radius, colors, icons, padding, margin, TextButton, TextField, Text, Alignment
    )

from OpenWeatherService import WeatherService


class WeatherWidget(UserControl):

    def __init__(self):
        super().__init__()
        self.view = None
        self.city = None
        self.weather_info = None
        self.weather_provider = WeatherService()
        self.get_weather_btn = None
        self.city_input = None

    def build(self):
        # UI components
        self.city_input = TextField(label="Enter city name", width=300)
        self.get_weather_btn = TextButton(text="Get Weather", on_click=self.update_weather_info)
        self.weather_info = Text()

        # Layout
        self.view = Column(
            controls=[
                Row(
                    controls=[
                        self.city_input,
                        self.get_weather_btn
                        ],
                    alignment='CENTER'
                    ),
                self.weather_info
                ],
            alignment='CENTER'
            )

        return self.view

    def update_weather_info(self):
        # Fetch weather data and update UI
        self.city = self.city_input.value
        weather_data = self.weather_provider.get_weather(self.city)

        if weather_data:
            temperature = weather_data["main"]["temp"]
            condition = weather_data["weather"][0]["description"]
            self.weather_info.value = f"Weather in {self.city}: {condition}, Temperature: {temperature}°C"
        else:
            self.weather_info.value = "Weather data not available."
