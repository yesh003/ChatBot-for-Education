import os
import google.generativeai as genai
from dotenv import load_dotenv

# ✅ Load environment variables from .env file
load_dotenv()
api_key = os.getenv("AIzaSyC4XgT1kHag2bNEAKi1ghNPDI035uU18RU")

# ✅ Ensure API key is not empty
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file or environment variables.")

# ✅ Configure Gemini (GAT) API
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")

def get_response(user_query):
    try:
        # Use structured format for consistent parsing
        response = model.generate_content(
            contents=[{"role": "user", "parts": [{"text": user_query}]}]
        )
        return response.candidates[0].content.parts[0].text.strip()
    except Exception as e:
        return f"[Error] {str(e)}"

def handle_user_query(user_query):
    return get_response(user_query)
