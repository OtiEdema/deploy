Generative AI Content Generator

https://github.com/OtiEdema/deploy/assets/71005527/a0f042fd-499b-4bf1-a692-03cf68d2be1e

This project demonstrates how to use the Google Generative AI API to generate content. It includes setting up the environment, configuring the API client, and generating text using the GenerativeModel.

Table of Contents
Installation
Setup
Usage
Troubleshooting
License

Installation
First, ensure you have the necessary dependencies installed. You can install them using the following command:


!pip install -q -U google-generativeai

Setup
Google Cloud Project:
Create a Google Cloud project at Google Cloud Console.
Enable billing for your project.
Enable the "Generative Language API" in the API library.

API Key:
Create an API key in the Google Cloud Console.
Set up the environment variable for the API key in your code:
import os
os.environ['GEMINI_API_KEY'] = 'YOUR_API_KEY_HERE'
Google Colab:

Mount your Google Drive to save or load files:
from google.colab import drive
drive.mount('/content/drive')

Usage
Import the Generative AI Module:
import google.generativeai as genai

Configure the Generative AI Client:
genai.configure(api_key=os.environ['GEMINI_API_KEY'])

Generate Content:
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("What is the meaning of life.")
print(response.text)

Troubleshooting
400 POST Error:
Ensure that your Google Cloud project has a billing account linked.
Verify that the "Generative Language API" is enabled.
Check for any regional restrictions that might apply to your location.

Environment Variable Issues:
Make sure that the API key is correctly set as an environment variable.
Verify the syntax and ensure there are no typos in the API key.
License
=======
Generative AI Content Generator


Video DEMO

https://github.com/OtiEdema/deploy/assets/71005527/a0f042fd-499b-4bf1-a692-03cf68d2be1e


This project demonstrates how to use the Google Generative AI API to generate content. It includes setting up the environment, configuring the API client, and generating text using the GenerativeModel.

Table of Contents
Installation
Setup
Usage
Troubleshooting
License

Installation
First, ensure you have the necessary dependencies installed. You can install them using the following command:


!pip install -q -U google-generativeai

Setup
Google Cloud Project:
Create a Google Cloud project at Google Cloud Console.
Enable billing for your project.
Enable the "Generative Language API" in the API library.

API Key:
Create an API key in the Google Cloud Console.
Set up the environment variable for the API key in your code:
import os
os.environ['GEMINI_API_KEY'] = 'YOUR_API_KEY_HERE'
Google Colab:

Mount your Google Drive to save or load files:
from google.colab import drive
drive.mount('/content/drive')

Usage
Import the Generative AI Module:
import google.generativeai as genai

Configure the Generative AI Client:
genai.configure(api_key=os.environ['GEMINI_API_KEY'])

Generate Content:
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("What is the meaning of life.")
print(response.text)

Troubleshooting
400 POST Error:
Ensure that your Google Cloud project has a billing account linked.
Verify that the "Generative Language API" is enabled.
Check for any regional restrictions that might apply to your location.

Environment Variable Issues:
Make sure that the API key is correctly set as an environment variable.
Verify the syntax and ensure there are no typos in the API key.
License
>>>>>>> c882ae8b17243d93d3bb4b30b23449f3bddfe530
This project is licensed under the MIT License. See the LICENSE file for details.