import os
import json
import openai
from dotenv import load_dotenv


class AIPlaylistGenerator:

    def __init__(self, model="gpt-3.5-turbo") -> None:
        load_dotenv()

        self.client = openai.OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
        )

        self.model = model

        self.example_json = """
        [
            {"song": "Someone Like You", "artist": "Adele"},
            {"song": "Hurt", "artist": "Johnny Cash"},
            {"song": "Skinny Love", "artist": "Bon Iver"},
            {"song": "Yesterday", "artist": "The Beatles"},
            {"song": "I Will Always Love You", "artist": "Whitney Houston"},
            {"song": "Nothing Compares 2 U", "artist": "Sinéad O'Connor"}
        ]
        """

    def get_message_to_openai(self, prompt, count) -> list:
        return [
            {"role": "system", "content": """You are a helpful playlist generating assistant.
            You should generate a list of song and their artists according to a text prompt.
            You should return a JSON array, where each element follows this format: {"song": <song_title>, "artist: <artist_name>"}"""
            },
            {"role": "user", "content": "Generate a playlist of 5 songs based on this prompt: super super sad songs"},
            {"role": "assistant", "content": self.example_json},
            {"role": "user", "content": f"Generate a playlist of {count} songs based on this prompt: {prompt}"},
        ]

    def generate_playlist(self, prompt, count=10) -> json:
        messages = self.get_message_to_openai(prompt, count)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            max_tokens=400
        )

        return json.loads(response.choices[0].message.content)


if __name__ == "__main__":
    generator = AIPlaylistGenerator()
    print(generator.generate_playlist("instrumental hurdy gurdy music"))
