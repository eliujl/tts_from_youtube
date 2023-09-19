# examples of using TextToSpeechConverter class
from TextToSpeechConverter import TextToSpeechConverter

# Create an instance of the TextToSpeechConverter class
converter = TextToSpeechConverter('1', "../../testFiles/example.txt")
# Convert text to speech
converter.convert_to_speech()

# # Create an instance of the TextToSpeechConverter class
# converter = TextToSpeechConverter(2, "../../testFiles/example.txt")
# # Convert text to speech
# converter.convert_to_speech()
