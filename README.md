# 🤖🎬 YouTube Audio-to-Text Transcription 🎧📝

Unleash the power of automation with this sophisticated and user-friendly script that downloads audio from YouTube videos, transcribes the content into text, detects the language of the transcribed text, and saves the transcription to a text file. Save time, effort, and resources by harnessing cutting-edge technology to streamline the transcription process.

## Table of Contents

- [🤖🎬 YouTube Audio-to-Text Transcription 🎧📝](#-youtube-audio-to-text-transcription-)
  - [Table of Contents](#table-of-contents)
  - [Detailed Description](#detailed-description)
  - [Key Features](#key-features)
  - [Prerequisites](#prerequisites)
  - [Required Libraries](#required-libraries)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Workflow](#workflow)
  - [Contributing 🤝🌱](#contributing-)
    - [Pull Requests](#pull-requests)
    - [Issues](#issues)

## Description

This script is designed to facilitate the transcription of YouTube videos into text format. It eliminates the need for time-consuming manual transcription by automating the process through a series of well-defined steps. The user-friendly interface allows users to input a YouTube video URL, which is then processed to extract the audio, convert it into text, and save the transcription as a text file. This efficient and convenient solution is ideal for those who require quick and accurate transcriptions for various purposes, such as research, content creation, or accessibility.

## Key Features

- **User-friendly:** Designed for ease of use, the script prompts users to enter a YouTube video URL, minimizing the need for complicated setup processes.
- **Efficient Audio Extraction:** The script utilizes the `pytube` library to effectively filter and download the audio stream from the specified YouTube video.
- **High-Quality Transcription:** The `whisper` library, a powerful speech-to-text tool, is employed to accurately transcribe the downloaded audio into text.
- **Convenient Output:** The transcription is saved as a text file in the same directory as the script, ensuring easy access and sharing capabilities.

## Prerequisites

1. Python 3.6+
2. `pip` to install required libraries

## Required Libraries

- `pytube`: A lightweight Python library that enables the downloading of YouTube videos and the extraction of audio streams.

- `whisper`: An advanced speech-to-text library that facilitates accurate and efficient transcription of audio files.
- `langdetect`: A language detection library ported from Google's language-detection.

## Installation

1. Clone this repository or download the script.
2. Install the required libraries:

   ```bash
   pip install pytube
   ```

   ```bash
   pip install git+https://github.com/openai/whisper.git
   ```

   ```bash
   pip install langdetect
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

3. The script will download the audio, transcribe it, detect language and save the transcription to a text file called `output_{language}.txt`.

4. Access the transcription by opening the `output_{language}.txt` file located in the same directory as the script.

## Workflow

1. The user inputs a YouTube video URL when prompted.
2. The `pytube` library is used to create a `YouTube` object and filter the audio stream.
3. The audio stream is downloaded as an MP3 file and saved in the `YoutubeAudios` folder.
4. The `whisper` library loads a base model and transcribes the downloaded audio into text.
5. The `langdetect` library detects the language of the transcribed text.
6. The transcription is saved to a text file named `output_{language}.txt` with the language code as part of the filename and opened for the user to view.

## Contributing 🤝🌱

Contributions from users are highly valued and appreciated. The ideas, suggestions, and improvements are welcome from everyone. There are two main ways to contribute to this project: through pull requests and issues.

### Pull Requests

1. Fork the repository and create a branch from the `main` branch.
2. Make changes or additions to the code.
3. Commit the changes, and push them to the branch.
4. Open a pull request to the `main` branch with a clear and concise description of the changes.

### Issues

1. Navigate to the [Issues](https://github.com/javedali99/whisper-openai/issues) section of the repository.
2. Check if there is an existing issue similar to the one you'd like to create.
3. If there isn't an existing issue, create a new issue by clicking the "New issue" button.
4. Provide a descriptive title and detailed information about the proposed changes that you want to potentially add to the current script.

---

🎓🌟 Feel free to contribute, share, and spread the love 💖💬🌍
