from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def get_embedding(text):
    result = client.models.embed_content(
        model="models/gemini-embedding-2",
        contents=text
    )
    return result.embeddings[0].values