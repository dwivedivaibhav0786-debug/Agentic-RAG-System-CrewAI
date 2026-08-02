from crewai import LLM
import os
from dotenv import load_dotenv

load_dotenv()


def load_llm():
    return LLM(
        model="command-r-plus",
        provider="cohere",
        api_key=os.getenv("COHERE_API_KEY"),
        temperature=0.2
    )