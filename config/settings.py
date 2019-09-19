
# Configs that can be change in an easy way from here
# Capital letters because they are import "CONSTANTS" for the game

import os
from pathlib import Path

#Screen size
WIDTH = 450
HEIGHT = 480
SPRITE_WIDTH = 30
SPRITE_HEIGHT = 30
#multiplier les images par les dimensions ci-dessus


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

#Load images paths
BACKGROUND = str(BASE_DIR/'macgyver'/'image'/'background.png')
WALL = str(BASE_DIR/'macgyver'/'image'/'wall.png')
PASSAGES = str(BASE_DIR/'macgyver'/'image'/'passages.png')

HERO = str(BASE_DIR/'macgyver'/'image'/'hero.png')

GUARD = str(BASE_DIR/'macgyver'/'image'/'guard.png')

BOX = str(BASE_DIR/'macgyver'/'image'/'box.png')
NEEDLE_PATH = str(BASE_DIR/'macgyver'/'image'/'needle.png')
TUBE_PATH = str(BASE_DIR/'macgyver'/'image'/'tube.png')
ETHER_PATH = str(BASE_DIR/'macgyver'/'image'/'ether.png')


#Frame per second
VELOCITY = 50