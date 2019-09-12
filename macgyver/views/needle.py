#! /usr/bin/env python3
# coding : utf-8 

"""class that will represent the item named Needle"""

import pygame as pg
from config.settings import NEEDLE

class Needle(pg.sprite.Sprite): #Classe d'héritage de Sprite
    """ class to add item named NEEDLE on gameboard """

    def __init__(self): #Initializer
        super().__init__()  #Appeller la méthode de  sprit  init elle-même 
        self.image = pg.image.load(NEEDLE).convert_alpha() #l'image avec le convert
        self.rect = self.image.get_rect()

        #DON'T FORGET TO ADD THEM INTO THE GAME, ONCE and only, 
        # when ALL MOVING OBJECTS
        #IN GAME ARE SET and READY to be inserted