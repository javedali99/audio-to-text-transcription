#This Python script downloads the audio or video from a YouTube link, uses OpenAI's Whisper to detect the language, and transcribes it into a .txt file.
#Author: Ruinan Ding

#Ruinan Ding

#Description
#To run this script, use the following command:
#python OpenAIWisperTranscriber.py
#Input the YouTube video URL when prompted, and it will download the audio and video streams from the URL along with the transcription of the audio.


#import required modules
import os
import whisper
from langdetect import detect
from pytube import YouTube


#Function to open a file
def startfile(fn):
    os.system('open %s' % fn)


#Function to create and open a txt file
def create_and_open_txt(text, filename):
    #Create and write the text to a txt file
    with open(filename, "w") as file:
        file.write(text)
    startfile(filename)


#Ask user for the YouTube video URL
url = input("Enter the YouTube video URL: ")

#Create a YouTube object from the URL
yt = YouTube(url)

#Uncomment the following lines to download the video stream
#Get the video stream
#video_stream = yt.streams.filter().first()
#Download the video stream
#output_path = "Video"
#filename = "Video.mp4"
#video_stream.download(output_path = output_path, filename = filename)

#Get the audio stream
audio_stream = yt.streams.filter(only_audio = True).first()

#Download the audio stream
output_path = "Audio"
filename = "Audio.mp3"
audio_stream.download(output_path = output_path, filename = filename)

print(f"Audio downloaded to {output_path}/{filename}")
print(f"Video downloaded to {output_path}/{filename}")

#Load the base model and transcribe the audio
model = whisper.load_model("base")
result = model.transcribe("Audio/Audio.mp3")
transcribed_text = result["text"]
print(transcribed_text)

#Delete the audio file
os.remove(f"{output_path}/{filename}")

#Detect the language
language = detect(transcribed_text)
print(f"Detected language: {language}")

#Create and open a txt file with the text
create_and_open_txt(transcribed_text, f"Transcription_{language}.txt")