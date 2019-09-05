
# Configs that can be change in an easy way from here
# Capital letters because they are import "CONSTANTS" for the game

from pathlib import Path

WIDTH = 400
HEIGHT = 400


BASE_DIR = Path(__file__).resolve().parent.parent #Path(__file__) gives us the path to our file. resolve().parent(to go  to config).parent(to  go  to demo and search for 'image' and then name of the file)
BACKGROUND = str(BASE_DIR/'image'/'floor-tiles-20x20.png')
HERO = str(BASE_DIR/'image'/'macgyver.png')


VELOCITY = 20