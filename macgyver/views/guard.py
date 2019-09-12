""" class that represent graphic element of the Guard in the game """
#! /usr/bin/env python3
# coding : utf-8 


from config.settings import GUARD
#from demo.gameboard import GameBoard
import pygame as pg

class Guard(pg.sprite.Sprite):
    """ class to represent guard """
    
    def __init__(self):

        super().__init__()
        self.image = pg.image.load(GUARD).convert_alpha()
        self.rect = self.image.get_rect()
        
        #self.gb = GameBoard()
        #self.position = self.gb.goal


def main():
    pass

if __name__ == "__main__":
    main()
