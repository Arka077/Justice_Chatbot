# pages/legal_chatbot.py

import streamlit as st
from rag_indexer import index_query_from_google
from rag_qa import answer_query_with_context
#from shared_sidebar import render_sidebar  # Optional if you use sidebar

st.title("🤖 Legal Assistant Chatbot")

user_query = st.chat_input("Ask a legal question...")
if user_query:
    with st.spinner("Fetching relevant legal data..."):
        index_query_from_google(user_query)
    with st.spinner("Answering your question..."):
        answer = answer_query_with_context(user_query)

    # Display question + answer together
    st.chat_message("assistant").write(
        f"**Your Question:** {user_query}\n\n**Answer:** {answer}"
    )

