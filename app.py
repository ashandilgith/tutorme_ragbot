import streamlit as st
import os
from src.chat import get_rag_response

st.set_page_config(page_title="Tutor AI Assistant", page_icon="📚")
st.title("Tutor Q&A Assistant")
st.caption("Ask questions about company policies or student IEPs. Grounded strictly in company data.")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle new user input
if prompt := st.chat_input("Ask a question... (e.g., 'What is the leave policy?')"):
    
    # Add user message to state and display it
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response
    with st.chat_message("assistant"):
        with st.spinner("Searching documents..."):
            response = get_rag_response(prompt)
            
            answer = response.get("answer", "I don't know.")
            sources = response.get("context", [])
            
            # Display the text answer
            st.markdown(answer)
            
            # If the model didn't fail gracefully, display the sources used
            if sources and "I don't know" not in answer:
                with st.expander("View Referenced Sources"):
                    # Use a set to avoid duplicating the same source file name if multiple chunks came from it
                    unique_sources = set()
                    
                    for doc in sources:
                        # Extract the filename from the filepath (e.g., data/policies/policy.pdf -> policy.pdf)
                        raw_source = doc.metadata.get('source', 'Unknown Document')
                        clean_source = os.path.basename(raw_source)
                        
                        st.markdown(f"**📄 {clean_source}**")
                        st.info(doc.page_content)
                        
    # Add assistant response to state
    st.session_state.messages.append({"role": "assistant", "content": answer})