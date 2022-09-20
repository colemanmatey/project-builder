"""

"""

from pathlib import Path

from core.settings import BUILD_DIR
from core.builder import Builder


class SassBuilder(Builder):

    def __init__(self,  root_dir="sass", index_file="main.scss"):
        super().__init__(root_dir, index_file)


    def build(self, structure, blank=False):
        super().build(structure)

        if blank == False:
            self.write_description()
            self.create_indices()
            self.compose_main()


    def write_description(self):
        """Write a brief description to each partial file"""

        for file in self.files:
            with file.open('w', encoding='utf-8') as f:
                stem = self.get_name(file.name)
                f.write(f"// {stem.capitalize()}\n\n")


    def create_indices(self):
        """Create an index partial in each directory"""
        
        # Create index partial
        for dir_path in self.directories:
            index = Path(dir_path / '_index.scss')
            index.touch(exist_ok=True)
            
            # Open the index file and import partials
            with index.open('w') as f:
                f.write(f"// {dir_path.stem.capitalize()}\n")
                for partial in self.structure[dir_path.stem]:
                    if partial != '_index.scss':
                        f.write(f"@forward '{dir_path.stem}/{self.get_name(partial)}';\n")

    def compose_main(self):
        """Compose main file"""

        file = Path(BUILD_DIR / self.root_dir / self.index_file)

        with file.open('w') as f:
            for directory in self.directories:
                f.write(f"// {directory.stem} styles\n")
                f.write(f"@use '{directory.stem}';\n\n")


    def get_name(self, file):
        """Return the file name without prefixes and extensions"""
        if file.startswith('_'):
            name = self.remove_prefix(file, '_')
            stem = Path(name).stem    
        return stem


    def remove_prefix(self, text, prefix):
        """Remove prefix from file names"""
        return text[text.startswith(prefix) and len(prefix):]


