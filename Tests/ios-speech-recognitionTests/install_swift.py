class SwiftInstaller:
    def __init__(self):
        self.package_manager = None
    
    def set_package_manager(self, package_manager):
        self.package_manager = package_manager
        
    def install_swift(self):
        if self.package_manager is not None:
            print("Installing Swift using", self.package_manager)
            # Code to install swift using the package manager goes here]]

    import subprocess

    def install_swift():
        command = "sudo apt-get update && sudo apt-get install swift"
        subprocess.run(command, shell=True)

      
class PackageManager:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name

if __name__ == '__main__':
    # Define the package manager to be used
    package_manager = PackageManager('apt-get')

    # Install Swift using the pdackage manager
    swift_installer = SwiftInstaller()
    swift_installer.set_package_manager(package_manager)
    swift_installer.install_swift()
