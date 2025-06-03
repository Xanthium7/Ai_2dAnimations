
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


system_instruction = load_system_instruction()


user_prompt = '''
Create an educational Manim animation to explain the set operations: union, intersection, and difference (A − B). Use two overlapping circles to represent sets A and B. The animation should be structured into three distinct scenes, each dedicated to one operation, with smooth transitions, labels, and clear visual emphasis. The purpose is to make the concept intuitive and visually engaging for learners.

---

# Scene Breakdown

Scene 1: Union (A ∪ B)
- Display two labeled, overlapping circles: A (left) and B (right).
- Animate the highlighting of both circles together, including the overlapping region.
- Use color blending or outlining to show that all elements from both sets are included.
- Add a label: “A ∪ B: All elements in A or B or both.”

Scene 2: Intersection (A ∩ B)
- Start with the same two overlapping circles.
- Dim the non-overlapping areas.
- Animate and highlight only the overlapping region between A and B.
- Add a label: “A ∩ B: Elements common to both A and B.”

Scene 3: Difference (A − B)
- Start again with circles A and B.
- Dim or fade out circle B.
- Highlight the part of circle A that does not overlap with B.
- Add a label: “A − B: Elements in A but not in B.”

---

# Additional Notes
- Use `Text` or `MathTex` for labels and symbols.
- Transitions between scenes should be smooth (e.g., Transform, Fade, ReplacementTransform).
- Use color cues (e.g., blue for A, red for B, purple for intersection) to aid understanding.

---

Optional: Let me know if you want to include set elements (like small dots or numbers inside the circles), a fourth scene for symmetric difference (A Δ B), or voiceover text.

'''


# print(system_instruction)

response = client.models.generate_content(
    model="gemini-2.5-flash-preview-05-20",
    config=types.GenerateContentConfig(
        system_instruction=system_instruction),
    contents=user_prompt,
)

print(response.text)
with open("response.txt", "w", encoding="utf-8") as f:
    f.write(response.text)
