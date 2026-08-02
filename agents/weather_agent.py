from crewai import Agent

from tools.weather_tool import WeatherTool

from config.llm_config import load_llm



weather_agent = Agent(

    role="Weather Specialist",

    goal="""
    Provide accurate weather information
    using OpenWeather API.
    """,

    backstory="""
    You specialize in current weather analysis.
    """,

    tools=[
        WeatherTool()
    ],

    llm=load_llm(),

    function_calling_llm=None,

    verbose=True
)