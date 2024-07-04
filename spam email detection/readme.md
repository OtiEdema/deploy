# Email Spam Detection

This project is a simple email spam detection system that uses machine learning models to classify emails as spam or not spam (ham). It includes both a Naive Bayes model and an LSTM-based neural network model. The project also provides a Streamlit-based web interface for users to interact with the models and classify email messages.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model Details](#model-details)
- [Dataset](#dataset)
- [Contributing](#contributing)
- [License](#license)

## Installation

To set up the project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/email-spam-detection.git
    cd email-spam-detection
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv myenv
    source myenv/bin/activate    # On Windows, use `myenv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the Streamlit app:

1. Ensure you are in the project directory and the virtual environment is activated.

2. Run the Streamlit app:
    ```bash
    streamlit run spam_detection_app.py
    ```

3. Open your browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

4. Enter an email message and select the model (Naive Bayes or LSTM) to classify the message as spam or not spam.

## Project Structure

email-spam-detection/
├── dataset.csv # The dataset used for training the models
├── requirements.txt # The required packages for the project
├── spam_detection_app.py # The main Streamlit app script
└── README.md # This README file


## Model Details

### Naive Bayes Model
- Uses TF-IDF vectorization for feature extraction.
- Simple and effective for text classification tasks.

### LSTM Model
- Uses tokenization and padding for text preprocessing.
- More advanced model capable of capturing sequential patterns in text.

## Dataset

The dataset used in this project contains two columns: `Category` and `Message`. The `Category` column indicates whether the message is spam or ham, and the `Message` column contains the text of the email.

### Sample Data

| Category | Message                                  |
|----------|------------------------------------------|
| ham      | Go until jurong point, crazy.. Available only in bugis n great world la e buffet... Cine there got amore wat... |
| spam     | Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. Text FA to 87121 to receive entry question (std txt rate)T&C's apply 08452810075over18's |

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

