from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from src.retriever import get_retriever
from src.llm import get_llm, get_prompt

def get_rag_response(query: str):
    retriever = get_retriever()
    llm = get_llm()
    prompt = get_prompt()
    
    # Chain 1: How to format the retrieved documents into the prompt
    document_chain = create_stuff_documents_chain(llm, prompt)
    
    # Chain 2: How to fetch the documents and pass them to Chain 1
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    
    # Execute
    response = retrieval_chain.invoke({"input": query})
    return response