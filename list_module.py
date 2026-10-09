import os
from google import genai

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
raise ValueError("GOOGLE_API_KEY is not set. Check your .env configuration.")

client = genai.Client(api_key=api_key)

for model in client.models.list():
print(model.name)
