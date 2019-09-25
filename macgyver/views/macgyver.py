#! /usr/bin/env python3
# coding : utf-8 
"""this class represents the hero in graphics and 
we control his directions according to moves"""

import pygame as pg
from config.settings import HERO, VELOCITY, SPRITE_WIDTH, SPRITE_HEIGHT
from macgyver.models.mouvement import right, left, up, down

class MacGyver(pg.sprite.Sprite):
    """ This class inherits from sprite class. This is the class
    to represent our hero, record his moves and update position """

    def __init__(self, hero): #Initializer
        
        super().__init__()  #calling sprites class to initialize object, use of super().__init__()
        self.image = pg.image.load(HERO).convert_alpha() #loading image
        self.rect = self.image.get_rect() # get_rect = rectangle of the image and its position
        self.hero = hero

    def update(self):
        """ Method that manages and tracks all updates from events"""
        self._process_keyboard_events()
        self.rect.x = self.hero.position.x * SPRITE_WIDTH
        self.rect.y = self.hero.position.y * SPRITE_HEIGHT

    def _process_keyboard_events(self):
        """ Method that captures events keys from gamer and it does action in the game"""
    
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key == pg.K_UP:
                self.hero.move(up)
            
            elif event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
                self.hero.move(down)
                
            elif event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
                self.hero.move(left)
            
            elif event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
                self.hero.move(right)


    def _limits_moves(self):
        """ method that keeps the hero (MacGyver) in the maze,
        he can't go over edges """
        return self.hero in self.gameboard.passages
