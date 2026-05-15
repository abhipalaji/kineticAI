import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

URL = "https://openrouter.ai/api/v1/chat/completions"


def generate_ai_response(system_prompt, user_prompt):

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "openai/gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        "temperature": 0.7
    }

    try:

        response = requests.post(
            URL,
            headers=headers,
            json=payload
        )

        data = response.json()

        print(data)

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        print("API ERROR:", e)
        return "Error reaching the Origin engine."


# OLD SUPPORT
call_ai = generate_ai_response