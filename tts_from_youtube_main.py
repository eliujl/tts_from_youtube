import sys
import os
from pytube import Playlist
from process_video import process_video


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
