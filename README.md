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
Constellation categorisation based on its name and description: Film

50 - Camera obscura
gpt-4 categorisation: Artwork

51 - Filmanfang „Lisbon Story“ (Wim Wenders)
gpt-4 categorisation: Film

52 - Filmanfang „Sieben Frauen“ (Rudolf Thome)
gpt-4 categorisation: Film

53 - “Der plötzliche Reichtum der armen Leute von Kombach” (Volker Schlöndorff) – Collage: "Sequenz 9" mit Auszügen aus dem Arbeitsdrehbuch
gpt-4 categorisation: Film

54 - Wassersport / Kopfsprünge (mit Günther Leitz am Rollenende)
gpt-4 categorisation: Film

55 - Visit with Uncle Jacob Rosenberg in Frankfurt (and Rhine/Wiesbaden)
gpt-4 categorisation: Film

56 - "Schumann-Theater" Postkarte
gpt-4 categorisation: Image

Most common categories: {'Film': 5, 'Artwork': 1, 'Image': 1}

Total tokens: 2923
```
