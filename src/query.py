import os
from dotenv import load_dotenv
from google import genai

from src.embeddings import get_embedding
from src.vector_store import collection

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def retrieve_chunks(question, k=3):

    query_embedding = get_embedding(question)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k,
        include=["documents", "metadatas"]
    )

    return results["documents"][0], results["metadatas"][0]



def generate_answer(question, chunks, metadata):

    context = "\n\n".join(
        [f"{m['source']}:\n{c}" for c, m in zip(chunks, metadata)]
    )

    prompt = f"""
You are a helpful assistant.

Answer ONLY using the context below.
If answer is not found, say "Not found in documents".

Context:
{context}

Question:
{question}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text

    except Exception:
        return (
            "⚠ LLM temporarily unavailable due to API limits.\n\n"
            "But retrieval is working.\n\n"
            "Top relevant document chunk:\n\n"
            f"{chunks[0] if chunks else 'No context found'}"
        )


def ask_question(question):

    chunks, metadata = retrieve_chunks(question)

    if not chunks:
        return {
            "answer": "Not found in documents",
            "sources": []
        }

    answer = generate_answer(question, chunks, metadata)

    return {
        "answer": answer,
        "sources": list(set([m["source"] for m in metadata]))
    }