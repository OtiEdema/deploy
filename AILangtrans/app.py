from flask import Flask, render_template, request, jsonify
from langdetect import detect
from transformers import MarianMTModel, MarianTokenizer, pipeline
import logging
import requests
from bs4 import BeautifulSoup
import numpy as np

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

def fetch_url_content(url):
    logging.debug("Fetching content for URL: %s", url)
    try:
        response = requests.get(url)
        response.raise_for_status()
        # Use BeautifulSoup to extract text content
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        logging.debug("Fetched content length: %d", len(text))
        if len(text) < 100:  # Arbitrary threshold for minimal content length
            raise ValueError("Fetched content is too short to process")
        return text
    except Exception as e:
        logging.exception("Error fetching URL content")
        raise

def detect_language(text):
    logging.debug("Detecting language for text of length: %d", len(text))
    try:
        detected_lang = detect(text)
        logging.debug("Detected language: %s", detected_lang)
        return detected_lang
    except Exception as e:
        logging.exception("Error detecting language")
        raise

def translate_text(text, src_lang, tgt_lang):
    logging.debug("Translating text from %s to %s", src_lang, tgt_lang)
    try:
        model_name = f'Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}'
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model = MarianMTModel.from_pretrained(model_name)
        inputs = tokenizer(text, return_tensors="pt", padding=True)
        translated = model.generate(**inputs)
        translated_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated][0]
        logging.debug("Translated text length: %d", len(translated_text))
        return translated_text
    except Exception as e:
        logging.exception("Error translating text")
        raise

def extract_entities(text):
    logging.debug("Extracting entities from text of length: %d", len(text))
    try:
        nlp = pipeline("ner")
        entities = nlp(text)
        logging.debug("Extracted entities: %s", entities)
        return entities
    except Exception as e:
        logging.exception("Error extracting entities")
        raise

def generate_summary(text):
    logging.debug("Generating summary for text of length: %d", len(text))
    try:
        summarizer = pipeline("summarization")
        summary = summarizer(text, max_length=100, min_length=50, do_sample=False)[0]['summary_text']
        logging.debug("Generated summary length: %d", len(summary))
        return summary
    except Exception as e:
        logging.exception("Error generating summary")
        raise

def make_serializable(obj):
    if isinstance(obj, dict):
        return {key: make_serializable(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [make_serializable(item) for item in obj]
    elif isinstance(obj, np.float32):
        return float(obj)
    elif isinstance(obj, np.int64):
        return int(obj)
    elif isinstance(obj, float):
        return float(obj)
    elif isinstance(obj, int):
        return int(obj)
    else:
        return obj

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    try:
        data = request.json
        user_input = data.get('user_input')
        preferred_lang = data.get('preferred_lang')

        logging.debug("User Input: %s", user_input)
        logging.debug("Preferred Language: %s", preferred_lang)

        # Check if the user input is a URL
        if user_input.startswith("http://") or user_input.startswith("https://"):
            user_input = fetch_url_content(user_input)

        if not user_input or len(user_input) < 100:
            raise ValueError("Input text is too short for processing")

        lang = detect_language(user_input)
        logging.debug("Detected Language: %s", lang)

        translated_text = translate_text(user_input, lang, preferred_lang)
        logging.debug("Translated Text: %s", translated_text[:200])  # Log first 200 characters

        entities = extract_entities(translated_text)
        logging.debug("Extracted Entities: %s", entities)

        summary = generate_summary(translated_text)
        logging.debug("Summary: %s", summary)

        response = {
            'lang': lang,
            'translated_text': translated_text,
            'entities': make_serializable(entities),
            'summary': summary
        }

        logging.debug("Response: %s", response)
        return jsonify(response)
    except Exception as e:
        logging.exception("Error processing request")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
