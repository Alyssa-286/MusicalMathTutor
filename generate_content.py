import openai
import os
from dotenv import load_dotenv

load_dotenv() # Load variables from .env file

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

client = openai.OpenAI(api_key=api_key)

def generate_math_lesson(concept):
    # ... function content (no changes needed here) ...