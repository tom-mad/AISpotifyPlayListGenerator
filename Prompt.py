import os
import openai
from dotenv import load_dotenv

example_json = """
[
    {"song": "Someone Like You", "artist": "Adele"},
    {"song": "Hurt", "artist": "Johnny Cash"},
    {"song": "Skinny Love", "artist": "Bon Iver"},
    {"song": "Yesterday", "artist": "The Beatles"},
    {"song": "I Will Always Love You", "artist": "Whitney Houston"},
    {"song": "Nothing Compares 2 U", "artist": "Sinéad O'Connor"}
]
"""

messages = [
    {"role": "system", "content": """You are a helpful playlist generating assistant.
     You should generate a list of song and their artists according to a text prompt.
     You should return a JSON array, where each element follows this format: {"song": <song_title>, "artist: <artist_name>"}"""
     },
    {"role": "user", "content": "Generate a playlist of songs based on this prompt: super super sad songs"},
    {"role": "assistant", "content": example_json},
    {"role": "user", "content": "Generate a playlist of songs based on this prompt: high energy exciting dance songs"},
]

def main(client, model="gpt-3.5-turbo"):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=400
    )

    print(response.choices[0].message.content)

if __name__ == "__main__":
    load_dotenv()

    client = openai.OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
    )

    main(client)
