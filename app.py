import streamlit as st

from agents.crew import create_crew
from rag.ingest import ingest_pdf

st.set_page_config(
    page_title="Agentic RAG System",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Agentic RAG using CrewAI")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    save_path = f"database/uploaded_docs/{uploaded_file.name}"

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.button("Process PDF"):

        ingest_pdf(save_path)

        st.success("PDF indexed successfully!")

question = st.text_input(
    "Ask a question"
)

if st.button("Ask"):

    crew = create_crew()

    answer = crew.kickoff(
        inputs={
            "question": question
        }
    )

    st.markdown("## Answer")

    st.write(answer)