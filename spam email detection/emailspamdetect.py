import streamlit as st
import pandas as pd
import numpy as np
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, SpatialDropout1D
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load Dataset
data = pd.read_csv(r'C:\projects\email\archive (6)\dataset.csv')

# Function to clean text data
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.strip()
    return text

# Apply text cleaning function to the dataset
data['clean_message'] = data['Message'].apply(clean_text)

# Encode labels as integers
label_encoder = LabelEncoder()
data['encoded_category'] = label_encoder.fit_transform(data['Category'])

# Verify the encoding
label_mapping = dict(zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_)))
print("Label mapping:", label_mapping)

# Feature Extraction using TF-IDF Vectorization for Naive Bayes
tfidf = TfidfVectorizer(stop_words='english', max_df=0.7)
X_tfidf = tfidf.fit_transform(data['clean_message'])
y = data['encoded_category']

# Train the Naive Bayes model
model_nb = MultinomialNB()
model_nb.fit(X_tfidf, y)

# Parameters for tokenization and padding for LSTM
max_features = 5000
embed_dim = 128
lstm_out = 196
max_length = 100

# Tokenization for LSTM
tokenizer = Tokenizer(num_words=max_features, split=' ')
tokenizer.fit_on_texts(data['clean_message'].values)
X_tokenized = tokenizer.texts_to_sequences(data['clean_message'].values)
X_padded = pad_sequences(X_tokenized, maxlen=max_length)

# Split the data into training and testing sets for LSTM
X_train, X_test, y_train, y_test = train_test_split(X_padded, y, test_size=0.2, random_state=42)

# Train the LSTM model
model_lstm = Sequential()
model_lstm.add(Embedding(max_features, embed_dim, input_length=max_length))
model_lstm.add(SpatialDropout1D(0.4))
model_lstm.add(LSTM(lstm_out, dropout=0.2, recurrent_dropout=0.2))
model_lstm.add(Dense(2, activation='softmax'))

model_lstm.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model_lstm.fit(X_train, y_train, epochs=5, batch_size=32, verbose=2, validation_split=0.2)

# Streamlit App
st.title('Email Spam Detection')

# Input text
input_text = st.text_area('Enter the email message to classify:')

# Model selection
model_choice = st.selectbox('Choose the model for classification:', ['Naive Bayes', 'LSTM'])

# Preprocess the input text
cleaned_text = clean_text(input_text)

if model_choice == 'Naive Bayes':
    # TF-IDF transformation
    input_tfidf = tfidf.transform([cleaned_text])
    # Predict with Naive Bayes
    prediction = model_nb.predict(input_tfidf)
    prediction_label = label_encoder.inverse_transform(prediction)[0]
else:
    # Tokenize and pad the input text for LSTM
    input_sequence = tokenizer.texts_to_sequences([cleaned_text])
    input_padded = pad_sequences(input_sequence, maxlen=max_length)
    # Predict with LSTM
    prediction = model_lstm.predict(input_padded)
    prediction_class = np.argmax(prediction, axis=1)
    prediction_label = label_encoder.inverse_transform(prediction_class)[0]

# Display the result
if st.button('Classify'):
    if prediction_label == 'spam':
        st.write('The message is classified as: **Spam**')
    else:
        st.write('The message is classified as: **Ham**')
