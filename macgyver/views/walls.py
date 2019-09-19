#! /usr/bin/env python3
# coding : utf-8 

""" this class will make the view (graphics) of the maze """

import pygame as pg
from config.settings import WALL

#from config.settings import WALL_IMG, PASSAGE_IMG

class Walls(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pg.image.load(WALL).convert()
        self.rect = self.image.get_rect()
        
        
        #self.background.blit(self.image(420,420))

        #brouillon
        #for position in game.gameboard.goals:
            #self.image = position
            #self.background.get_rect())


        #Comment faire pour la porté de mon attribut de mon objet gameboard = Gameboard()?
        #importer Gameboard()
        #for self.walls in self.gameboard.walls:
            #faire un blit() sur le background
            #tout ce qui ne bouge pas, on peut le "bliter" dans background


def main():
    pass

if __name__ == "__main__":
    main()


#class LabyrinthView:
    #pass

    #def __init__(self):

       # """this methods prepares the wall images position"""

        #for position in self.gameboard.walls:
        #    self.sprites.add(self.image)


