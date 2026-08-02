import os

def create_directories():

    folders = [
        "database",
        "database/faiss_index",
        "database/uploaded_docs"
    ]

    for folder in folders:

        os.makedirs(folder, exist_ok=True)