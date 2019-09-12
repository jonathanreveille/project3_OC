#! /usr/bin/env python3
# coding : utf-8 

import pygame as pg
from config.settings import TUBE

class Tube(pg.sprite.Sprite): #Classe d'héritage de Sprite
    """ class to add hero on game, record  his moves  and updates"""

    def __init__(self): #Initializer
        super().__init__()
        self.image = pg.image.load(TUBE).convert_alpha() #l'image avec le convert
        self.rect = self.image.get_rect()


    def _add_on_game(self):
        """method that helps item to show on random position"""
        pass



def main():
    pass

if __name__ == "__main__":
    main()
