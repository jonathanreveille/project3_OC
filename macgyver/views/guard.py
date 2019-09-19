""" class that represent graphic element of the Guard in the game """
#! /usr/bin/env python3
# coding : utf-8 

"""This module represents the sprite that is set on the goal
position of the maze """

import pygame as pg
from config.settings import GUARD

class Guard(pg.sprite.Sprite):
    """ class to represent guard """
    
    def __init__(self):

        super().__init__()
        self.image = pg.image.load(GUARD).convert_alpha()
        self.rect = self.image.get_rect(x=420,y=420)

def main():
    pass

if __name__ == "__main__":
    main()
