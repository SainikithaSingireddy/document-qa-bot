from pathlib import Path
from pypdf import PdfReader
from embeddings import get_embedding
from vector_store import collection
import pdfplumber
import re

DATA_FOLDER = Path("data")

def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip()


def read_pdf(file_path):
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += clean_text(page_text) + "\n"

    return text


def chunk_text(text, chunk_size=1000, overlap=200):
    chunks = []
    start = 0
    chunk_id = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        chunks.append({
            "id": chunk_id,
            "text": chunk
        })

        chunk_id += 1
        start += chunk_size - overlap

    return chunks


if __name__ == "__main__":
    pdf_files = list(DATA_FOLDER.glob("*.pdf"))

    print(f"Found {len(pdf_files)} PDF files")

    total_embeddings = 0

    for pdf in pdf_files:
        text = read_pdf(pdf)
        chunks = chunk_text(text)

        print(f"\nDocument: {pdf.name}")
        print(f"Characters extracted: {len(text)}")
        print(f"Chunks created: {len(chunks)}")

        for i, chunk in enumerate(chunks):
            embedding = get_embedding(chunk["text"])

            collection.add(
                embeddings=[embedding],
                documents=[chunk["text"]],
                metadatas=[{"source": pdf.name, "chunk_id": i, "type": "pdf"}],
                ids=[f"{pdf.name}_{i}"]
            )

            total_embeddings += 1

    print(f"\n---- Embeddings stored in ChromaDB: {total_embeddings}----")