# Constellation categorisation with GPT-4

A Constellation categorisation tool using [ChatGPT completion API](https://platform.openai.com/docs/api-reference/chat/create).

## Installation

* Install virtualenv: `pip install virtualenv`
* Create a virtual environment: `virtualenv venv`
* Activate your environment: `source venv/bin/activate`
* Install the Python dependencies: `pip install -r requirements.txt`
* Create a `.envrc` file: `cp template.envrc .envrc`
* Fill in your API keys
* Allow the environment variables to be loaded `direnv allow`

## Create an OpenAI API Key

* Create an OpenAI API Key: https://platform.openai.com/account

## Running

* After activating your environment, run: `python categorise.py`
* Deactivate your virtual environment with: `deactivate`

# Options

* `CONSTELLATION_URL` - the URL of the Constellation API you'd like to categorise
* `DEBUG` - whether to show individual tokens per constellation link used

## Output

Here's an example of the output:

```bash
122214 - Arrkutja Tharra, Kungka Kutjara, Two Girls
OpenAPI Tokens: 642
gpt-4 categorisation: Video

68417 - Bluey
OpenAPI Tokens: 120
gpt-4 categorisation: TV show

100652 - Set design in Little J and Big Cuz
OpenAPI Tokens: 131
gpt-4 categorisation: TV show

62086 - The Secret Life of Us
OpenAPI Tokens: 111
gpt-4 categorisation: TV show

121855 - More Than Just a Game
OpenAPI Tokens: 320
gpt-4 categorisation: Videogame

122228 - Robbie Hood
OpenAPI Tokens: 197
gpt-4 categorisation: TV show

118042 - A Good Eye for Story
OpenAPI Tokens: 130
gpt-4 categorisation: Film

120000 - Ngura Pukulpa – Happy Place
OpenAPI Tokens: 158
gpt-4 categorisation: Artwork

Total tokens: 1809
```
