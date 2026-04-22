from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore  # <-- The new, official package
from src.config import GOOGLE_API_KEY, QDRANT_URL, QDRANT_API_KEY, COLLECTION_NAME, EMBEDDING_MODEL, CHUNK_SIZE, CHUNK_OVERLAP

def ingest_documents():
    print("Loading documents...")
    loader = PyPDFDirectoryLoader("data/")
    documents = loader.load()

    print(f"Loaded {len(documents)} document pages. Splitting text...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ".", " ", ""]
    )
    chunks = text_splitter.split_documents(documents)
    
    print(f"Created {len(chunks)} chunks. Generating embeddings and pushing to Qdrant...")

    embeddings = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL, 
        google_api_key=GOOGLE_API_KEY
    )
    
    # The updated syntax for the new package
    QdrantVectorStore.from_documents(
        documents=chunks,
        embedding=embeddings,
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
        collection_name=COLLECTION_NAME,
        force_recreate=True 
    )

    print("Ingestion complete!")

if __name__ == "__main__":
    ingest_documents()