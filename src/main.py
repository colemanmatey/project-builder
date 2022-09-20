"""

"""

from core.builder import Builder


if __name__ == '__main__':
    sass = Builder("sass", "main.scss")
    structure = sass.load('sass.json')
    sass.build(structure)