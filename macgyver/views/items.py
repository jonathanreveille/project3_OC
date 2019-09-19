#! /usr/bin/env python3
# coding : utf-8 
""" Module to load items into the game in graphic mode"""

import pygame as pg
from macgyver.demo.gameboard import GameBoard
from macgyver.demo.position import Position
from macgyver.demo.items import Item
from config.settings import SPRITE_WIDTH, SPRITE_HEIGHT

class Items(pg.sprite.Sprite):

    def __init__(self, image, items):
        super().__init__()

        self.gameboard = GameBoard()
        self.items = self.gameboard.items
        self.image = pg.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()


    def update(self):
        """method that checks if the item is still on the gameboard or if the hero the pick it up"""
        
        pos =  Position(self.rect.x, self.rect.y)

        if pos in self.gameboard.items:
            return Position(self.rect.x*SPRITE_WIDTH, self.rect.y* SPRITE_HEIGHT)
        else:
            pass


def main():
    pass

if __name__ == "__main__":
    main()


# BROUILLON,  TENTATIVE D'AJOUTER UN SPRITE A LA POSITION DE ITEM
# IT WORKS, BUT NO CONTROL ON SPRITE TO GO OFF THE SCREEN ONCE HERO GO OVER
        #self.box = pg.image.load(BOX).convert_alpha() # to represent a box where items are hidden
        #self.items2 = pg.image.load(ETHER_PATH).convert_alpha()
        #self.items3 = pg.image.load(TUBE_PATH).convert_alpha()
        
        #for items in self.gameboard.items:
        #    self.background.blit(self.box,(items.x*SPRITE_WIDTH, items.y*SPRITE_HEIGHT))
        #   self.background.blit(self.items2,(items.x*SPRITE_WIDTH, items.y*SPRITE_HEIGHT))
            #self.background.blit(self.items3,(items.x*SPRITE_WIDTH, items.y*SPRITE_HEIGHT))


        #for items in self.gameboard.items:
        #   if name == 'ether':
            #    self.background.blit(self.image,(items.x*SPRITE_WIDTH, items.y*SPRITE_HEIGHT))
            #elif name == "tube":
            #    self.background.blit(self.image,(items.x*SPRITE_WIDTH, items.y*SPRITE_HEIGHT))
            #elif name == "needle":
            #   self.background.blit(self.image,(items.x*SPRITE_WIDTH, items.y*SPRITE_HEIGHT))



#self.gameboard = GameBoard()
#self.position = self.gameboard.items
#self.gameboard.items = self



#position = Position(self.rect.x, self.rect.y)
#if position in self.gameboard.items:
#    self.rect = self.background.blit(self.image, (self.rect.x, self.rect.y))
#else:
#    self.rect = self.background.blit(self.image, (450, 450))

##position = self.item.position(self.rect.x, self.rect.y)
#position = self.gameboard.items.position(self.rect.x, self.rect.y)

#if position in self.gameboard.items:
#    self.rect = self.background.blit(self.image, (self.rect.x, self.rect.y))
#else:
#    self.rect = self.background.blit(self.image, (450, 480))


#self.rect = pg.rect.Rect((self.rect.x, self.rect.y, SPRITE_WIDTH, SPRITE_HEIGHT)) 
        
        #pygame.rect.Rect((self.x, self.y, SPRITE_WIDTH, SPRITE_HEIGHT))
