import streamlit as st
import sys
import os

# Add src folder to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from query import ask_question

st.set_page_config(
    page_title="RAG Document Q&A Bot",
    page_icon="📚",
    layout="wide"
)

st.title("RAG Document Q&A Bot")
st.write("Ask questions about the documents stored in the knowledge base.")

question = st.text_input(
    "Enter your question:",
    placeholder="Example: What is Artificial Intelligence?"
)

if st.button("Ask Question"):

    if question.strip():

        with st.spinner("Searching documents and generating answer..."):

            try:
                answer = ask_question(question)

                st.success("Answer Generated")

                st.subheader("Answer")
                st.write(answer)

            except Exception as e:
                st.error(f"Error: {str(e)}")

    else:
        st.warning("Please enter a question.")