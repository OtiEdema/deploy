AI-Powered Document Analysis with RAG and Summarization

https://github.com/user-attachments/assets/11cce4f7-79a6-47b1-9772-09a4796e4b6f

Overview
This project demonstrates the implementation of an AI-powered application that uses Retrieval-Augmented Generation (RAG) to analyze and retrieve information from documents. The application is built using Large Language Models (LLMs) and Natural Language Processing (NLP) techniques, with the added capability of document summarization. The app allows users to upload a document, ask questions based on the document's content, and receive precise, context-aware answers. Additionally, it offers the ability to summarize lengthy documents according to a user-defined summarization percentage.

Key Features
Document Upload: Supports PDF, DOCX, and TXT file formats.
Document Summarization: Allows users to generate concise summaries of lengthy documents with customizable summarization percentages.
Question Answering: Users can enter queries and receive precise answers based on the document's content.
Efficient Retrieval: Uses FAISS (Facebook AI Similarity Search) for quick and accurate retrieval of relevant document sections.
Integration with Streamlit: A user-friendly web interface built with Streamlit for ease of use.
Technologies Used
Python: Core programming language.
Streamlit: For building the web interface.
Hugging Face Transformers:
AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForQuestionAnswering: Used for tokenization and running models for summarization and question answering.
LangChain:
HuggingFaceEmbeddings, FAISS, and RetrievalQA: For embedding documents and retrieving relevant content.
PyPDF2: For reading and extracting text from PDF documents.
python-docx: For reading and processing DOCX files.
FAISS: An efficient similarity search tool for vector indexing and retrieval.
Setup Instructions
Prerequisites
Make sure you have Python 3.8 or above installed on your system.

## Installation
Clone the repository:
git clone 
cd your-repo-name

## Create a virtual environment:
bash
Copy code
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

## Install the required packages:
bash
Copy code
pip install -r requirements.txt
Running the Application

## Start the Streamlit application:
bash
Copy code
streamlit run rag_app.py

##Upload a Document:
Open your web browser and go to the local URL provided by Streamlit.
Upload a document (PDF, DOCX, or TXT) using the file uploader.

## Summarize the Document:
Navigate to the Summarization tab.
Select the desired summarization percentage using the slider.
Click "Generate Summary" to see a concise summary of your document.

## Ask Questions:
Navigate to the Question Answering tab.
Enter a query in the text input field.
Click "Get Answer" to receive a precise, context-aware answer based on the document content.

## Code Explanation
Step 1: Imports and Document Reading
Imports:
The necessary libraries are imported, including Streamlit, PyPDF2, docx, Hugging Face Transformers, LangChain, and FAISS.

## Document Reading Function:
A function named read_document is defined to read and preprocess the uploaded document. It handles PDF, DOCX, and TXT file formats and returns the extracted text.

Step 2: Streamlit Setup and Document Display
Streamlit Interface:
The Streamlit app is configured with a title and layout. A file uploader component allows users to upload their documents.

## Document Display:
After uploading, the document content is displayed within the app, allowing users to review the document before querying or summarizing it.

Step 3: Embedding and Vector Store Setup

## Document Embeddings:
The document text is converted into embeddings using Hugging Face's HuggingFaceEmbeddings model.

## FAISS Vector Store:
A FAISS vector store is created to store the embeddings, allowing efficient retrieval of relevant document sections when queries are made.

Step 4: Language Model and RetrievalQA Setup
Tokenizer and Model Loading:
The tokenizer and language model for question answering are loaded using Hugging Face's AutoTokenizer and AutoModelForQuestionAnswering.

## Summarization Pipeline:
A summarization pipeline is created and wrapped in a HuggingFacePipeline, enabling the app to generate summaries based on the document content.

## RetrievalQA Chain:
The RetrievalQA chain is set up, linking the language model with the document retriever to generate accurate, contextually relevant answers.

Step 5: Query Input and Answer Generation
Query Input:
A text input field is created in Streamlit for users to enter their queries.

## Answer Generation:
The RetrievalQA chain retrieves the most relevant document sections and generates an answer, which is then displayed in the app.

## Demo
Upload a Sample Document:
Users can upload a document and test both the summarization and question-answering features.

## Enter Queries:
Example queries can be entered to see how the app retrieves and generates answers based on the document content.

## Conclusion
This RAG application demonstrates how to effectively use LangChain, FAISS, and Hugging Face Transformers to build an AI-powered document analysis tool. The app is versatile and can be expanded with additional features such as multi-document analysis or integration with other enterprise systems.

## Contact
For questions, suggestions, or collaborations, please reach out to me here at GitHub or Linkedin


