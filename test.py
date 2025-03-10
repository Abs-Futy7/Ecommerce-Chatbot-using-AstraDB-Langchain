import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing! Check your .env file.")

print(f"API Key Loaded: {GEMINI_API_KEY[:5]}...")  # Prints the first 5 characters to confirm it loads.
