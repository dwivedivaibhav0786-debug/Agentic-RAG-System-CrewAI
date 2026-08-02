from rag.retriever import get_retriever


retriever = get_retriever()


docs = retriever.invoke(
    "What does the PDF say about CrewAI?"
)


print("Documents found:", len(docs))


for doc in docs:
    print("\n----------------")
    print(doc.page_content)
