# RAG Document Q&A Bot

A **Retrieval-Augmented Generation (RAG)** based AI system that allows users to ask questions from uploaded documents (PDFs) and get accurate answers using semantic search + LLM.

---

##  Live Demo
https://document-app-bot-4gav9uf8bbxb4idkj4mapm.streamlit.app/

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
## 📁 Project Structure
```text
document-qa-bot/
├── app.py
├── src/
│   ├── query.py
│   ├── ingest.py
│   ├── embeddings.py
│   ├── vector_store.py
├── data/
├── db/
├── requirements.txt
├── .env
└── README.md

```


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
git clone https://github.com/SainikithaSingireddy/document-qa-bot.git
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

### Status

✔ RAG pipeline working  
✔ Document retrieval functional  
✔ Streamlit UI working  
✔ Project ready for demo