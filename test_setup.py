import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("ERROR: OPENAI_API_KEY not found.")
    print("Steps to fix:")
    print("  1. Copy .env.example to .env")
    print("  2. Add your OpenAI API key to .env")
else:
    masked = api_key[:7] + "..." + api_key[-4:]
    print(f"API key found: {masked}")
    print("Setup looks good. Run: streamlit run app.py")
