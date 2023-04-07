import os
from agents.directory_creator_agent import DirectoryCreatorAgent

def test_create_directory():
    agent = DirectoryCreatorAgent("test_directory")
    directory_name = "new_directory"
    result = agent.create_directory(directory_name)
    assert os.path.exists(result)
    assert os.path.isdir(result)
    