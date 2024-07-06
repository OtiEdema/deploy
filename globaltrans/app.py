import streamlit as st
from transformers import MarianMTModel, MarianTokenizer, pipeline
from langdetect import detect
import logging
import requests
from bs4 import BeautifulSoup
import numpy as np
import pyttsx3

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Streamlit app configuration
st.set_page_config(page_title="Oti AI LinguaStream", page_icon="🌐", layout="wide")

# Display header image
st.image("header_image.jpg", use_column_width=True)

st.title("Oti AI LinguaStream")
st.write("Translate, summarize, and extract entities from any text or URL content.")

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to fetch URL content
def fetch_url_content(url):
    logging.debug("Fetching content for URL: %s", url)
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        logging.debug("Fetched content length: %d", len(text))
        if len(text) < 100:
            raise ValueError("Fetched content is too short to process")
        return text
    except Exception as e:
        logging.exception("Error fetching URL content")
        raise

# Function to detect language
def detect_language(text):
    logging.debug("Detecting language for text of length: %d", len(text))
    try:
        detected_lang = detect(text)
        logging.debug("Detected language: %s", detected_lang)
        return detected_lang
    except Exception as e:
        logging.exception("Error detecting language")
        raise

# Function to translate text
def translate_text(text, src_lang, tgt_lang):
    if not tgt_lang:
        raise ValueError("Target language code cannot be empty.")
    
    logging.debug("Translating text from %s to %s", src_lang, tgt_lang)
    try:
        model_name = f'Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}'
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model = MarianMTModel.from_pretrained(model_name)
        inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
        translated = model.generate(**inputs)
        translated_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated][0]
        logging.debug("Translated text length: %d", len(translated_text))
        return translated_text
    except Exception as e:
        logging.exception("Error translating text")
        raise

# Function to extract entities
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

# Function to generate summary
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

# Function to make objects serializable
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

# Streamlit sidebar options
st.sidebar.header("Input Options")
input_type = st.sidebar.selectbox("Select input type", ["Text", "URL"])
language = st.sidebar.text_input("Enter target language code (default is 'en')", value="en")
extract_entities_option = st.sidebar.checkbox("Extract Entities", value=True)
voice_output = st.sidebar.selectbox("Read summary out loud?", ["No", "Yes, Female Voice", "Yes, Male Voice"])

if st.sidebar.button("Reset"):
    st.experimental_rerun()

# Input area based on input type
if input_type == "Text":
    user_input = st.text_area("Enter text to process")
else:
    user_input = st.text_input("Enter URL to process")

# Processing on button click
if st.button("Process"):
    with st.spinner("Processing..."):
        try:
            if input_type == "URL":
                user_input = fetch_url_content(user_input)
            
            if not user_input or len(user_input) < 100:
                st.error("Input text is too short for processing")
            else:
                detected_lang = detect_language(user_input)
                translated_text = translate_text(user_input, detected_lang, language)
                entities = extract_entities(translated_text) if extract_entities_option else []
                summary = generate_summary(translated_text)
                
                st.subheader("Detected Language")
                st.write(detected_lang)
                st.subheader("Translated Text")
                st.write(translated_text)
                st.subheader("Summary")
                st.write(summary)
                if extract_entities_option:
                    st.subheader("Extracted Entities")
                    st.json(make_serializable(entities))
                
                if voice_output != "No":
                    voices = engine.getProperty('voices')
                    engine.setProperty('voice', voices[0].id if voice_output == "Yes, Male Voice" else voices[1].id)
                    engine.say(summary)
                    engine.runAndWait()
        
        except Exception as e:
            st.error(f"Error processing request: {e}")
            logging.exception("Error processing request")
