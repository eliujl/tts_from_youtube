# Fully Open-source Text-to-Speech Converter

This Python script allows you to convert text to speech using two different open-source engines: pyttsx3 and Coqui TTS. You can choose between speed and quality based on your needs. The packages for the engines can be installed locally and no internet connection is required. There is no subscription fee or usage limit.

## Features

- Choose between two text-to-speech engines.
- Convert text from a file to an MP3 audio file.


## Prerequisites

Before using this script, ensure you have the following dependencies installed:

- Python 3.x
- pyttsx3 (for option 1)
- Coqui TTS (for option 2)
- TTS models for Coqui TTS (specifically the model `jenny` is used in this script, which will be downloaded the first time you use it)
- Depending on your system, espeak-ng may need to be installed. For example, in Linux, install using:
```
sudo apt install espeak-ng
sudo apt install espeak-ng-data
```

## Usage

To use the script, follow these steps:

1. Clone the repository or download the script. There are two ways to use the script. 

2. You can run the script from the command line with the following options:

```shell
python TextToSpeechConverter.py [choice] [input_filename]
```

   - `choice` (optional): Enter `1` to use pyttsx3 (faster) or `2` to use Coqui TTS (better quality). If not provided, the default value `1` will be used (if `input_filename` is provided) or you will be prompted to choose (if `input_filename` is not provided).
   - `input_filename` (optional): Specify the input text file. If not provided, you will be prompted to enter it.

3. You can use the `TextToSpeechConverter` class in your own Python scripts to convert text to speech. Follow these steps to utilize the class:
   1. Import the `TextToSpeechConverter` class from the module:

   ```python
   from TextToSpeechConverter import TextToSpeechConverter
   ```
   2. Create an instance of the class, specifying your choice and input file as arguments. You can choose between two text-to-speech engines: 1 for pyttsx3 (faster) or 2 for Coqui TTS (better quality). Optionally, you can provide just the input file, and the choice will be prompted when running the script. Examples are provided in `tts_test_script.py`.


4. The script will synthesize the speech and save it as an MP3 file in the same directory as the input text file.

## Example

To convert a text file named `example.txt` to speech using Coqui TTS, you can run one of the following command:

```shell
python text_to_speech_converter.py 2 example.txt
python text_to_speech_converter.py example.txt
```

To use the class, one example is:
```python
from TextToSpeechConverter import TextToSpeechConverter

converter = TextToSpeechConverter('1', "../../testFiles/example.txt")
converter.convert_to_speech()

```


