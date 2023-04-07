from abc import ABC, abstractmethod

class DirectoryCreationCommand(ABC):
    @abstractmethod
    def execute(self):
        pass

class CreateDirectoryCommand(DirectoryCreationCommand):
    def __init__(self, agent, directory_name):
        self.agent = agent
        self.directory_name = directory_name

    def execute(self):
        return self.agent.create_directory(self.directory_name)
    