# YouTube Audio-to-Text Transcription 🤖🎬🎧📝

Unleash the power of automation with this sophisticated and user-friendly script that downloads audio from YouTube videos, transcribes the content into text, and saves the transcription to a text file. Save time, effort, and resources by harnessing cutting-edge technology to streamline the transcription process.

## Table of Contents

- [YouTube Audio-to-Text Transcription 🤖🎬🎧📝](#youtube-audio-to-text-transcription-)
  - [Table of Contents](#table-of-contents)
  - [Detailed Description](#detailed-description)
  - [Key Features](#key-features)
  - [Prerequisites](#prerequisites)
  - [Required Libraries](#required-libraries)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Workflow](#workflow)
  - [Contributing 🤝🌱](#contributing-)

## Detailed Description

This script is designed to facilitate the transcription of YouTube videos into text format. It eliminates the need for time-consuming manual transcription by automating the process through a series of well-defined steps. The user-friendly interface allows users to input a YouTube video URL, which is then processed to extract the audio, convert it into text, and save the transcription as a text file. This efficient and convenient solution is ideal for those who require quick and accurate transcriptions for various purposes, such as research, content creation, or accessibility.

## Key Features

- **User-friendly:** Designed for ease of use, the script prompts users to enter a YouTube video URL, minimizing the need for complicated setup processes.
- **Efficient Audio Extraction:** The script utilizes the `pytube` library to effectively filter and download the audio stream from the specified YouTube video.
- **High-Quality Transcription:** The `whisper` library, a powerful speech-to-text tool, is employed to accurately transcribe the downloaded audio into text.
- **Convenient Output:** The transcription is saved as a text file in the same directory as the script, ensuring easy access and sharing capabilities.

## Prerequisites

1. Python 3.9+
2. `pip` to install required libraries

## Required Libraries

- `pytube`: A lightweight Python library that enables the downloading of YouTube videos and the extraction of audio streams.

- `whisper`: An advanced speech-to-text library that facilitates accurate and efficient transcription of audio files.

## Installation

1. Clone this repository or download the script.
2. Install the required libraries:

   ```bash
   pip install pytube
   ```

   ```bash
   pip install git+https://github.com/openai/whisper.git
   ```

## Usage

1. Run the script:

   ```bash
   python youtube_audio_to_text.py
   ```

2. When prompted, enter the YouTube video URL you wish to transcribe:

   ```
   Enter the YouTube video URL: https://www.youtube.com/watch?v=XXXXXXXXXXX
   ```

3. The script will download the audio, transcribe it, and save the transcription to a text file called `output.txt`.

4. Access the transcription by opening the `output.txt` file located in the same directory as the script.

## Workflow

1. The user inputs a YouTube video URL when prompted.
2. The `pytube` library is used to create a `YouTube` object and filter the audio stream.
3. The audio stream is downloaded as an MP3 file and saved in the `YoutubeAudios` folder.
4. The `whisper` library loads a base model and transcribes the downloaded audio into text.
5. The transcription is saved to a text file named `output.txt` and opened for the user to view.

## Contributing 🤝🌱

We believe that collaboration and community-driven development are crucial to achieving the best results. Your contributions are highly valued and much appreciated. We welcome ideas, suggestions, and improvements from everyone. To contribute to this project, please follow these steps:

1. Fork the repository and create your branch from the `main` branch.
2. Make your changes or additions to the code.
3. Commit your changes, and push them to your branch.
4. Open a pull request to the `main` branch with a clear and concise description of your changes.

Together, we can enhance this script, making it more efficient, user-friendly, and powerful. Thank you for being part of our community and contributing to the growth of this project! 🎉🙌

---

🎓🌟 Feel free to contribute, share, and spread the love 💖💬🌍
