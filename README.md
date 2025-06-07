# TranslateAWordTo

Simple CLI Python script to translate a single word into a target language using offline support. Designed for fast, basic translations via the `translate` Python module.

## Features

- Lightweight and easy to use  
- Translates one word at a time  
- Offline translation support (no API key needed)  
- Great for command-line learners and simple automation

## How It Works

This script takes a word and returns the translated word using the `translate` module.

Example:

-`$ python3 translateAWord.py`

-`Enter a word to translate: hello`

-`Enter the language to translate to: es`

-`Translated: hola`

## Installation

Clone the repo:
`git clone https://github.com/MurphyAmos/TranslateAWordTo.git`

Navigate to repo:
`cd TranslateAWordTo`


Install dependencies (make sure you have Python 3 installed):
`pip install translate`

## Usage

Run the script:
python3 translateAWord.py

When prompted:
- Enter the word you want to translate  
- Enter the language (like `Spanish`, `French`,`Hindi` etc.)

## Language Codes

Use ISO 639-1 codes. Here are a few examples:

| Language | Code |
|----------|------|
| Spanish  | `es` |
| French   | `fr` |
| German   | `de` |
| Japanese | `ja` |
| Italian  | `it` |

## Note

- Only supports single-word input  
- Requires internet connection for certain language models, depending on your installed `translate` backend

## License

[MIT](https://choosealicense.com/licenses/mit/)
