#! /usr/bin/env python3
# coding : utf-8 

""" Module for pygame interface"""

import pygame as pg

from config import settings
from macgyver.views.macgyver import MacGyver
from macgyver.views.items import ItemSprite
from macgyver.views.guard import Guard
from macgyver.models.gameboard import GameBoard
from macgyver.models.hero import Hero
from macgyver.models.items import Item, N, E, T
from macgyver.exceptions.gamewon import GameWon
from macgyver.exceptions.gameover import GameOver


class Game:
    """ Class that represents the game for pygame"""

    def __init__(self): #Constructor
        """ All elements that are needed for the game to be played """

        self.gameboard = GameBoard() #creating a GameBoard()
        self.gameboard.load_from_file() #loading file from models gameboard.py
        self.gameboard.add_items(N) #adding item from models items.py
        self.gameboard.add_items(E)
        self.gameboard.add_items(T)
        self.hero = Hero(self.gameboard) #putting the hero into the GameBoard

        pg.init() #Initializing pygame
        
        pg.display.set_caption("MacGyver's Mad Escape") #Set the title on screen

        self.screen = pg.display.set_mode((settings.WIDTH, settings.HEIGHT)) #1. Set the size of the screen in pixels
        self.background = pg.image.load(settings.BACKGROUND).convert_alpha() #2. Set an attribute for the background, the image is its value

        self.lost = pg.image.load(settings.LOST).convert_alpha() #loading image for loosing game
        self.won = pg.image.load(settings.WON).convert_alpha() #loading image for winning game

        
        self.wall = pg.image.load(settings.WALL).convert_alpha() #loading image that is wall
        for wall in self.gameboard.walls: # Add images for each wall
            self.background.blit(self.wall, (wall.x*settings.SPRITE_WIDTH, wall.y*settings.SPRITE_HEIGHT)) #copie and size of image (x,y)

        self.passages = pg.image.load(settings.PASSAGES).convert_alpha() #loading image of passage
        for passages in self.gameboard.passages:  # Add images for each passage path
            self.background.blit(self.passages,(passages.x* settings.SPRITE_WIDTH, passages.y* settings.SPRITE_HEIGHT))
        
        self.screen.blit(self.background, (0,0), self.screen.get_rect()) # Copie the background over the screen. It's called to '.blit()'.

        self.sprites = pg.sprite.RenderUpdates() # Sprites - We use a pygame method to manage updates with sprites  

        # We add our sprites into the gameboard
        self.sprites.add(MacGyver(self.hero))
        self.sprites.add(Guard())
        self.sprites.add(ItemSprite(settings.TUBE_PATH, T, self.gameboard))
        self.sprites.add(ItemSprite(settings.ETHER_PATH, E, self.gameboard))
        self.sprites.add(ItemSprite(settings.NEEDLE_PATH, N, self.gameboard))

        pg.key.set_repeat(500, 100) #Allows the player to keep on pressing down the key and the hero moves

        pg.display.update() # Always update

        #The switch ON/OFF (T/F boolean) for the gameloop 
        self.running = False


    def start(self):
        """Method that launches the game"""

        clock = pg.time.Clock()
        self.running = True #the True or False switch
        
        try:
            
            while self.running: #loop of the game launch

                clock.tick(40) #Frame per seconds. In order words, the speed of the loop.
                
                self._process_quit_events() #process to close the game window

                #1. Cover the gamespace with the background, we clear our screen 
                #   and put our background over it
                self.sprites.clear(self.screen, self.background) 
                
                #2. Call update() methods from for classes that are from sprites
                self.sprites.update()
                
                #3. Draws over what should be drawn, paste or blits all different images on screen
                updated_sprites = self.sprites.draw(self.screen)
                
                #4 Returns the list of updated sprites that were modified from last loop lap
                pg.display.update(updated_sprites)

       
        except GameWon as e: #if gamer wins
            print(e)
            self.running = True
            self.display_message(self.won)

        
        except GameOver as e: #if gamer looses
            print(e)
            self.running = True
            self.display_message(self.lost)


    def _process_quit_events(self):
        """ method that quits the game when the user press the RED CROSS on window"""
        for _ in pg.event.get(pg.QUIT):
            self.running = False


    def display_message(self, image):
        """ method that adds a screen for GameOver or GameWon"""
        self.running = True
        self.background = image
        self.screen.blit(self.background, self.screen.get_rect())
        pg.display.update()
        self.start()


def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()