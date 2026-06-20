import os
import google.generativeai as genai
from dotenv import load_dotenv

from src.embeddings import get_embedding
from src.vector_store import collection

load_dotenv()


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def ask_question(question):

    try:
       
        query_embedding = get_embedding(question)

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=3
        )

        docs = results.get("documents", [[]])[0]

        if not docs:
            return {
                "answer": "Not found in documents.",
                "sources": []
            }

        context = "\n\n".join(docs)

        prompt = f"""
You are a helpful assistant. Answer ONLY using the context below.

Context:
{context}

Question:
{question}

Answer clearly and concisely.
"""

        # 4. Call Gemini model
        model = genai.GenerativeModel("gemini-1.5-flash")

        response = model.generate_content(prompt)

        return {
            "answer": response.text,
            "sources": results.get("metadatas", [[]])[0]
        }

    except Exception as e:
        return {
            "answer": f"Error: {str(e)}",
            "sources": []
        }