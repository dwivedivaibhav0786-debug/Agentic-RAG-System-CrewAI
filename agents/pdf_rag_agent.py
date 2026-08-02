from crewai import Agent
from config.llm_config import load_llm
from tools.rag_tool import pdf_rag_tool


pdf_agent = Agent(

    role="PDF RAG Specialist",

    goal="""
    Answer questions only using uploaded PDF documents.
    """,

    backstory="""
    You specialize in retrieving information from PDFs.
    """,

    tools=[
        pdf_rag_tool
    ],

    llm=load_llm(),

    verbose=True
)