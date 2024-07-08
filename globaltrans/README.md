# Oti AI LinguaStream

https://github.com/OtiEdema/deploy/assets/71005527/bd076c45-4905-42a4-8d85-4a46aaf71d2c

## Overview
Oti AI LinguaStream is a multi-functional language processing tool that allows users to translate, summarize, and extract entities from any text or URL content. The application uses a combination of natural language processing (NLP) techniques to deliver comprehensive language services.

## Features
- **Language Detection**: Automatically detects the language of the input text.
- **Translation**: Translates text from the detected language to a target language.
- **Summarization**: Provides a concise summary of the translated text.
- **Entity Extraction**: Extracts named entities from the translated text.
- **Text-to-Speech**: Reads the summary out loud using a text-to-speech engine.

## Installation
To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/OtiEdema/deploy/tree/cc79b3b008d4ae6e08855ceca55838eb065a8ebf/globaltrans
   
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Dependencies
- `streamlit`
- `transformers`
- `langdetect`
- `requests`
- `beautifulsoup4`
- `numpy`
- `pyttsx3`

You can install these dependencies using the following command:
```bash
pip install streamlit transformers langdetect requests beautifulsoup4 numpy pyttsx3

Usage
Input Options: Select input type (Text or URL) and enter the text or URL to process.
Target Language: Enter the target language code for translation (default is 'en' for English).
Extract Entities: Choose whether to extract entities from the text.
Text-to-Speech: Select whether to read the summary out loud (options for female or male voice).
Process: Click the 'Process' button to start the processing.
The application will display:

Detected language
Translated text
Summary of the text
Extracted entities (if selected)
Reads the summary out loud (if selected)
Logging
The application uses logging to record debug and error information. Logs are essential for troubleshooting and understanding the application's behavior.

Error Handling
The application includes error handling for various operations such as fetching URL content, language detection, translation, entity extraction, and summarization. Appropriate error messages are displayed to the user in case of any issues.

License
This project is licensed under the MIT License.

Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for any bugs or feature requests.

Acknowledgements
Streamlit
Hugging Face Transformers
LangDetect
Beautiful Soup
PyTTSX3
Contact
For any questions or suggestions, please contact on Linkedin.
