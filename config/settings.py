
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

#Screen size
WIDTH = 300
HEIGHT = 300
#chercher une image de mur en 40 pixel ou 50 pixel = donc 750 pixel en tout

#Load images for game
BACKGROUND = str(BASE_DIR/'macgyver'/'image'/'background.png')
HERO = str(BASE_DIR/'macgyver'/'image'/'hero.png')
NEEDLE = str(BASE_DIR/'macgyver'/'image'/'needle.png')
TUBE = str(BASE_DIR/'macgyver'/'image'/'tube.png')
ETHER = str(BASE_DIR/'macgyver'/'image'/'ether.png')

#os.path.join method 
#BACKGROUND = os.path.join('image', 'background.png')
#HERO = os.path.join('image', 'macgyver.png')
#NEEDLE = os.path.join('image', 'needle.png')
#TUBE = os.path.join('image','tube.png')
#ETHER = os.path.join('image','ether.png')


#Frame per second
VELOCITY = 30


#BASE_DIR = Path(__file__).resolve().parent #Path(__file__) gives us the path 
#to our file. resolve().parent(to go  to config).parent(to  go  
#to demo and search for 'image' and then name of the file)
#str(BASE_DIR/'image'/'background.png') 
#str(BASE_DIR/'image'/'macgyver.png')