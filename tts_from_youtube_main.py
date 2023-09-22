import sys
import os
from pytube import Playlist, YouTube
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

# Main function
def main():
    # Get the input URL
    if len(sys.argv) >= 2:
        playlist_url = sys.argv[1]
    elif len(sys.argv) == 1:
        playlist_url = input('Enter YouTube video or playlist URL: ')
    else:
        print("Usage: python tts_from_youtube_main.py <YouTube video or playlist URL>")
        sys.exit(1)

    # Use the second command-line argument as the output directory, if provided
    if len(sys.argv) >= 3:
        output_directory = sys.argv[2]
    else:
        # If not provided, use a default temporary folder under the current directory
        # Prompt the user to enter the output directory or use a temporary one
        output_directory = input('Enter output directory (leave empty for a temporary folder in the current directory): ').strip()
        if not output_directory:
            output_directory = os.path.join(os.getcwd(), 'temp_files')
  
    # Check if the input URL is a playlist or a single video
    if 'playlist' in playlist_url:
        # It's a playlist
        playlist = Playlist(playlist_url)
        # Create a list of video URLs
        video_urls = [video_url for video_url in playlist]
    else:
        # It's a single video, convert it into a list
        video_urls = [playlist_url]

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Iterate through the videos in the playlist
    for video_url in video_urls:
        process_video(video_url, output_directory)

    print("Downloaded audio, transcribed to text, and resynthesized to audio.")

if __name__ == "__main__":
    main()
