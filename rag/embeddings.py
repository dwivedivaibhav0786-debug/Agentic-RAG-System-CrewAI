from langchain_huggingface import HuggingFaceEmbeddings

from utils.constants import EMBEDDING_MODEL


def get_embedding_model():

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    return embeddings