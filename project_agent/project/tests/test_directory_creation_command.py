from agents.directory_creator_agent import DirectoryCreatorAgent
from commands.directory_creation_command import CreateDirectoryCommand

def test_create_directory_command():
    agent = DirectoryCreatorAgent("test_directory")
    command = CreateDirectoryCommand(agent, "new_directory")
    result = command.execute()
    assert result == "test_directory/new_directory"
    assert os.path.exists(result)
    assert os.path.isdir(result)
    