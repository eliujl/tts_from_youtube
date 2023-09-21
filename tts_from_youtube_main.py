from pytube import Playlist, YouTube
from moviepy.editor import AudioFileClip
import os
import sys
from Mp3SpeechTranscriber import Mp3SpeechTranscriber
from TextToSpeechConverter import TextToSpeechConverter

# Get the input URL 
if len(sys.argv) == 2:
    playlist_url = sys.argv[1]
elif len(sys.argv) == 1:
    playlist_url = input('Enter youtube video playlist URL: ')
else:
    print("Usage: python tts_from_youtube_main.py <YouTube video or playlist URL>")
    sys.exit(1)

# Check if the input URL is a playlist or a single video
if 'playlist' in playlist_url:
    # It's a playlist
    playlist = Playlist(playlist_url)
    # Create a list of video URLs
    video_urls = [video_url for video_url in playlist]
else:
    # It's a single video, convert it into a list
    video_urls = [playlist_url]

# Define the directory to save the downloaded MP3s
output_directory = 'C:\home\j\Videos\\audio'

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Iterate through the videos in the playlist
for video_url in video_urls:
    try:
        yt = YouTube(video_url)
        video = yt.streams.filter(only_audio=True).first()
        # Download the audio
        print(f"Downloading: {video.title}")
        video.download(output_path=output_directory)
        filename = yt.title
        downloaded_file_path = os.path.join(
            output_directory, video.default_filename)
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
print("Downloaded audio, transcribed to text, and resynthesized to audio.")
