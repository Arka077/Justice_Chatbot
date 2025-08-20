import requests
import os
from dotenv import load_dotenv

load_dotenv()
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"

def call_mistral(prompt, api_key=MISTRAL_API_KEY, temperature=0.7, max_tokens=512):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mistral-medium",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    response = requests.post(MISTRAL_API_URL, headers=headers, json=payload)
    return response.json()["choices"][0]["message"]["content"]
