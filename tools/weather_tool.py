import requests

from crewai.tools import BaseTool

from config.settings import OPENWEATHER_API_KEY



class WeatherTool(BaseTool):

    name: str = "weather_tool"

    description: str = """
    Get current weather information
    for a city.
    """


    def _run(
        self,
        city: str
    ):


        url = (
            "https://api.openweathermap.org/"
            "data/2.5/weather"
        )


        params = {

            "q": city,

            "appid":
            OPENWEATHER_API_KEY,

            "units":
            "metric"

        }


        response = requests.get(

            url,

            params=params

        )


        if response.status_code != 200:

            return response.text


        data = response.json()


        return {

            "city":
            data["name"],

            "temperature":
            data["main"]["temp"],

            "humidity":
            data["main"]["humidity"],

            "wind_speed":
            data["wind"]["speed"],

            "condition":
            data["weather"][0]["description"]

        }