from crewai import Crew, Process

from agents.manager_agent import manager_agent

from agents.pdf_rag_agent import pdf_agent
from agents.weather_agent import weather_agent
from agents.web_search_agent import search_agent

from agents.tasks import create_tasks



def create_crew():

    tasks = create_tasks(
        pdf_agent,
        weather_agent,
        search_agent
    )


    crew = Crew(

        agents=[

            pdf_agent,
            weather_agent,
            search_agent

        ],

        tasks=tasks,

        manager_agent=manager_agent,

        process=Process.hierarchical,

        verbose=True

    )


    return crew