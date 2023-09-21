# test script for TestMp3SpeechTranscriber class. Execute: python -m unittest TestMp3SpeechTranscriber
import unittest
import os
from Mp3SpeechTranscriber import Mp3SpeechTranscriber

class TestMp3SpeechTranscriber(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = "test_output"
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        # Clean up the temporary directory
        for file in os.listdir(self.test_dir):
            file_path = os.path.join(self.test_dir, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        os.rmdir(self.test_dir)

    def test_transcribe_single_file(self):
        input_path = "../../testFiles/example.mp3"
        output_path = self.test_dir
        transcriber = Mp3SpeechTranscriber(input_path=input_path, output_path=output_path)
        transcriber.transcribe()
        output_file = os.path.join(output_path, "example.txt")
        self.assertTrue(os.path.isfile(output_file))

    def test_transcribe_directory(self):
        input_path = "../../testFiles"
        output_path = self.test_dir
        transcriber = Mp3SpeechTranscriber(input_path=input_path, output_path=output_path)
        transcriber.transcribe()
        output_file_1 = os.path.join(output_path, "example.txt")
        output_file_2 = os.path.join(output_path, "example1.txt")
        self.assertTrue(os.path.isfile(output_file_1))
        self.assertTrue(os.path.isfile(output_file_2))

if __name__ == "__main__":
    unittest.main()
