import speech_recognition as sr
import time
import threading
import sys

class CommandHandler:
    def process_command(self, command):
        print("Processing command...")
        if command == "stop":
            return False

        # Implement command processing logic here
        # print the contents of the command
        print(command)
        # Implement other command processing logic here
        pass

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

class StdinHandler:
    def process_input(self):
        while True:
            command = input("Enter a command: ").strip()
            should_continue = self.process_command(command)
            if not should_continue:
                break

    def process_command(self, command):
        print("Processing stdin command...")
        if command == "stop":
            return False

        # Implement command processing logic here
        # print the contents of the command
        print(command)
        # Implement other command processing logic here
        return True

class Recognizer:
    def __init__(self, command_handler, speech_recognizer, stdin_handler):
        self.command_handler = command_handler
        self.speech_recognizer = speech_recognizer
        self.stdin_handler = stdin_handler
        self.stop_flag = threading.Event()
   
    def process_audio(self, audio_data):
        # if the audio_data is valid
        if( audio_data is   not None ):
             command = self.speech_recognizer.recognize_speech(audio_data)
        else:
            print ( "bad audio_data, returning from process_audio... " )
            return

        if command:
            print(f"Detected command: {command}")
            should_continue = self.command_handler.process_command(command)
            if not should_continue:
                raise KeyboardInterrupt
        else:
            print("Could not understand audio")

    def run(self):
        # Start the speech recognition thread
        speech_thread = threading.Thread(target=self.run_speech_recognition)
        speech_thread.start()

        # Start the stdin input thread
        stdin_thread = threading.Thread(target=self.run_stdin_input)
        stdin_thread.start()

        # Wait for both threads to complete
        speech_thread.join()
        stdin_thread.join()

    def run_speech_recognition(self):
        with sr.Microphone() as source:
            print("Recognizer started listening")
            while not self.stop_flag.is_set():
                try:
                    audio_data = self.speech_recognizer.recognizer.listen(source, timeout=1) # Add a timeout for the listening duration

                except sr.WaitTimeoutError:
                    pass  # If the timeout occurs, simply continue listening
                except KeyboardInterrupt:
                    print("Stopping recognizer")
                    self.stop_flag.set()


    def run_stdin_input(self):
        try:
            self.stdin_handler.process_input()
        except KeyboardInterrupt:
            print("Stopping stdin input")
        finally:
            self.stop_flag.set()

if __name__ == "__main__":
    command_handler = CommandHandler()
    speech_recognizer = SpeechRecognizer()
    stdin_handler = StdinHandler()
    recognizer = Recognizer(command_handler, speech_recognizer, stdin_handler)
    recognizer.run()
