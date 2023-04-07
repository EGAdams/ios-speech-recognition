
import os
import shutil


# Create directories
os.makedirs("project/agents")
os.makedirs("project/commands")
os.makedirs("project/tests")

# Create empty __init__.py files
open("project/agents/__init__.py", "w").close()
open("project/commands/__init__.py", "w").close()
open("project/tests/__init__.py", "w").close()

# Create main.py
open("project/main.py", "w").close()

# Create DirectoryCreatorAgent class
with open("project/agents/directory_creator_agent.py", "w") as f:
    f.write("""class DirectoryCreatorAgent:
    def __init__(self, directory_path):
        self.directory_path = directory_path

    def create_directory(self, directory_name):
        full_path = os.path.join(self.directory_path, directory_name)
        os.makedirs(full_path)
        return full_path
    """)

# Create DirectoryCreationCommand class
with open("project/commands/directory_creation_command.py", "w") as f:
    f.write("""from abc import ABC, abstractmethod

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
    """)

# Create test files
with open("project/tests/test_directory_creator_agent.py", "w") as f:
    f.write("""import os
from agents.directory_creator_agent import DirectoryCreatorAgent

def test_create_directory():
    agent = DirectoryCreatorAgent("test_directory")
    directory_name = "new_directory"
    result = agent.create_directory(directory_name)
    assert os.path.exists(result)
    assert os.path.isdir(result)
    """)

with open("project/tests/test_directory_creation_command.py", "w") as f:
    f.write("""from agents.directory_creator_agent import DirectoryCreatorAgent
from commands.directory_creation_command import CreateDirectoryCommand

def test_create_directory_command():
    agent = DirectoryCreatorAgent("test_directory")
    command = CreateDirectoryCommand(agent, "new_directory")
    result = command.execute()
    assert result == "test_directory/new_directory"
    assert os.path.exists(result)
    assert os.path.isdir(result)
    """)

# Copy over the .gitignore file
shutil.copy(".gitignore", "project/.gitignore")
