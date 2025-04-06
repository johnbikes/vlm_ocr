# Applying a "small" VLM to some documents
- A family member sent me several handwritten documents that I wanted to transcribe

## Configure env
- `cp .env.sample .env` and update
- using uv the wrong way for now ...
- `uv venv <LOCATION WITH SPACE ...> --python 3.11`
- `source <LOCATION WITH SPACE ...>/bin/activate`
- `uv pip install -r requirements.txt`

## Run
- `python main.py`

## Basic convert
- set **PDF_DIR** in .env to the location of your pdfs (not recursive at the moment)
- `python convert.py`