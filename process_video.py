import os
from pytube import YouTube
from moviepy.editor import AudioFileClip
from Mp3SpeechTranscriber import Mp3SpeechTranscriber
from TextToSpeechConverter import TextToSpeechConverter

# Function to replace invalid characters in a string
def sanitize_filename(filename):
    invalid_chars = ['?', ':', '|', '*', '<', '>', '\\', '/']
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename

# Function to download and process a single video
def process_video(video_url, output_directory):
    try:
        yt = YouTube(video_url)
        video = yt.streams.filter(only_audio=True).first()
        # Download the audio
        print(f"Downloading: {video.title}")
        video.download(output_path=output_directory)
        filename = sanitize_filename(yt.title)
        downloaded_file_path = os.path.join(output_directory, video.default_filename)
        mp3filename = os.path.join(output_directory, filename + '.mp3')
        audio = AudioFileClip(downloaded_file_path)
        audio.write_audiofile(mp3filename)
        print(f"Converted: {filename} to {mp3filename}")

        txtfilename = os.path.join(output_directory, filename + '.txt')
        transcriber = Mp3SpeechTranscriber(input_path=mp3filename, output_path=output_directory)
        print(f"To transcribe {mp3filename} to {txtfilename}")
        transcriber.transcribe()
        print(f"Transcribed: {filename} to {txtfilename}")

        # Create an instance of the TextToSpeechConverter class
        converter = TextToSpeechConverter('1', txtfilename)
        print(f"To synthesize {filename} to speech")
        # Convert text to speech
        converter.convert_to_speech()
        print(f"Synthesized {filename} to speech file.")
    except Exception as e:
        print(f"Error downloading {video_url}: {str(e)}")