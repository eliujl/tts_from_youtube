# Text-to-Speech from YouTube
## Re-synthesizing clean audio (audo only) from text transcribed from youtube video / playlist. Fully open-source, fully local.



This Python script allows you to download a YouTube video or playlist, transcribe into text, and then resynthesize back to audio. The repo for the engines can be installed locally and no internet connection is required. There is no subscription fee or usage limit.

## Motivation
There are many valuable YouTube videos worth revisiting, such as insightful lectures or educational content. I often listen to them using an audioplayer. However, the audio quality in these videos can be less than ideal, having issues like background noise, loud mouse clicking and keyboard typing, various accents, fluctuating volume, long pauses, or rapid speech, making them challenging to comprehend or enjoy. 

This repo aims to address these challenges by extracting only the audio, enhancing its quality, and generating a clean version that eliminates these issues. Now, I can listen to my favorite content using audioplayer without any distractions, enabling a more immersive and enjoyable learning experience.

(TBD) Furthermore, the intermediate result of transcribed text allows for easier editing / LLM processing, such as adding intro / outro / summary, removing repetitions, correcting grammatical errors, cleaning up verbal fillers such as uh and oh, rewriting / expanding /shortening a sentence or paragraph, etc. 



## Features

- Download audio from YouTube videos or playlists.
- Transcribe audio to text using local Whisper model (by OpenAI) for easier editing and processing.
- Resynthesize cleaned audio in MP3 format using one of two text-to-speech (TTS) engines for a high-quality listening experience.

## Prerequisites

Ensure you have the following dependencies installed:

- Python 3.x
- [pytube](https://github.com/nficano/pytube):  A lightweight, dependency-free Python library for downloading YouTube videos and playlists.
- [Whisper](https://github.com/openai/whisper):  OpenAI's Whisper for transcription. Note that the package is called openai-whisper (not just whisper, which is a different package).
- [pyttsx3](https://pypi.org/project/pyttsx3/) TTS engine option 1. Extremely lightweight and fast.
- [Coqui TTS](https://github.com/coqui-ai/TTS) TTS engine option 2. 
- TTS models for Coqui TTS (specifically the model `jenny` is used in this script, which will be automatically downloaded the first time you use it)
- [espeak-ng](https://github.com/espeak-ng/espeak-ng) Depending on your system, espeak-ng may need to be installed. For example, in Linux, install using:
```
sudo apt install espeak-ng
sudo apt install espeak-ng-data
```

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/eliujl/tts_from_youtube
   cd tts_from_youtube
   pip install -r requirements.txt
   ```

## Usage


Run the script with the following command:

```bash
python tts_from_youtube_main.py <YouTube video or playlist URL> <output directory>
```

If you don't provide an output directory, the script will use a temporary folder in the current directory.

Example Usages
Download and re-synthesize audio from a YouTube video:

```bash
python tts_from_youtube_main.py https://youtu.be/TCH_1BHY58I
```

Download and re-synthesize audio from a YouTube playlist:

```bash
python tts_from_youtube_main.py https://youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ&si=WQc1A7wJbwymLY0L
```

Specify output directory:

```bash
python tts_from_youtube_main.py https://youtu.be/TCH_1BHY58I ./temp_audio
```

If no YouTube URL is given when starting the Python script, it will ask you to enter a URL and specify an output directory (press Enter to use the default temporary folder).

