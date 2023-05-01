from abc import ABC, abstractmethod


# Observer pattern: Subject interface
class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self, command):
        pass


# Observer pattern: Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, command):
        pass


# Factory Method pattern: Creator interface
class RecognizerFactory(ABC):
    @abstractmethod
    def create_recognizer(self):
        pass


# Strategy pattern: Strategy interface
class CommandHandler(ABC):
    @abstractmethod
    def handle_command(self, command):
        pass


# AI Assistant class
class AIAssistant(Observer):
    def __init__(self, recognizer_factory: RecognizerFactory, command_handler: CommandHandler):
        self.recognizer = recognizer_factory.create_recognizer()
        self.command_handler = command_handler
        self.recognizer.attach(self)

    def update(self, command):
        self.command_handler.handle_command(command)

    def start_listening(self):
        self.recognizer.start_listening()

    def stop_listening(self):
        self.recognizer.stop_listening()

