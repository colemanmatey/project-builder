"""

"""

import json
from pathlib import Path


# Path of the root directory
BASE_DIR = Path(__file__).resolve().parent

# Path of output
BUILD_DIR = BASE_DIR / 'build'


class Builder:

    def __init__(self, root_dir=None, index_file=None):
        """
        Create root directory and index file
        """
        self.root_dir = root_dir
        self.index_file = index_file
        self.structure = None

        # Initialize Builder
        self.mkdirs(self.root_dir)
        self.touch(self.root_dir, [self.index_file])


    def load(self, filename):
        """
        Read project structure from a JSON file
        """
        with open(BASE_DIR / filename, 'r') as f:
            return json.load(f)


    def mkdirs(self, folder, *args):
        """
        Create folders using the keys in the json file loaded
        """
        if self.root_dir != None:
            Path(BUILD_DIR / self.root_dir).mkdir(parents=True, exist_ok=True)
            for folder in args:
                Path(BUILD_DIR / folder).mkdir(parents=True, exist_ok=True)


    def touch(self, folder, files):
        """
        Create files using the values in the json file loaded
        """
        # Create folder if it does not exist
        self.root_dir = folder
        path = Path(BUILD_DIR / self.root_dir)
        if path.exists() != 'True':
            path.mkdir(parents=True, exist_ok=True)

        # Create files
        for file in files:
            self.index_file = file
            if self.index_file != None:
                Path(BUILD_DIR / self.root_dir / self.index_file).touch(exist_ok=True)


    def build(self, structure):
        """
        Build the project structure
        """
        self.structure = structure

        if self.structure != None:
            # Create folders
            for directory in self.directories:
                Path(directory).mkdir(parents=True, exist_ok=True)
            
            # Create files
            for file in self.files:
                file.touch(exist_ok=True)

    
    @property
    def directories(self):
        """
        Returns a tuple of all folder paths
        """
        return (
            Path(BUILD_DIR / self.root_dir / directory)
            for directory in self.structure.keys()
        )


    @property
    def files(self):
        """
        Returns a tuple of all file paths
        """
        return (
            Path(BUILD_DIR / self.root_dir / directory / file)
            for directory in self.structure 
            for file in self.structure[directory]
        )