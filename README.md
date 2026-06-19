# RAG Document Q&A Bot

## Project Overview
This project is a Retrieval-Augmented Generation (RAG) based Document Q&A system.
It allows users to ask natural language questions over multiple documents and get answers based on retrieved context from a vector database.

The system extracts text from PDF documents, splits them into chunks, generates embeddings, stores them in ChromaDB, and retrieves relevant context to answer user queries.

---

## Tech Stack
- Python 3.11+
- ChromaDB (Vector Database)
- pdfplumber (PDF extraction)
- Google Gemini Embeddings API (or equivalent embedding model)
- Regex (text cleaning)

---

##  Architecture

1. **Document Ingestion**
   - Load PDFs from `/data`
   - Extract text using pdfplumber

2. **Text Chunking**
   - Split text into overlapping chunks (1000 chars, overlap 200)

3. **Embedding Generation**
   - Convert each chunk into vector embeddings

4. **Vector Storage**
   - Store embeddings in ChromaDB with metadata (source filename)

5. **Retrieval**
   - Convert user query into embedding
   - Perform similarity search in ChromaDB

6. **Answer Generation**
   - Combine retrieved chunks
   - Generate grounded response based on context

---

## Project Structure

document-qa-bot/
│
├── data/ # PDF documents
├── src/
│ ├── ingest.py # Document ingestion pipeline
│ ├── query.py # Q&A chatbot (CLI)
│ ├── embeddings.py # Embedding generation
│ ├── vector_store.py # ChromaDB setup
│
├── requirements.txt
├── README.md

### ⚙️ Setup Instructions
### 1. Clone Repository
git clone <repo-url>
cd document-qa-bot

### 2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Add API Key
Create a `.env` file:
GOOGLE_API_KEY=your_api_key_here

### 5. Run Ingestion
python src/ingest.py

### 6. Run Query Bot
python src/query.py

### 🧪 Example Queries
- What is Artificial Intelligence?
- Explain deep learning
- What is cybersecurity?
- How does RAG work?
- What is space exploration?

### ⚠️ Known Limitations
- PDF text extraction may contain minor formatting issues
- Works best with text-based PDFs (not scanned images)
- Currently CLI-based (no UI)
- Embedding model dependency required for setup