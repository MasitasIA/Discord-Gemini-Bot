import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)

def gemini_query(query: str):
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"Trata de responder en menos de 1800 caracteres a este texto: {query}",
    )
    return response.text