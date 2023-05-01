import argparse
import sys
import speech_recognition as sr
import time

class CommandHandler:
    def process_command(self, command):
        print("Processing command...")
        if command == "stop":
            return False

        # Implement command processing logic here
        # print the contents of the command
        print(command)
        # Implement other command processing logic here
        return True

class SpeechRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def recognize_speech(self, audio_data):
        try:
            command = self.recognizer.recognize_google(audio_data)
            return command
        except sr.UnknownValueError:
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None

class Recognizer:
    def __init__(self, command_handler, speech_recognizer):
        self.command_handler = command_handler
        self.speech_recognizer = speech_recognizer

    def process_audio(self, audio_data):
        command = self.speech_recognizer.recognize_speech(audio_data)
        if command:
            print(f"Detected command: {command}")
            should_continue = self.command_handler.process_command(command)
            if not should_continue:
                raise KeyboardInterrupt
        else:
            print("Could not understand audio")

    def run_speech_recognition(self):
        with sr.Microphone() as source:
            print("Recognizer started listening")
            while True:
                try:
                    audio_data = self.speech_recognizer.recognizer.listen(source, timeout=1)
                    self.process_audio(audio_data)
                except sr.WaitTimeoutError:
                    pass
                except KeyboardInterrupt:
                    print("Stopping recognizer")
                    break

    def run_stdin_recognition(self):
        print("Recognizer started listening to stdin")
        while True:
            try:
                command = input("Enter a command: ")
                should_continue = self.command_handler.process_command(command)
                if not should_continue:
                    break
            except KeyboardInterrupt:
                print("Stopping recognizer")
                break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Choose input method for the Recognizer.')
    parser.add_argument('--stdin', action='store_true', help='Use stdin as input.')
    parser.add_argument('--audio', action='store_true', help='Use microphone audio as input.')
    args = parser.parse_args()

    if not (args.stdin or args.audio):
        print("Please specify an input method using --stdin or --audio.")
        sys.exit(1)

    command_handler = CommandHandler()
    speech_recognizer = SpeechRecognizer()
    recognizer = Recognizer(command_handler, speech_recognizer)

    if args.stdin:
        recognizer.run_stdin_recognition()
    elif args.audio:
        recognizer.run_speech_recognition()
