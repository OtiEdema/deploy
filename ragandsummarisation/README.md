# AI-Powered Report Analysis

This project is a Streamlit application that allows users to upload documents in various formats (TXT, PDF, DOCX) and perform AI-powered analysis. The app provides functionalities for summarizing documents and answering questions based on the content of the documents.

## Features

- **Document Upload**: Upload text, PDF, or DOCX files.
- **Document Summarization**: Generate summaries of uploaded documents based on a user-defined summarization percentage.
- **Question Answering**: Ask questions related to the content of the uploaded document and receive AI-generated answers.

## Installation

To run this application locally, you need to have Python installed. Follow the steps below:

1. **Clone the repository**:

   ```bash
   git clone 
   cd deploy

Install the required packages:

You can install the dependencies using pip:

pip install -r requirements.txt

Ensure that the following packages are included in requirements.txt:

streamlit
PyPDF2
python-docx
langchain_huggingface
langchain_community
transformers
Run the Streamlit app:

streamlit run app.py

Usage
Upload a Document: Once the app is running, upload a document in TXT, PDF, or DOCX format.

Choose Functionality:

Summarization: Select the "Summarization" tab, choose the percentage of summarization, and generate a summary of your document.
Question Answering: Select the "Question Answering" tab, input your query, and receive an answer based on the content of your document.
View Results: The app will display the summarized content or the answer to your query.

Project Structure
app.py: The main Streamlit application code.
requirements.txt: List of dependencies required to run the application.
How It Works
Document Reading: The app reads and processes the uploaded documents, converting them into plain text.
VectorStore with FAISS: The document content is embedded using HuggingFaceEmbeddings, and a FAISS index is created for efficient similarity search.
Summarization: A BART model from Hugging Face is used to generate summaries.
Question Answering: A RoBERTa model fine-tuned for question answering is used to generate answers based on the content of the document.
Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for any suggestions or improvements.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgements
Streamlit
Hugging Face
LangChain
Contact
For any questions or suggestions, feel free to reach out via GitHub or email.

