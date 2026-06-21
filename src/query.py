import os
import google.generativeai as genai
from dotenv import load_dotenv

from src.embeddings import get_embedding
from src.vector_store import collection

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_question(question):
    try:
        query_embedding = get_embedding(question)
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=5
        )

        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]

        if not documents:
            return {
                "answer": "No relevant information was found in the uploaded documents.",
                "sources": []
            }
        
        context = "\n\n".join(documents)

        prompt = f"""
You are a helpful document assistant.

Answer the question ONLY using the provided context.

If the answer is not available in the context, respond exactly with:

Not found in documents.

Context:
{context}

Question:
{question}
"""

        response = model.generate_content(prompt)

        return {
            "answer": response.text.strip(),
            "sources": metadatas
        }

    except Exception:
        return {
            "answer": "⚠️ Unable to process your request at the moment. Please try again later.",
            "sources": []
        }