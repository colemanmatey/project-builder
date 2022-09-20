"""

"""

from sassbuilder import SassBuilder


if __name__ == '__main__':
    sass = SassBuilder("sass")
    structure = sass.load('sass.json')
    sass.build(structure)