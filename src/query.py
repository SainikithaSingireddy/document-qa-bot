import os
import time
from embeddings import get_embedding
from vector_store import collection
from google import genai


client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

last_call_time = 0

def rate_limit():
    global last_call_time
    if time.time() - last_call_time < 3:
        time.sleep(3)
    last_call_time = time.time()



def safe_generate(prompt):
    for _ in range(3):
        try:
            rate_limit()

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:
            print("Retrying due to API limit or error...")
            time.sleep(5)

    return "API limit reached. Please try again later."


def retrieve_chunks(question, k=3):
    query_embedding = get_embedding(question)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    return results["documents"][0], results["metadatas"][0]

def generate_answer(question, chunks, metadata):

    context = "\n\n".join(
        [
            f"[SOURCE: {meta['source']}]\n{chunk}"
            for chunk, meta in zip(chunks, metadata)
        ]
    )

    prompt = f"""
You are a strict document-based AI assistant.

RULES:
- Use ONLY the given context
- If answer is not in context, say: "Not found in documents"
- Do NOT use external knowledge

Context:
{context}

Question: {question}

Answer clearly and concisely:
"""

    return safe_generate(prompt)

def ask_question(question):
    chunks, metadata = retrieve_chunks(question)
    answer = generate_answer(question, chunks, metadata)

    return answer

if __name__ == "__main__":
    print("\n🤖 RAG Document Q&A Bot Ready!\n")

    while True:
        q = input("Ask a question (or type 'exit'): ")

        if q.lower() == "exit":
            break

        answer = ask_question(q)

        print("\n" + "=" * 60)
        print("\n Answer:\n")
        print(answer)
        print("\n" + "=" * 60 + "\n")