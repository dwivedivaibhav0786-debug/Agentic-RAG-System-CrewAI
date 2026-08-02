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

The project implements a multi-agent
question answering system using CrewAI.

Agents:

1. Manager Agent

The Manager Agent understands user questions,
selects the correct specialist agent,
and combines multiple answers.


2. PDF RAG Agent

The PDF RAG Agent answers questions from
uploaded PDF documents.

Process:

- Extract PDF text
- Split text into chunks
- Generate embeddings
- Store embeddings in FAISS
- Retrieve relevant chunks
- Generate answers


3. Web Search Agent

The Web Search Agent answers current
information questions.

It uses search APIs and returns source links.


4. Weather Agent

The Weather Agent provides:

Temperature
Humidity
Wind Speed
Weather Condition


Vector Database:

FAISS is used to store document embeddings
and perform similarity search.


Embedding Model:

all-MiniLM-L6-v2


CrewAI:

CrewAI manages communication between
multiple AI agents.


Example Questions:

What is the responsibility of the Manager Agent?

Which embedding model is used?

How does PDF RAG work?


Future Improvements:

- Add memory
- Multiple PDF support
- Citation generation
- More AI agents
"""


pdf = canvas.Canvas(
    output_path,
    pagesize=letter
)


text = pdf.beginText(
    50,
    750
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
    "PDF created:",
    output_path
)