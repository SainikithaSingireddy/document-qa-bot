# RAG Document Q&A Bot

A **Retrieval-Augmented Generation (RAG)** based AI system that allows users to ask questions from uploaded documents (PDFs) and get accurate answers using semantic search + LLM.

---

##  Live Demo
https://your-streamlit-url-here

---

##  Project Overview

This project implements a **RAG pipeline**:

1. Load documents (PDFs)
2. Extract and chunk text
3. Convert text into embeddings
4. Store embeddings in a vector database (ChromaDB)
5. Retrieve relevant chunks using similarity search
6. Generate answers using Google Gemini LLM

---

##  Tech Stack

- Python 
- Streamlit (Frontend UI)
- Google Gemini API (LLM + Embeddings)
- ChromaDB (Vector Database)
- PyPDF (PDF text extraction)
- dotenv (Environment variables)

---

## Project Structure

document-qa-bot/
│
├── app.py # Streamlit UI
├── src/
│ ├── query.py # RAG pipeline (retrieve + generate)
│ ├── ingest.py # Document ingestion pipeline
│ ├── embeddings.py # Embedding generation
│ ├── vector_store.py # ChromaDB setup
│
├── data/ # PDF documents
├── db/ # Vector database storage
├── requirements.txt
├── .env
└── README.md


---

##  How It Works

### 1. Document Ingestion
- PDFs are read using PyPDF
- Text is split into chunks

### 2. Embedding Generation
- Each chunk is converted into vector embeddings using:
  - `models/gemini-embedding-2`

### 3. Vector Storage
- Embeddings stored in ChromaDB

### 4. Query Flow
- User question → embedding generated
- Similar chunks retrieved from DB
- Context passed to Gemini LLM
- Final answer generated

---

##  How to Run Locally

1. Clone repo
```bash
git clone https://github.com/your-repo/document-qa-bot.git
cd document-qa-bot

2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

3. Install dependencies
pip install -r requirements.txt

4. Add API key in .env
GOOGLE_API_KEY=your_api_key_here

5. Run ingestion
python src/ingest.py

6. Run application
streamlit run app.py

----------
### Status
----------

✔ RAG pipeline working  
✔ Document retrieval functional  
✔ Streamlit UI working  
✔ Project ready for demo