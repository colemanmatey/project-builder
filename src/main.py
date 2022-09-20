"""

"""

from core.builder import Builder


if __name__ == '__main__':
    sass = Builder('sass')
    structure = sass.load('sass.json')
    sass.build(structure)