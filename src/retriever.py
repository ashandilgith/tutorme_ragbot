from langchain_qdrant import QdrantVectorStore # <-- The new, official package
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from src.config import GOOGLE_API_KEY, QDRANT_URL, QDRANT_API_KEY, COLLECTION_NAME, EMBEDDING_MODEL

def get_retriever():
    embeddings = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL, 
        google_api_key=GOOGLE_API_KEY
    )
    
    # The modernized way to connect to an existing database
    vector_store = QdrantVectorStore.from_existing_collection(
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
    )
    
    return vector_store.as_retriever(search_kwargs={"k": 4})