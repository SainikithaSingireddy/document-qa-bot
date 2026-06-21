# 📄 RAG Document Q&A Bot

## Live Demo

**Application:** https://document-app-bot-4gav9uf8bbxb4idkj4mapm.streamlit.app/

**GitHub Repository:** https://github.com/SainikithaSingireddy/document-qa-bot

---

## Overview

RAG Document Q&A Bot is a Retrieval-Augmented Generation (RAG) application that allows users to ask questions about documents stored in a knowledge base and receive context-aware answers generated using Google Gemini.

The system processes documents, creates vector embeddings, stores them in ChromaDB, retrieves relevant content for a user's query, and generates answers grounded in the retrieved context.

---

## Features

* Document ingestion and processing
* PDF document support
* Text chunking
* Semantic search using vector embeddings
* ChromaDB vector database
* Google Gemini integration
* Context-aware question answering
* Source attribution
* Streamlit web interface

---

## Tech Stack

* Python
* Streamlit
* Google Gemini API
* ChromaDB
* PyPDF
* python-dotenv
* tqdm

---

## Project Structure

```text
document-qa-bot/
│
├── app.py
├── data/
├── db/
├── requirements.txt
├── README.md
│
└── src/
    ├── __init__.py
    ├── embeddings.py
    ├── ingest.py
    ├── query.py
    ├── vector_store.py
```

---

## How It Works

### 1. Document Ingestion

Documents are loaded from the data folder and processed.

### 2. Text Chunking

Large documents are split into smaller chunks for efficient retrieval.

### 3. Embedding Generation

Gemini Embeddings convert text chunks into vector representations.

### 4. Vector Storage

Embeddings are stored in ChromaDB for semantic search.

### 5. Retrieval

When a user asks a question, the system retrieves the most relevant document chunks.

### 6. Answer Generation

Gemini generates an answer using only the retrieved context.

### 7. Source Attribution

The application displays the document sources used to generate the answer.

---

## Installation

### Clone Repository

```bash
git clone https://github.com/SainikithaSingireddy/document-qa-bot.git
cd document-qa-bot
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## Ingest Documents

Place documents inside the `data` folder and run:

```bash
python -m src.ingest
```

---

## Run the Application

```bash
streamlit run app.py
```

---

## Example Questions

* What is Artificial Intelligence?
* Summarize the documents.
* What topics are covered?
* Explain climate change.
* What information is available in the business plan?

---

## Future Improvements

* Support for DOCX and TXT files
* Upload documents through the UI
* Conversation history
* Advanced citation display
* Multi-document summarization

---

## Author

**Sainikitha Singireddy**

Developed as part of a technical assessment and learning project focused on Retrieval-Augmented Generation (RAG), Vector Databases, and Large Language Models.
