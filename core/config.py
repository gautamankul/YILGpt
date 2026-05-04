import os
from dotenv import load_dotenv

# This looks for a .env file and loads the variables into os.environ
load_dotenv() 

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# Safety check to ensure keys loaded correctly
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found. Check your .env file!")