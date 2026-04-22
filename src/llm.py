from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from src.config import GOOGLE_API_KEY, LLM_MODEL

def get_prompt():
    system_prompt = """You are a helpful assistant for tutors. 
    Answer the question based ONLY on the provided context below.
    
    If the context does not contain the answer or you are unsure, you must output exactly: "I don't know."
    Do not attempt to guess, infer, or use outside knowledge.
    
    If you find the answer, briefly cite the source document name and section (e.g., "According to leave_policy.pdf...") in your response.

    Context:
    {context}"""
    
    return ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])

def get_llm():
    # Temperature 0 is critical here to prevent creative hallucinations
    return ChatGoogleGenerativeAI(
        model=LLM_MODEL, 
        google_api_key=GOOGLE_API_KEY, 
        temperature=0 
    )