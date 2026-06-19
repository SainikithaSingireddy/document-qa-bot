import chromadb

client = chromadb.PersistentClient(path="/tmp/chroma_db")

collection = client.get_or_create_collection(name="rag_docs")