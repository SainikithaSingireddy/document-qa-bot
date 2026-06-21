import streamlit as st
from src.query import ask_question

st.set_page_config(
    page_title="RAG Document Q&A Bot",
    page_icon="📄",
    layout="centered"
)

st.title("📄 RAG Document Q&A Bot")

st.markdown(
    """
Ask questions about documents stored in the knowledge base.

Examples:
- What is Artificial Intelligence?
- Summarize the document
- What topics are covered?
"""
)

question = st.text_input(
    "Enter your question:",
    placeholder="Type your question here..."
)

if question:
    with st.spinner("Searching documents and generating answer..."):
        result = ask_question(question)

    st.divider()

    st.subheader("Answer")
    st.write(result.get("answer", "No answer available."))

    st.divider()

    st.subheader("Sources")

    sources = result.get("sources", [])

    if sources:
        unique_sources = []

        for source in sources:
            file_name = source.get("source", "Unknown")

            if file_name not in unique_sources:
                unique_sources.append(file_name)

        for file_name in unique_sources:
            st.success(f"{file_name}")

    else:
        st.info("No sources found.")