#! /usr/bin/env python3
# coding : utf-8 

import pygame as pg
from config.settings import ETHER

class Ether(pg.sprite.Sprite): #Classe d'héritage de Sprite
    """ class to add hero on game, record  his moves  and updates"""

    def __init__(self): #Initializer
        super().__init__()  #Appeller la méthode de  sprit  init elle-même 
        self.image = pg.image.load(ETHER).convert_alpha() #l'image avec le convert
        self.rect = self.image.get_rect()


