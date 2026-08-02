from rag.ingest import ingest_pdf


if __name__ == "__main__":

    pdf_path = (
        "database/uploaded_docs/"
        "agentic_rag_document.pdf"
    )

    ingest_pdf(
        pdf_path
    )

    print(
        "PDF indexed successfully"
    )