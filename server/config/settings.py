import os
from pathlib import Path
from dotenv import load_dotenv


# Project root directory
BASE_DIR = Path(__file__).resolve().parents[2]

# Load .env from project root
load_dotenv(BASE_DIR / ".env")


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

TEMPFILE_UPLOAD_DIRECTORY = str(BASE_DIR / "temp" / "uploaded_files")

MODEL_OPTIONS = {
  "groq": {
    "playground": "https://console.groq.com",
    "models": ["openai/gpt-oss-20b"]
  },
  "gemini": {
    "playground": "https://ai.google.dev",
    "models": ["gemini-2.0-flash", "gemini-2.5-flash"]
  }
}

VECTORSTORE_DIRECTORY = {
  key.lower(): str(BASE_DIR / "data" / f"{key.lower()}_vector_store")
  for key in MODEL_OPTIONS.keys()
}