import os
from dotenv import load_dotenv

load_dotenv()

# API Keys and Connections
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL", ":memory:") # Defaults to memory if cloud URL is missing
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

# RAG Configuration



COLLECTION_NAME = "tutor_docs_final"
EMBEDDING_MODEL = "gemini-embedding-001"


LLM_MODEL = "gemini-2.5-flash"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200