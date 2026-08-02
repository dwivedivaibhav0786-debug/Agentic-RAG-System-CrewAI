from crewai.tools import BaseTool

from rag.retriever import get_retriever


class PDFRAGTool(BaseTool):

    name: str = "pdf_rag_tool"

    description: str = """
    Search uploaded PDF documents and answer questions
    using retrieved document context.
    """

    def _run(self, question: str):

        retriever = get_retriever()

        if retriever is None:
            return "Vector database not available."

        docs = retriever.invoke(question)

        if not docs:
            return "No relevant information found in PDF."

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        return context


pdf_rag_tool = PDFRAGTool()