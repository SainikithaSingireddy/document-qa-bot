import os
from pypdf import PdfReader
from embeddings import get_embedding
from vector_store import collection

DATA_DIR = "data"


def read_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text


def chunk_text(text, size=800):
    return [text[i:i+size] for i in range(0, len(text), size)]


print("Starting ingestion...")

for file in os.listdir(DATA_DIR):

    if not file.endswith(".pdf"):
        continue

    path = os.path.join(DATA_DIR, file)

    print(f"\nProcessing: {file}")

    text = read_pdf(path)
    chunks = chunk_text(text)

    print(f"Chunks: {len(chunks)}")

    for i, chunk in enumerate(chunks):

        embedding = get_embedding(chunk)

        collection.add(
            ids=[f"{file}_{i}"],
            documents=[chunk],
            embeddings=[embedding],
            metadatas=[{"source": file}]
        )

print("\nDONE INGESTION ✔")