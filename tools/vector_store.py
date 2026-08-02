from langchain_community.vectorstores import FAISS
from tools.embeddings import get_embeddings


VECTOR_PATH = "database/faiss_index"


def load_vector_store():

    embeddings = get_embeddings()

    try:

        vector_store = FAISS.load_local(
            VECTOR_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )

        return vector_store

    except Exception as e:

        print("Vector store loading error:", e)
        return None