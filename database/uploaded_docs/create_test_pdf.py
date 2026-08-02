from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os


output_path = (
    "database/uploaded_docs/"
    "agentic_rag_document.pdf"
)


os.makedirs(
    "database/uploaded_docs",
    exist_ok=True
)


content = """
Agentic RAG System Using CrewAI


Introduction

Agentic RAG combines Large Language Models,
Retrieval Augmented Generation, and autonomous
AI agents to answer user questions.


System Agents


1. Manager Agent

The Manager Agent understands user questions,
classifies user intent, selects specialist agents,
and combines multiple responses.


2. PDF RAG Agent

The PDF RAG Agent answers questions from uploaded
PDF documents.

The workflow includes:

- Extracting PDF text
- Splitting documents into chunks
- Creating embeddings
- Storing embeddings in FAISS
- Retrieving relevant information
- Generating answers


3. Web Search Agent

The Web Search Agent handles current information
questions using search APIs.

It provides answers with source links.


4. Weather Agent

The Weather Agent connects with OpenWeather API.

It provides:

- Temperature
- Humidity
- Wind speed
- Weather conditions


Vector Database

FAISS is used as the vector database.

FAISS stores document embeddings and performs
similarity searches to find relevant information.


Embeddings

The project uses the Sentence Transformer model:

all-MiniLM-L6-v2


CrewAI

CrewAI manages collaboration between multiple AI
agents.

Each agent has a specific role and uses tools
to complete tasks.


Example Questions


Question:

What does the PDF RAG Agent do?


Answer:

The PDF RAG Agent retrieves information from
uploaded documents using embeddings and FAISS.


Question:

Which embedding model is used?


Answer:

The system uses all-MiniLM-L6-v2.


Future Improvements

- Add conversational memory
- Support multiple PDFs
- Add citation support
- Add more specialist agents
- Deploy using Docker
"""


pdf = canvas.Canvas(
    output_path,
    pagesize=letter
)


width, height = letter

text = pdf.beginText(
    50,
    height - 50
)

text.setFont(
    "Helvetica",
    11
)


for line in content.split("\n"):

    text.textLine(line)


pdf.drawText(text)

pdf.save()


print(
    f"Created PDF: {output_path}"
)