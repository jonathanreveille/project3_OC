
# Configs that can be change in an easy way from here
# Capital letters because they are import "CONSTANTS" for the game

import os
from pathlib import Path

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
BACKGROUND = os.path.join('image', 'background.png')
HERO = os.path.join('image', 'macgyver.png')
NEEDLE = os.path.join('image', '')

#Frame per second
VELOCITY = 20


#BASE_DIR = Path(__file__).resolve().parent #Path(__file__) gives us the path 
#to our file. resolve().parent(to go  to config).parent(to  go  
#to demo and search for 'image' and then name of the file)
#str(BASE_DIR/'image'/'background.png') 
#str(BASE_DIR/'image'/'macgyver.png')