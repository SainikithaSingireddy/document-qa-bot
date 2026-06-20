import streamlit as st
from src.query import ask_question

st.title("RAG Document Q&A Bot")

question = st.text_input("Ask a question")

if question:
    result = ask_question(question)

    st.subheader("Answer")
    st.write(result["answer"])

    st.subheader("Sources")
    st.write(result["sources"])