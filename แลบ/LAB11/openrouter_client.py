import json
import os

import requests
from dotenv import load_dotenv


load_dotenv()

OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"


def call_openrouter(message: str) -> dict:
    """
    Send a message to OpenRouter and return the assistant response.
    """

    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENROUTER_API_KEY is not set. "
            "Please add it to your .env file."
        )

    response = requests.post(
        url=OPENROUTER_API_URL,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "model": "openrouter/free",
            "messages": [
                {
                    "role": "user",
                    "content": message
                }
            ],
            "reasoning": {
                "enabled": True
            }
        }),
        timeout=60
    )

    # Raise an error if the API request failed
    response.raise_for_status()

    data = response.json()

    return data["choices"][0]["message"]



def call_openrouter4web(messages: list[dict]) -> str:
    """
    Send conversation history to OpenRouter.

    messages example:
    [
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hi!"},
        {"role": "user", "content": "What is your name?"}
    ]
    """

    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENROUTER_API_KEY is not set. "
            "Please add it to your .env file."
        )

    response = requests.post(
        url=OPENROUTER_API_URL,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "model": "openrouter/free",
            "messages": messages,
            "reasoning": {
                "enabled": True
            }
        }),
        timeout=120
    )

    response.raise_for_status()

    data = response.json()

    assistant_message = data["choices"][0]["message"]

    return assistant_message.get("content", "")

