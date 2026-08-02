from tools.pdf_loader import load_pdf

from rag.chunking import split_documents

from tools.vector_store import create_vector_store



def ingest_pdf(file_path):


    documents = load_pdf(
        file_path
    )


    chunks = split_documents(
        documents
    )


    vector_store = create_vector_store(
        chunks
    )


    return vector_store