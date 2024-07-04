# Ensure necessary libraries are installed
# Run these commands in your terminal
# pip install streamlit pillow selenium webdriver-manager youtube-search-python googlesearch-python wikipedia-api requests

import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from youtubesearchpython import VideosSearch
import googlesearch
import wikipediaapi
import requests

# Function to send WhatsApp message using Selenium and ChromeDriver
def send_whatsapp_message(number, message):
    st.info(f"Sending message to {number}...")

    try:
        # Initialize ChromeDriver
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--headless")  # Commenting out headless mode
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

        # Open WhatsApp Web
        driver.get('https://web.whatsapp.com/')

        # Display the QR code to the user and wait for them to scan it
        st.info("Please scan the QR code and then press the button to continue.")
        # Add a sleep to ensure QR code loads
        time.sleep(30)  # Increased sleep time to 30 seconds

        if st.button("Continue after scanning QR code"):
            # Locate the chat input element
            search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')

            # Type the recipient number
            search_box.send_keys(f"{number}{Keys.ENTER}")

            # Wait for the chat to load
            time.sleep(5)  # Increased wait time

            # Locate the message input element
            input_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="1"]')

            # Type the message
            input_box.send_keys(message)
            input_box.send_keys(Keys.ENTER)

            # Close the WebDriver session
            driver.quit()

            st.success(f"Message sent to {number}: {message}")

    except Exception as e:
        st.error(f"Error: {e}")

# Function to play YouTube video
def play_youtube_video(video_query):
    st.info(f"Playing YouTube video: {video_query}")
    try:
        videos_search = VideosSearch(video_query, limit=1)
        video_result = videos_search.result()['result'][0]
        video_url = video_result['link']
        st.video(video_url)
    except Exception as e:
        st.error(f"Error: {e}")

# Function to perform Google search
def google_search(query):
    st.info(f"Performing Google search: {query}")
    try:
        search_results = googlesearch.search(query, num_results=5)
        for result in search_results:
            st.write(result)
    except Exception as e:
        st.error(f"Error: {e}")

# Function to get information from Wikipedia
def get_wikipedia_info(topic):
    st.info(f"Getting information from Wikipedia about: {topic}")
    try:
        session = requests.Session()
        session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
        wiki_wiki = wikipediaapi.Wikipedia('en', session=session)
        page = wiki_wiki.page(topic)
        if page.exists():
            st.write(page.summary)
        else:
            st.error(f"No information found for {topic} on Wikipedia.")
    except Exception as e:
        st.error(f"Error: {e}")

# Function to convert text to handwritten image using Pillow
def convert_to_handwritten(text, style):
    # Define paths to your installed fonts
    font_paths = {
        "AlexBrush": r"C:\deploy\educational\hand written fonts\alex-brush\AlexBrush-Regular.ttf",
        "ChunkFive": r"C:\deploy\educational\hand written fonts\chunkfive\ChunkFive-Regular.otf",
        "KaushanScript": r"C:\deploy\educational\hand written fonts\kaushan-script\KaushanScript-Regular.otf",
        "Playwrite_ES_Deco": r"C:\deploy\educational\hand written fonts\Playwrite_ESDeco\PlaywriteESDeco-VariableFont_wght.ttf",
        "SourceCodePro": r"C:\deploy\educational\hand written fonts\source-code-pro\SourceCodePro-Light.otf",
        # Add more styles as needed
    }

    # Ensure the selected style has a defined font path
    if style in font_paths:
        font_path = font_paths[style]
    else:
        st.error("Font path not defined for selected style.")
        return

    try:
        max_width = 800  # Max width of the image
        max_height = 200  # Max height of the image

        # Initialize font size based on available space
        font_size = min(max_width // len(text), max_height)

        # Load the selected font
        font = ImageFont.truetype(font_path, size=font_size)

        # Create a blank image
        image = Image.new('RGB', (max_width, max_height), color=(255, 255, 255))
        draw = ImageDraw.Draw(image)

        # Calculate text bounding box
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # Calculate text position to center it vertically and horizontally
        text_x = (max_width - text_width) // 2
        text_y = (max_height - text_height) // 2

        # Draw text on image
        draw.text((text_x, text_y), text, fill=(0, 0, 0), font=font)

        # Save image to file
        image.save('output.png')

        # Display the image
        st.image("output.png", caption="Handwritten Text")

    except OSError as e:
        st.error(f"Error loading font: {e}")

# Main function to run the Streamlit app
def main():
    st.title("Personalized Educational Assistant")

    # Sidebar with options
    st.sidebar.header("Select an Option")
    selected_option = st.sidebar.selectbox("Choose an Option", ["Send WhatsApp Message", "Play YouTube Video",
                                                               "Google Search", "Get Wikipedia Info",
                                                               "Convert Text to Handwritten"])

    if selected_option == "Send WhatsApp Message":
        st.subheader("Send WhatsApp Message")
        number = st.text_input("Recipient's Phone Number (include country code, e.g., +123456789)")
        message = st.text_area("Message")
        if st.button("Send"):
            send_whatsapp_message(number, message)

    elif selected_option == "Play YouTube Video":
        st.subheader("Play YouTube Video")
        video_query = st.text_input("Enter Video Query")
        if st.button("Play"):
            play_youtube_video(video_query)

    elif selected_option == "Google Search":
        st.subheader("Perform Google Search")
        query = st.text_input("Enter your query")
        if st.button("Search"):
            google_search(query)

    elif selected_option == "Get Wikipedia Info":
        st.subheader("Get Information from Wikipedia")
        topic = st.text_input("Enter topic")
        if st.button("Get Info"):
            get_wikipedia_info(topic)

    elif selected_option == "Convert Text to Handwritten":
        st.subheader("Convert Text to Handwritten")
        text = st.text_area("Enter text to convert")
        style = st.selectbox("Select Handwriting Style", ["AlexBrush", "ChunkFive", "KaushanScript", "Playwrite_ES_Deco", "SourceCodePro"])
        if st.button("Convert"):
            convert_to_handwritten(text, style)

if __name__ == "__main__":
    main()
