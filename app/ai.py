import openai
import os
from dotenv import load_dotenv
from pyexpat.errors import messages

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")  # Her skriver du navnet på miljøvariablen

def run_ai(prompt: str) -> str:
    response = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": prompt}])
    return response.choices[0].message.content.strip()
