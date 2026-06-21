# 📄 RAG Document Q&A Bot

A Retrieval-Augmented Generation (RAG) application that allows users to ask questions about uploaded documents and receive context-aware answers generated using Google Gemini.

## 🚀 Features

- Document ingestion and processing
- PDF document support
- Text chunking
- Vector embeddings using Gemini Embeddings
- ChromaDB vector storage
- Semantic document retrieval
- AI-powered answers using Gemini
- Source attribution for retrieved content
- Streamlit web interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- ChromaDB
- PyPDF
- python-dotenv

---

## 📂 Project Structure

```text
document-qa-bot/
│
├── app.py
├── data/
├── db/
├── src/
│   ├── __init__.py
│   ├── embeddings.py
│   ├── ingest.py
│   ├── query.py
│   ├── vector_store.py
│
├── requirements.txt
├── README.md
└── .env
```

---

## ⚙️ Setup

### Clone Repository

```bash
git clone <repository-url>
cd document-qa-bot
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## 📥 Ingest Documents

Place documents inside the `data` folder.

Run:

```bash
python -m src.ingest
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 💬 Example Questions

- What is Artificial Intelligence?
- Summarize the documents.
- What topics are covered?
- Explain climate change.

---

## 📌 How It Works

1. Documents are loaded and processed.
2. Text is split into chunks.
3. Gemini Embeddings generate vector representations.
4. ChromaDB stores document vectors.
5. User questions are embedded.
6. Relevant chunks are retrieved.
7. Gemini generates answers using retrieved context.
8. Sources are displayed to the user.

---

## 📜 License

This project was developed as part of a technical assessment and learning project.