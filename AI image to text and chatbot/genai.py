import streamlit as st
import google.generativeai as genai
import os
from PIL import Image
import textwrap
from io import BytesIO

# Set up your API key
os.environ['GEMINI_API_KEY'] = 'AIzaSyCgL6T4YL3hFdFccylZ8RCeQxAiUGADrc8'

# Configure the generative AI client
genai.configure(api_key=os.environ['GEMINI_API_KEY'])

def to_markdown(text):
    text = text.replace('•', '  *')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

def generate_text_prompt(prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text

def generate_image_text_prompt(image, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    image_part = {"mime_type": "image/jpeg", "data": image}
    response = model.generate_content([prompt, image_part])
    return response.text

# Streamlit UI
st.set_page_config(page_title="Oti AI Content Creator", page_icon=":robot_face:", layout="wide", initial_sidebar_state="expanded")

st.title("Oti AI Content Creator")
st.subheader("A futuristic way to generate content using text and images.")

option = st.selectbox("Choose the type of content generation:", ("Text Prompt", "Image and Text Prompt"))

if option == "Text Prompt":
    text_prompt = st.text_area("Enter your text prompt:")
    if st.button("Generate Content"):
        if text_prompt:
            st.markdown("### Generated Content")
            response_text = generate_text_prompt(text_prompt)
            st.markdown(to_markdown(response_text))
        else:
            st.error("Please enter a text prompt.")

elif option == "Image and Text Prompt":
    text_prompt = st.text_area("Enter your text prompt:")
    image_file = st.file_uploader("Upload an image:", type=["jpg", "jpeg", "png"])
    if st.button("Generate Content"):
        if text_prompt and image_file:
            image = Image.open(image_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            buffered = BytesIO()
            image.save(buffered, format="JPEG")
            response_text = generate_image_text_prompt(buffered.getvalue(), text_prompt)
            st.markdown("### Generated Content")
            st.markdown(to_markdown(response_text))
        else:
            st.error("Please enter a text prompt and upload an image.")

st.markdown("---")
st.markdown("**Chat with the AI**")
chat_history = st.session_state.get("chat_history", [])

if 'chat' not in st.session_state:
    model = genai.GenerativeModel('gemini-1.5-flash')
    st.session_state.chat = model.start_chat(history=[])

with st.form("chat_form"):
    chat_prompt = st.text_input("Enter your message:")
    submitted = st.form_submit_button("Send")
    if submitted and chat_prompt:
        response = st.session_state.chat.send_message(chat_prompt)
        chat_history.append(f"You: {chat_prompt}")
        chat_history.append(f"AI: {response.text}")
        st.session_state["chat_history"] = chat_history

for message in chat_history:
    st.markdown(to_markdown(message))

st.markdown("**End of Chat**")
