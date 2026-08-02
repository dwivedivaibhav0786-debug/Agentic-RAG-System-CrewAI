from tools.vector_store import load_vector_store



def get_retriever():

    vector_store = load_vector_store()


    if vector_store is None:

        return None


    retriever = vector_store.as_retriever(

        search_kwargs={
            "k":5
        }

    )


    return retriever