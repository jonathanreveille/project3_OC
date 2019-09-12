
# Configs that can be change in an easy way from here
# Capital letters because they are import "CONSTANTS" for the game

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MAZE_LVL1= str(BASE_DIR/'macgyver'/'levels'/'maze1.txt')

# Explanation of the characters used to describe the maze from levels/
START_CHAR = 'S'
GUARD_CHAR = 'G'
WALL_CHAR = 'W'
PASSAGES_CHAR = '.'
HERO_CHAR = 'H'

#Screen size
WIDTH = 450
HEIGHT = 480
#chercher une image de mur en 40 pixel ou 50 pixel = donc 750 pixel en tout

#Load images for the maze
BACKGROUND = str(BASE_DIR/'macgyver'/'image'/'background.png')
WALL = str(BASE_DIR/'macgyver'/'image'/'wall.png')
PASSAGES = str(BASE_DIR/'macgyver'/'image'/'passages.png')

#image that moves while the game is running, or at start of the game : size 50x50 pixels
HERO = str(BASE_DIR/'macgyver'/'image'/'hero.png')
NEEDLE = str(BASE_DIR/'macgyver'/'image'/'needle.png')
TUBE = str(BASE_DIR/'macgyver'/'image'/'tube.png')
ETHER = str(BASE_DIR/'macgyver'/'image'/'ether.png')
GUARD = str(BASE_DIR/'macgyver'/'image'/'guard.png')

#Frame per second
VELOCITY = 30