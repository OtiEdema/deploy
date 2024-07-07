Personalized Educational Assistant

https://github.com/OtiEdema/deploy/assets/71005527/1ae4075b-27bf-44aa-bc9a-67b8d2010ca5


This Streamlit web application serves as a personalized educational assistant with several features including sending WhatsApp messages, playing YouTube videos, performing Google searches, retrieving information from Wikipedia, and converting text to handwritten images using different styles.

Features
Send WhatsApp Message: Send messages to WhatsApp contacts.
Play YouTube Video: Search and play videos directly from YouTube.
Perform Google Search: Conduct Google searches from within the app.
Get Wikipedia Info: Retrieve information about various topics from Wikipedia.
Convert Text to Handwritten: Generate handwritten-style images from input text.

Installation

Clone the repository:

Install dependencies:

pip install -r requirements.txt

Download and configure ChromeDriver:

Place the executable (chromedriver.exe for Windows) in a directory accessible by your PATH environment variable, or specify its path in app.py where WebDriver is instantiated.

Run the Streamlit app:
streamlit run app.py

Open the app in your browser:
The app will open in your default web browser at http://localhost:8501.

Usage
Select an option from the sidebar to perform the desired action.
Follow the instructions for each feature:
WhatsApp Message: Scan the QR code and enter recipient's number and message.
YouTube Video: Enter a search query and click 'Play'.
Google Search: Enter a query and click 'Search'.
Wikipedia Info: Enter a topic and click 'Get Info'.
Convert to Handwritten: Enter text and choose a handwriting style, then click 'Convert'.

Technologies Used

Python
Streamlit
Selenium (for WhatsApp messaging)
Pillow (PIL) for image processing

Contributing
Contributions are welcome! Please fork the repository and create a pull request with your suggested changes.

License
This project is licensed under the MIT License - see the LICENSE file for details.