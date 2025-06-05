from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import sys
import re

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


def extract_python_code_blocks(text):
    """Extract content between ```python and ``` markers"""
    pattern = r'```python\s*\n(.*?)\n```'
    matches = re.findall(pattern, text, re.DOTALL)
    return '\n\n'.join(matches) if matches else text


system_instruction = load_system_instruction()
user_filter_prompt = load_user_filter_instruction()

user_prompt = '''
create me animation video explaning the creation and fucntioning of neural networks.

'''


print("Generating filtered prompt...")
response = client.models.generate_content(
    model="gemini-2.5-flash-preview-05-20",
    config=types.GenerateContentConfig(
        system_instruction=user_filter_prompt),
    contents=user_prompt,
)

filtered_prompt = response.text
print(filtered_prompt)


print("Generating response...")
print("__" * 50)
response = client.models.generate_content(
    model="gemini-2.5-flash-preview-05-20",
    config=types.GenerateContentConfig(
        system_instruction=system_instruction),
    contents=user_prompt,
)

print(response.text)
extracted_code = extract_python_code_blocks(response.text)

with open("response.txt", "w", encoding="utf-8") as f:
    f.write(extracted_code)
