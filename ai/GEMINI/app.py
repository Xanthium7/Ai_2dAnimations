from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
from prompts.SystemInstruction import system_instruction

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash-preview-05-20",
    config=types.GenerateContentConfig(
        system_instruction=system_instruction),
    contents="Explain how AI works in a few words",
)


print(response.text)
with open("response.txt", "w", encoding="utf-8") as f:
    f.write(response.text)
