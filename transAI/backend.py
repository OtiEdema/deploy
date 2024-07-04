from pytube import YouTube
from langchain import OpenAI

def download_audio(url):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=".")
    return out_file

def transcribe_audio(audio_file):
    model = OpenAI()
    transcript = model.transcribe(audio_file)
    return transcript
