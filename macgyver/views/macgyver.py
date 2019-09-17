#! /usr/bin/env python3
# coding : utf-8 
"""this class represents the hero in graphics and 
we control his directions according to moves"""

import pygame as pg
from config.settings import HERO, VELOCITY, SPRITE_WIDTH, SPRITE_HEIGHT
from macgyver.demo.mouvement import right, left, up, down

class MacGyver(pg.sprite.Sprite): #Classe d'héritage de Sprite
    """ class to add hero on game, record  his moves  and updates"""

    def __init__(self, hero): #Initializer
        
        super().__init__()  #calling sprites class to initialize object, use of super().__init__()
        self.image = pg.image.load(HERO).convert_alpha() #loading image
        self.rect = self.image.get_rect() # la position de MacGyver. get_rect = c'est le rectangle de mon image et sa position
        self.hero = hero


    def update(self):
        """ Methods that manages and tracks all updates from events"""
        self._process_keyboard_events()
        self.rect.x = self.hero.position.x * SPRITE_WIDTH
        self.rect.y = self.hero.position.y * SPRITE_HEIGHT

        # sur la base de la position de McG
    

    def _process_keyboard_events(self):
        """ method that captures events from user and do action for game"""
        
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key == pg.K_UP:
                #self.rect.move_ip(0, -VELOCITY)
                self.hero.move(up)
            
            elif event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
                #self.rect.move_ip(0, +VELOCITY)
                self.hero.move(down)
            elif event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
                #self.rect.move_ip(-VELOCITY, 0)
                self.hero.move(left)
            
            elif event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
                #self.rect.move_ip(VELOCITY, 0)
                self.hero.move(right)


    def _limits_moves(self, position):
        """method to make the hero stay on the screen"""
        return self.hero in self.gameboard.passages

    
# Ajouter la limite de MacGyver dans l'écran
