#! /usr/bin/env python3
# coding : utf-8 
"""this class represents the hero in graphics and 
we control his directions according to moves"""

import pygame as pg
from config.settings import HERO, VELOCITY


class MacGyver(pg.sprite.Sprite): #Classe d'héritage de Sprite
    """ class to add hero on game, record  his moves  and updates"""

    def __init__(self): #Initializer
        super().__init__()  #Appeller la méthode de  sprit  init elle-même 
        self.image = pg.image.load(HERO).convert() #l'image avec le convert
        self.rect = self.image.get_rect() # la position de MacGyver. get_rect = c'est le rectangle de mon image et sa position


    def update(self):
        """ Methods that manages and tracks all updates from events"""
        self._process_keyboard_events()
    

    def _process_keyboard_events(self):
        """ method that captures events from user and do action for game"""
        
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key == pg.K_UP:
                self.rect.move_ip(0, -VELOCITY)
            
            elif event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
                self.rect.move_ip(0, +VELOCITY)
            
            elif event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
                self.rect.move_ip(-VELOCITY, 0)
            
            elif event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
                self.rect.move_ip(VELOCITY, 0)

                # il bougera seulement dans passage

# Ajouter la limite de MacGyver dans l'écran
