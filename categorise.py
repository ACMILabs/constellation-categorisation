"""A ChatGPT constellation categorisation tool."""
import os
import openai
import requests


CONSTELLATION_URL = 'https://xos.acmi.net.au/api/constellations/384/'
CHATGPT_MODEL = 'gpt-4'  # 'gpt-3.5-turbo'
DEBUG = False
CATEGORIES = [
    'Film',
    'TV show',
    'Videogame',
    'Object',
    'Image',
    'Music video',
    'Video',
    'Website',
    'Artwork',
    'Mixed reality',
]


class OpenAI:
    """An OpenAI client to categorise constellations."""

    def __init__(self):
        self.model = CHATGPT_MODEL
        self.openai_client = openai
        self.openai_client.api_key = os.getenv('OPENAI_API_KEY')

    def categorise(self, text):
        """Retrieve a response from ChatGPT from our input text."""
        system_prompt = {
            'role': 'system',
            'content': 'You are a museum collection staff member. Your role is to '\
                       'categorise the following description of an object into the '\
                       f'categories: {", ".join(CATEGORIES)}. '\
                       'Reply only with the category you choose.',
        }
        object_prompt = {
            'role': 'user',
            'content': text,
        }
        response = self.openai_client.ChatCompletion.create(
            model=self.model,
            messages=[
                system_prompt,
                object_prompt,
            ],
        )
        if DEBUG:
            print(f'OpenAPI Tokens: {response.usage.total_tokens}')
        content = response.choices[0].message.content
        return (content, response.usage.total_tokens)


def main():
    """Get Constellation data from the ACMI/DFF API, and categorise the links."""

    total_tokens = 0
    constellation_data = requests.get(CONSTELLATION_URL).json()

    openai_client = OpenAI()
    unique_work_ids = set()

    for link in constellation_data['links']:
        for work in [link["start"], link["end"]]:
            if work["id"] not in unique_work_ids:
                work_description = f'{work["title"]}\n{work["brief_description"]}'
                print(f'{work["id"]} - {work["title"]}')
                response, tokens = openai_client.categorise(work_description)
                total_tokens += tokens
                print(f'{CHATGPT_MODEL} categorisation: {response}\n')
                unique_work_ids.add(work["id"])


    print(f'Total tokens: {total_tokens}')


if __name__ == '__main__':
    main()
