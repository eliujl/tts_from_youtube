import os
import sys

class TextToSpeechConverter:
    def __init__(self, choice=None, input_filename=None):
        self.choice = choice
        self.input_filename = input_filename

	# Function to get input text from a file and generate an output filename
    def get_input_and_output_filenames(self):
        input_filename = self.input_filename
        try:
        	# Get the text from the txt file.
            with open(input_filename) as f:
                text = f.read()
        except FileNotFoundError:
            print(f"Error: The file '{input_filename}' does not exist.")
            sys.exit(1)
        except Exception as e:
            print(f"Error: An error occurred while reading the file '{input_filename}': {e}")
            sys.exit(1)

        input_directory = os.path.dirname(os.path.abspath(input_filename))
        filename = os.path.basename(f.name)
        filename_no_ext = os.path.join(input_directory, os.path.splitext(filename)[0])

        return text, filename_no_ext

	# Function to convert text to speech using pyttsx3
    def convert_to_speech_with_pyttsx3(self):
        import pyttsx3

        text, filename_no_ext = self.get_input_and_output_filenames()
        output_filename = f"{filename_no_ext}_tts.mp3"

        print(f"Synthesizing {filename_no_ext}.txt to {output_filename}")

        try:
            # init function to get an engine instance for the speech synthesis
            self.engine = pyttsx3.init(driverName='sapi5')
            self.engine.setProperty('rate', 180)  # setting up new voice rate
            voices = self.engine.getProperty('voices')
            self.engine.setProperty('voice', voices[1].id)

            self.engine.save_to_file(text, output_filename)
            self.engine.runAndWait()

            print(f"Completed synthesizing {filename_no_ext}.txt to {output_filename}")
        except Exception as e:
            print(f"Error: An error occurred during the conversion: {e}")
            sys.exit(1)

	# Function to convert text to speech using Coqui TTS
    def convert_to_speech_with_coqui_tts(self):
        from TTS.api import TTS
        import torch

        text, filename_no_ext = self.get_input_and_output_filenames()
        output_filename = f"{filename_no_ext}_coqui.mp3"

        print(f"Synthesizing {filename_no_ext}.txt to {output_filename}")

        try:
            print(f"To convert to {output_filename}")

	        # Get device
            device = "cuda" if torch.cuda.is_available() else "cpu"

            tts = TTS(model_name="tts_models/en/jenny/jenny", progress_bar=True).to(device)
            tts.tts_to_file(text, file_path=output_filename)

            print(f"Completed synthesizing {filename_no_ext}.txt to {output_filename}")
        except Exception as e:
            print(f"Error: An error occurred during the conversion: {e}")
            sys.exit(1)

    # Main function to handle user input and choices
    def convert_to_speech(self):
        if self.choice is None:
            print("Choose an option for synthesizing speech from text:")
            print("1. Convert to speech with pyttsx3 (faster)")
            print("2. Convert to speech with Coqui TTS (better quality)")
            self.choice = input("Enter your choice (1 or 2): ")
        if self.input_filename is None:
            self.input_filename = input("Enter the input txt filename: ")

        if self.choice == '1' or self.choice == 1:
            self.convert_to_speech_with_pyttsx3()
        elif self.choice == '2' or self.choice == 2:
            self.convert_to_speech_with_coqui_tts()
        else:
            print(f"Invalid choice {self.choice}. Please enter 1 or 2")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        choice = sys.argv[1]
        input_filename = sys.argv[2]
        converter = TextToSpeechConverter(choice, input_filename)
    elif len(sys.argv) == 2:
        choice = '1'
        input_filename = sys.argv[1]
        converter = TextToSpeechConverter(choice, input_filename)
    else:
        converter = TextToSpeechConverter()

    converter.convert_to_speech()