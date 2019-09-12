#! /usr/bin/env python3
# coding : utf-8 

""" this class will make the view (graphics) of the maze """

import pygame as pg

class Labyrinth(pg.sprite.Sprite):
    def __init__(self):
        self.image = None
        self.rect = None


class LabyrinthView:
    pass