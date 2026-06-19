from embeddings import get_embedding
from vector_store import collection
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def retrieve_chunks(question, k=5):
    """Retrieve top-k similar chunks from ChromaDB"""

    query_embedding = get_embedding(question)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    chunks = results["documents"][0]
    metadata = results["metadatas"][0]

    return chunks, metadata


def generate_answer(question, chunks, metadata):
    """Generate grounded answer using retrieved context"""

    context = ""

    for chunk, meta in zip(chunks, metadata):
        context += f"""
[Source: {meta['source']}]

{chunk}

----------------------------------
"""

    prompt = f"""
You are a Document Q&A Assistant.

Use ONLY the provided context to answer.

If the answer is not present in the context, reply:

"I cannot find the answer in the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    answer = response.text

    sources = list(set([meta["source"] for meta in metadata]))

    answer += "\n\nSources:\n"

    for source in sources:
        answer += f"- {source}\n"

    return answer


def ask_question(question):
    chunks, metadata = retrieve_chunks(question)

    answer = generate_answer(
        question,
        chunks,
        metadata
    )

    return answer


if __name__ == "__main__":
    print("\n RAG Document Q&A Bot Ready!\n")

    while True:
        q = input("Ask a question (or type 'exit'): ")

        if q.lower() == "exit":
            break

        answer = ask_question(q)

        print("\n" + "=" * 60)
        print("\n📚 Answer:\n")
        print(answer)
        print("\n" + "=" * 60 + "\n")