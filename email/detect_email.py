import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer
import re
import string

# Load Dataset
data = pd.read_csv('dataset.csv')  # Load the dataset from a CSV file. Assume the CSV has columns 'label' and 'email'.

# Function to clean text data
def clean_text(text):
    text = text.lower()  # Convert text to lowercase.
    text = re.sub(r'\d+', '', text)  # Remove digits.
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation.
    text = text.strip()  # Remove leading and trailing whitespace.
    return text

# Apply text cleaning function to the dataset
data['clean_email'] = data['email'].apply(clean_text)  # Apply the clean_text function to each email.

# Feature Extraction using TF-IDF Vectorization
tfidf = TfidfVectorizer(stop_words='english', max_df=0.7)  # Initialize TF-IDF Vectorizer with English stop words and a max document frequency of 70%.
X = tfidf.fit_transform(data['clean_email'])  # Fit and transform the cleaned email text to TF-IDF features.
y = data['label']  # Extract the labels.

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  # Split the data: 80% for training and 20% for testing.

# Initialize and train the Naive Bayes model
model = MultinomialNB()  # Initialize the Multinomial Naive Bayes model.
model.fit(X_train, y_train)  # Train the model on the training data.

# Predict and evaluate the model on the test data
y_pred = model.predict(X_test)  # Predict the labels for the test data.
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')  # Print the accuracy of the model.
print(confusion_matrix(y_test, y_pred))  # Print the confusion matrix.
print(classification_report(y_test, y_pred))  # Print the classification report.

# Hyperparameter Tuning using GridSearchCV
from sklearn.model_selection import GridSearchCV

parameters = {
    'alpha': [0.01, 0.1, 1]  # Define the grid of hyperparameters to search (alpha values for Naive Bayes).
}

grid_search = GridSearchCV(MultinomialNB(), parameters, cv=5, scoring='accuracy')  # Initialize GridSearchCV with 5-fold cross-validation.
grid_search.fit(X_train, y_train)  # Fit GridSearchCV on the training data.

best_model = grid_search.best_estimator_  # Get the best model from GridSearchCV.
y_pred = best_model.predict(X_test)  # Predict the labels for the test data using the best model.

print(f'Best Parameters: {grid_search.best_params_}')  # Print the best hyperparameters found.
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')  # Print the accuracy of the best model.
print(confusion_matrix(y_test, y_pred))  # Print the confusion matrix for the best model.
print(classification_report(y_test, y_pred))  # Print the classification report for the best model.

# Deep Learning Approach using LSTM

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, SpatialDropout1D
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Parameters for tokenization and padding
max_features = 5000  # Maximum number of words to keep, based on word frequency.
embed_dim = 128  # Dimension of the dense embedding.
lstm_out = 196  # Output dimension of LSTM layer.
max_length = 100  # Maximum length of sequences (number of tokens).

# Tokenization
tokenizer = Tokenizer(num_words=max_features, split=' ')  # Initialize the tokenizer.
tokenizer.fit_on_texts(data['clean_email'].values)  # Fit the tokenizer on the cleaned email text.
X = tokenizer.texts_to_sequences(data['clean_email'].values)  # Convert text to sequences of integers.
X = pad_sequences(X, maxlen=max_length)  # Pad sequences to ensure they have the same length.

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  # Split the data: 80% for training and 20% for testing.

# LSTM Model
model = Sequential()  # Initialize the Sequential model.
model.add(Embedding(max_features, embed_dim, input_length=max_length))  # Add an embedding layer.
model.add(SpatialDropout1D(0.4))  # Add a spatial dropout layer to prevent overfitting.
model.add(LSTM(lstm_out, dropout=0.2, recurrent_dropout=0.2))  # Add an LSTM layer with dropout.
model.add(Dense(2, activation='softmax'))  # Add a dense layer with softmax activation for binary classification.

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])  # Compile the model with sparse categorical cross-entropy loss and Adam optimizer.

# Train the model
model.fit(X_train, y_train, epochs=5, batch_size=32, verbose=2)  # Train the model on the training data for 5 epochs.

# Evaluate the model
y_pred = model.predict(X_test)  # Predict the labels for the test data.
y_pred_classes = np.argmax(y_pred, axis=1)  # Convert predicted probabilities to class labels.

print(f'Accuracy: {accuracy_score(y_test, y_pred_classes)}')  # Print the accuracy of the LSTM model.
print(confusion_matrix(y_test, y_pred_classes))  # Print the confusion matrix for the LSTM model.
print(classification_report(y_test, y_pred_classes))  # Print the classification report for the LSTM model.
