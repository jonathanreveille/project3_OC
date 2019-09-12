#! /usr/bin/env python3
# coding : utf-8 

""" this class will make the view (graphics) of the maze """

import pygame as pg

from macgyver.demo.gameboard import GameBoard
from macgyver.demo.position import Position
from macgyver.pygamemain import Game
from config.settings import WALL, BACKGROUND, PASSAGE 

#from config.settings import WALL_IMG, PASSAGE_IMG

class Labyrinth(pg.sprite.Sprite):
    def __init__(self):

        self.image = pg.image.load(WALL).convert_alpha()
        self.rect = self.image.get_rect()
        

class LabyrinthView:
    pass

    #def __init__(self):

       # """this methods prepares the wall images position"""

        #for position in self.gameboard.walls:
        #    self.sprites.add(self.image)




def main():
    pass

if __name__ == "__main__":
    main()
