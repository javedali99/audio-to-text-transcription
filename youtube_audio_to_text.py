# Transform an audio from a YouTube video to text script with language detection.
# Author: Javed Ali (www.javedali.net)

# Description: This script will ask the user for a YouTube video URL, download the audio from the video, transform it to text, detect the language of the file and save it to a txt file.


# import required modules
import os

import whisper
from langdetect import detect
from pytubefix import YouTube


# Function to open a file
def startfile(fn):
    os.system('open %s' % fn)


# Function to create and open a txt file
def create_and_open_txt(text, filename):
    # Create and write the text to a txt file
    with open(filename, "w") as file:
        file.write(text)
    startfile(filename)


# Ask user for the YouTube video URL
url = input("Enter the YouTube video URL: ")

# Create a YouTube object from the URL
yt = YouTube(url)

# Get the audio stream
audio_stream = yt.streams.filter(only_audio=True).first()

# Download the audio stream
output_path = "YoutubeAudios"
filename = "audio.mp3"
audio_stream.download(output_path=output_path, filename=filename)

print(f"Audio downloaded to {output_path}/{filename}")

# Load the base model and transcribe the audio
model = whisper.load_model("base")
result = model.transcribe("YoutubeAudios/audio.mp3")
transcribed_text = result["text"]
print(transcribed_text)

# Detect the language
language = detect(transcribed_text)
print(f"Detected language: {language}")

# Create and open a txt file with the text
create_and_open_txt(transcribed_text, f"output_{language}.txt")
