import os
import whisper
import sys

class Mp3SpeechTranscriber:
    def __init__(self, input_path=None, output_path=None):
        self.input_path = input_path
        self.output_path = output_path

    def transcribe(self):
        try:
            # Load the Whisper model
            model = whisper.load_model("large")

            # Check if the input path is a directory or a file
            if os.path.isdir(self.input_path):
                # If it's a directory, process all MP3 files in the directory
                for filename in os.listdir(self.input_path):
                    if filename.endswith(".mp3"):
                        audio_file = os.path.join(self.input_path, filename)
                        transcription = model.transcribe(audio_file)
                        # Write the transcription to the output text file
                        output_file = os.path.join(self.output_path, filename.replace(".mp3", ".txt"))
                        print(output_file)
                        with open(output_file, "w") as text_file:
                            text_file.write(transcription["text"])
                        print(f"Transcribed {audio_file} to {output_file}")
            elif os.path.isfile(self.input_path) and self.input_path.endswith(".mp3"):
                # If it's a single MP3 file, transcribe it
                transcription = model.transcribe(self.input_path)
                # Write the transcription to the output text file
                output_file = os.path.join(self.output_path, os.path.basename(self.input_path).replace(".mp3", ".txt"))
                print(output_file)
                with open(output_file, "w") as text_file:
                    text_file.write(transcription["text"])
                print(f"Transcribed {self.input_path} to {output_file}")
            else:
                print("Invalid input. Cannot find the file or folder. Please provide a valid MP3 file or folder of MP3 files.")

        except Exception as e:
            print(f"An error occurred when transcribing: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python your_script.py input_path output_path")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # Create an instance of the AudioTranscriber class
    transcriber = Mp3SpeechTranscriber(input_path=input_path, output_path=output_path)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Call the transcribe method
    transcriber.transcribe()
