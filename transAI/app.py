
import streamlit as st
from langchain.llms import OpenAI
from backend import download_audio, transcribe_audio
from doc_generator import save_as_pdf, save_as_word

def main():
    st.title("YouTube Video Transcription")
    url = st.text_input("Enter YouTube URL:")
    format_choice = st.selectbox("Output Format", ["PDF", "Word"])

    if st.button("Transcribe"):
        audio_file = download_audio(url)
        transcript = transcribe_audio(audio_file)
        if format_choice == "PDF":
            save_as_pdf(transcript)
            with open("transcription.pdf", "rb") as file:
                st.download_button("Download PDF", file, "transcription.pdf", "application/pdf")
        else:
            save_as_word(transcript)
            with open("transcription.docx", "rb") as file:
                st.download_button("Download Word", file, "transcription.docx", "application/vnd.openxmlformats-officedocument.wordprocessingml.document")

if __name__ == "__main__":
    main()

