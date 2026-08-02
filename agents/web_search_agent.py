from crewai import Agent

from tools.search_tool import SearchTool

from config.llm_config import load_llm



search_agent = Agent(

    role="Web Research Specialist",

    goal="""
    Find current information from the internet
    and provide source links.
    """,

    backstory="""
    You are an expert internet researcher.
    """,

    tools=[
        SearchTool()
    ],

    llm=load_llm(),

    function_calling_llm=None,

    verbose=True
)