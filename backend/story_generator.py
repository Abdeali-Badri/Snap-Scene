from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def generate_story(user_prompt: str) -> str:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You write very simple stories for short animated videos."
            },
            {
                "role": "user",
                "content": (
                    "Write a simple animated story in 3 to 4 short lines. "
                    "Keep language minimal and visual.\n\n"
                    f"Story idea: {user_prompt}"
                )
            }
        ],
        max_tokens=90
    )

    return response.choices[0].message.content
