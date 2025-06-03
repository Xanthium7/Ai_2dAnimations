
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import sys

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def load_system_instruction():
    system_instruction_path = os.path.join(os.path.dirname(
        __file__), "..", "..", "prompts", "SystemInstruction.md")
    with open(system_instruction_path, "r", encoding="utf-8") as f:
        return f.read()


def load_user_filter_instruction():
    user_filter_instruction_path = os.path.join(os.path.dirname(
        __file__), "..", "..", "prompts", "userFilterPrompt.md")
    with open(user_filter_instruction_path, "r", encoding="utf-8") as f:
        return f.read()


system_instruction = load_system_instruction()
user_filter_prompt = load_user_filter_instruction()

user_prompt = '''
create me a 2d animation video explaning the roation of earth around the sun,
 explaning how it results in seasons.
'''


response = client.models.generate_content(
    model="gemini-2.5-flash-preview-05-20",
    config=types.GenerateContentConfig(
        system_instruction=user_filter_prompt),
    contents=user_prompt,
)

filtered_prompt = response.text
print(filtered_prompt)


response = client.models.generate_content(
    model="gemini-2.5-flash-preview-05-20",
    config=types.GenerateContentConfig(
        system_instruction=system_instruction),
    contents=user_prompt,
)

print(response.text)
with open("response.txt", "w", encoding="utf-8") as f:
    f.write(response.text)
