""" Here is a file to control all the Configs of the game
Parameters can be easily changed from here """

from pathlib import Path

# Screen size
WIDTH = 450
HEIGHT = 480

# Rectangle (or sprite) size
SPRITE_WIDTH = 30
SPRITE_HEIGHT = 30

# Legend for characters used to decrypt the maze content from levels/
START_CHAR = 'S'
GUARD_CHAR = 'G'
WALL_CHAR = 'W'
PASSAGES_CHAR = '.'
HERO_CHAR = 'H'

# Loading method variable BASE_DIR, using __file__ magic method
BASE_DIR = Path(__file__).resolve().parent.parent

# Loading maze
MAZE_LVL1 = str(BASE_DIR/'macgyver'/'levels'/'maze1.txt')

# Loading music

# Loading background
BACKGROUND = str(BASE_DIR/'macgyver'/'image'/'background.png')
INTRO = str(BASE_DIR/'macgyver'/'image'/'intro.png')

# Loading images paths
WALL = str(BASE_DIR/'macgyver'/'image'/'bush.png')
PASSAGES = str(BASE_DIR/'macgyver'/'image'/'passages.png')

# Loading characters
HERO = str(BASE_DIR/'macgyver'/'image'/'hero.png')
GUARD = str(BASE_DIR/'macgyver'/'image'/'guard.png')

# Loading items
NEEDLE_PATH = str(BASE_DIR/'macgyver'/'image'/'needle.png')
TUBE_PATH = str(BASE_DIR/'macgyver'/'image'/'tube.png')
ETHER_PATH = str(BASE_DIR/'macgyver'/'image'/'ether.png')

# Loading pop up image at end of the game
WON = str(BASE_DIR/'macgyver'/'image'/'won.png')
LOST = str(BASE_DIR/'macgyver'/'image'/'lost.png')

#Frame per second
VELOCITY = 40


