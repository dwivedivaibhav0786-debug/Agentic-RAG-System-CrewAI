from crewai import Task


def create_tasks(
        pdf_agent,
        weather_agent,
        search_agent
):

    return [

        Task(

            description="""

            Answer the user question:

            {question}

            Decide which specialist agent should handle this.

            After delegation, return the exact useful information
            provided by the specialist.

            Do not create fake/sample responses.

            """,

            expected_output="""

            A complete final answer for the user.

            Include:
            - Actual values from tools
            - Sources when available
            - No placeholder text

            """

        )

    ]