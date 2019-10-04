#! /usr/bin/env python3
# coding : utf-8
""" Module to load items into the game in graphic mode"""

import pygame as pg
from config.settings import SPRITE_WIDTH, SPRITE_HEIGHT


class ItemSprite(pg.sprite.Sprite):
    """ Class that will represents the sprites of our items in
    the maze """

    def __init__(self, image, item, gameboard):  # Constructor

        super().__init__()
        self.gameboard = gameboard
        self.item = item
        self.image = pg.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.item.position.x*SPRITE_WIDTH
        self.rect.y = self.item.position.y*SPRITE_HEIGHT

    def update(self):
        """ Method that updates IF the items is picked up or not"""

        if self.gameboard.hero.position == self.item.position:
            items = len(self.gameboard.hero.bag)
            self.rect.x = (items - 1) * SPRITE_WIDTH
            self.rect.y = self.gameboard.length * SPRITE_HEIGHT


def main():
    pass


if __name__ == "__main__":
    main()
