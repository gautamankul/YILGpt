from fastapi import FastAPI
from dotenv import load_dotenv
import os

# 1. LOAD FIRST
load_dotenv()

# 2. THEN ACCESS
key = os.getenv("OPENAI_API_KEY")
if key:
    print(f"API Key loaded: {key[:10]}...")
else:
    print("API Key NOT found. Check your .env file path!")

# 3. THEN IMPORT ROUTES (since routes might trigger the RAG service)
from api.routes import router

app = FastAPI(title="YIL GPT")
app.include_router(router)