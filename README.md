# RAG Document Q&A Bot

## Project Overview

This project is a Retrieval-Augmented Generation (RAG) based Document Question Answering system.

The application allows users to ask natural language questions about documents stored in a knowledge base and receive answers grounded in the document content.

Instead of relying only on the language model's general knowledge, the system retrieves the most relevant document chunks from a vector database and uses them as context for answer generation. This helps reduce hallucinations and improves answer accuracy.

---

## Features

- PDF document ingestion
- Text extraction and cleaning
- Text chunking with overlap
- Vector embeddings using Gemini Embeddings
- ChromaDB vector database storage
- Semantic similarity search
- Retrieval-Augmented Generation (RAG)
- Source-aware answers
- Streamlit web interface
- Public deployment support

---

## Tech Stack

- Python 3.11+
- ChromaDB
- Google Gemini API (`google-genai`)
- pdfplumber
- pypdf
- python-dotenv
- Streamlit

---

## Architecture

### 1. Document Ingestion

- Load PDF documents from the `data/` folder
- Extract text using pdfplumber
- Clean extracted text

### 2. Text Chunking

- Split documents into chunks
- Chunk Size: 1000 characters
- Overlap: 200 characters

### 3. Embedding Generation

- Generate vector embeddings using Gemini Embedding Model

### 4. Vector Storage

- Store embeddings and metadata in ChromaDB

### 5. Retrieval

- Convert user question into an embedding
- Retrieve top matching chunks using semantic similarity search

### 6. Answer Generation

- Send retrieved context and question to Gemini
- Generate grounded answers using retrieved information

---

## Project Structure

```text
document-qa-bot/
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── app.py
│
├── data/
│   ├── ai.pdf
│   ├── cybersecurity.pdf
│   └── space.pdf
│
├── db/
│
└── src/
    ├── embeddings.py
    ├── ingest.py
    ├── main.py
    ├── query.py
    └── vector_store.py
```

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/SainikithaSingireddy/document-qa-bot.git
cd document-qa-bot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Create Environment File

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

### 6. Ingest Documents

```bash
python src/ingest.py
```

### 7. Run Application

CLI Version:

```bash
python src/main.py
```

Streamlit Version:

```bash
streamlit run app.py
```

---

## RAG Workflow

```text
User Question
      │
      ▼
Generate Query Embedding
      │
      ▼
Search ChromaDB
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
Build Context Prompt
      │
      ▼
Gemini LLM
      │
      ▼
Grounded Answer
```

---

## Example Questions

- What is Artificial Intelligence?
- What is Machine Learning?
- What is Space Exploration?
- Explain Deep Learning.
- What information is available about Cyber Security?

---

## Sample Output

Question:

```text
What is Artificial Intelligence?
```

Answer:

```text
Artificial Intelligence is a computing concept that helps machines think and solve complex problems similarly to humans.

Source:
ai.pdf
```

---

## Future Improvements

- DOCX document support
- Page-level citations
- Improved chunking strategies
- Multi-document ranking
- Conversation memory
- Support for additional embedding models
- Support for local LLMs using Ollama

---

## Author

**Sainikitha Singireddy**

AI Engineering Internship Assignment – RAG Document Q&A Bot