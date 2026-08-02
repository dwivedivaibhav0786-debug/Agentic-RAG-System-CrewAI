import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")

UPLOAD_DIR = "database/uploaded_docs"
VECTOR_DB = "database/faiss_index"