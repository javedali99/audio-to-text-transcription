# 🤖🎬 YouTube Audio-to-Text Transcription 🎧📝

A sophisticated and user-friendly automation that downloads audio from YouTube videos, transcribes the content into text, detects the language of the transcribed text, and saves the transcription to a text file. Save time, effort, and resources by harnessing cutting-edge technology to streamline the transcription process.

## Table of Contents

- [🤖🎬 YouTube Audio-to-Text Transcription 🎧📝](#-youtube-audio-to-text-transcription-)
  - [Description](#description)
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

   3. Download FFmpeg and add it to environment variables.
   Windows:
   https://phoenixnap.com/kb/ffmpeg-windows
   Mac:
   https://phoenixnap.com/kb/ffmpeg-mac
   Ubuntu:
   https://phoenixnap.com/kb/install-ffmpeg-ubuntu
      
## Usage

1. Run the script:

   ```bash
   python OpenAIWisperTranscriber.py
   ```

2. When prompted, enter the YouTube video URL you wish to transcribe:

   ```
   Enter the YouTube video URL in this format: https://www.youtube.com/watch?v=XXXXXXXXXXX
   ```

3. The script will download the audio, transcribe it, detect language, and save the transcription to a text file called `Transcription_{language}.txt`.

4. Access the transcription by opening the `Transcription_{language}.txt` file located in the same directory as the script.

## Workflow

1. The user inputs a YouTube video URL when prompted.
2. The `pytube` library is used to create a `YouTube` object and filter the audio stream.
3. The audio stream is downloaded as an MP3 file and saved in the `Audio` folder.
4. The `whisper` library loads a base model and transcribes the downloaded audio into text.
5. The `langdetect` library detects the language of the transcribed text.
6. The transcription is saved to a text file named `Transcription_{language}.txt` with the language code as part of the filename and opened for the user to view.

## Known Issues

Once in a few while, the punctuations gets ruined. Sometimes this happens for the whole transcript, sometimes it happens at the middle of it.

Sometimes, the spelling is wrong, you can prompt ChatGPT to fix it or manually fix it using Cltr+R.

Also, once a while, the script may throw an exception regarding some regex expression in `cipher.py` or some sorts randomly one day. This is believed to be caused by some sort of change on the YouTube server side. You can try some suggestion regarding modifying the regex expression suggested on StackOverflow which may or may not work, but usually, this script starts working again the next day or in a few hours. Meanwhile, you can prompt ChatGPT to transcribe off of the YouTube auto-generated transcript

## Tips

You can prompt ChatGPT to fix the puncutations when it happens:

```bash
Fix the punctuations or grammar below but keep the output verbatim:

<insert generated text>
```

It may often picks up the wrong words, you can prompt ChatGPT to fix it and paste in the transcript, for example:

```bash
Below is a machine-generated transcript. Correct any misspellings and grammar but do not summarize the transcript or leave anything out:


<insert generated text>
```

Or you can use the Cont+R and manually replace the mispellings with a text editor.

Another way to get a transcript is that you can grab the transcript from YouTube, provided it has an auto-generated text, and paste it to chatgpt and ask it to transcribe it:

```bash
`You are a professional transcriber with 20 years of experience and you have been transcribing transcripts in verbatim for 20 years. You will turn a YouTube video transcript below into proper English format verbatim so I can watch the video and follow the transcript exactly word for word. Leave out any timestamps but do not leave out any context. Do not summarize anything in the output:


<insert generated text>
```

As of GPT-3.5, it tends to summerize the youtube transcript if it is too long, so you may need to break it into parts and ask ChatGPT to do each individually.

How to get YouTube transcript:
https://www.descript.com/blog/article/transcript-of-youtube-videos

You can ask ChatGPT to refine the transcript, like using this prompt for example:

```bash
Turn the transcript below, word for word, without leaving out any words or sentences. Correct any wrong English. Add section titles:


<insert generated text>
```

Or prompt ChatGPT to process it into a summary like:

```bash
Summarize into key takeaways:

<insert generated text>
```

You can even prompt ChatGPT to translate it into a different Language:

```bash
You are a professional translator with 20 years of experience and you have been translating transcripts in verbatim for 20 years. You will turn a YouTube video transcript below into proper <language> verbatim so I can watch the video and follow the transcript exactly word for word in that language. Leave out any timestamps but do not leave out any context. Do not summarize anything in the output:

<insert generated text>
```

## Contributing 🤝🌱

Contributions from users are highly valued and appreciated. There are two main ways to contribute to this project: through pull requests and issues.

### Pull Requests

1. Fork the repository and create a branch from the `main` branch.
2. Make changes or additions to the code.
3. Commit the changes, and push them to the branch.
4. Open a pull request to the `main` branch with a clear and concise description of the changes.

### Issues

1. Navigate to the [Issues](https://github.com/Ruinan-Ding/openai-wisper-transcriber/pulls) section of the repository.
2. Check if there is an existing issue similar to the one you'd like to create.
3. If there isn't an existing issue, create a new issue by clicking the "New issue" button.
4. Provide a descriptive title and detailed information about the proposed changes that you want to potentially add to the current script.

---

🎓🌟 Feel free to contribute, share, and spread the love 💖💬🌍
