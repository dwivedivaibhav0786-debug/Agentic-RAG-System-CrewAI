import requests

from crewai.tools import BaseTool

from config.settings import SERPER_API_KEY



class SearchTool(BaseTool):

    name: str = "web_search_tool"


    description: str = """
    Search the internet and return
    current information with sources.
    """


    def _run(
        self,
        query: str
    ):


        url = (
            "https://google.serper.dev/search"
        )


        headers = {

            "X-API-KEY":
            SERPER_API_KEY,

            "Content-Type":
            "application/json"

        }


        response = requests.post(

            url,

            headers=headers,

            json={
                "q":query
            }

        )


        data=response.json()


        results=[]


        for item in data.get(
            "organic",
            []
        )[:5]:


            results.append(

                {
                "title":
                item.get("title"),

                "link":
                item.get("link"),

                "snippet":
                item.get("snippet")

                }

            )


        return results