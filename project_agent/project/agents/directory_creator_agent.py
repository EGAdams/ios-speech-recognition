class DirectoryCreatorAgent:
    def __init__(self, directory_path):
        self.directory_path = directory_path

    def create_directory(self, directory_name):
        full_path = os.path.join(self.directory_path, directory_name)
        os.makedirs(full_path)
        return full_path
    