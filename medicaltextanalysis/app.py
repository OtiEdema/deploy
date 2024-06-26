
from flask import Flask, request, render_template
import nltk
from gensim.models import Word2Vec
from nltk.corpus import stopwords
import re
import scispacy
import spacy
from scispacy.abbreviation import AbbreviationDetector
from scispacy.umls_linking import UmlsEntityLinker

app = Flask(__name__)

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
nlp = spacy.load('en_ner_bc5cdr_md')
nlp.add_pipe("abbreviation_detector")
linker = UmlsEntityLinker(resolve_abbreviations=True, name="umls")

# Function to preprocess text
def preprocess_text(text):
    text = re.sub(r'\[[0-9]*\]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.lower()
    text = re.sub(r'\d', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text

# Function to tokenize and remove stopwords
def tokenize_and_clean(text):
    sentences = nltk.sent_tokenize(text)
    sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    for i in range(len(sentences)):
        sentences[i] = [word for word in sentences[i] if word not in stop_words]
    return sentences

# Function to extract medical entities
def extract_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for processing text
@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':
        paragraph = request.form['paragraph']
        word = request.form['word']
        
        # Preprocess and tokenize
        text = preprocess_text(paragraph)
        sentences = tokenize_and_clean(text)
        
        # Train Word2Vec model
        model = Word2Vec(sentences, min_count=1)
        
        # Extract entities
        entities = extract_entities(paragraph)
        
        # Find most similar words
        if word in model.wv:
            similar_words = model.wv.most_similar(word)
        else:
            similar_words = "Word not in vocabulary."
        
        return render_template('index.html', word=word, similar_words=similar_words, entities=entities, paragraph=paragraph)

if __name__ == '__main__':
    app.run(debug=True)
