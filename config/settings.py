
# Configs that can be change in an easy way from here
# Capital letters because they are import "CONSTANTS" for the game

import os
from pathlib import Path

#Screen size
WIDTH = 450
HEIGHT = 480

# Explanation of the characters used to describe the maze from levels/
START_CHAR = 'S'
GUARD_CHAR = 'G'
WALL_CHAR = 'W'
PASSAGES_CHAR = '.'
HERO_CHAR = 'H'


#Load method
BASE_DIR = Path(__file__).resolve().parent.parent
#Load maze
MAZE_LVL1= str(BASE_DIR/'macgyver'/'levels'/'maze1.txt')
#Load images
BACKGROUND = str(BASE_DIR/'macgyver'/'image'/'background.png')
WALL = str(BASE_DIR/'macgyver'/'image'/'wall.png')
PASSAGES = str(BASE_DIR/'macgyver'/'image'/'passages.png')
HERO = str(BASE_DIR/'macgyver'/'image'/'hero.png')
NEEDLE = str(BASE_DIR/'macgyver'/'image'/'needle.png')
TUBE = str(BASE_DIR/'macgyver'/'image'/'tube.png')
ETHER = str(BASE_DIR/'macgyver'/'image'/'ether.png')
GUARD = str(BASE_DIR/'macgyver'/'image'/'guard.png')

#Frame per second
VELOCITY = 30