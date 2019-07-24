""" This module allows us to represent our hero on the map, it will define many parameter such as ..."""

from demo.position import Position
from demo.mouvement import Mouvement
from demo.gameboard import GameBoard
from demo.gamewon import GameWon
from demo.items import Item


class Hero:
    """ This class will define the position of 
    the hero at start position,
    then on the gameboard,
    and where the hero stands on the gameboard"""

    def __init__(self, gameboard):
       
        self.position = gameboard.start
        self.gameboard = gameboard
        self.gameboard.hero = self
        self.items = []
        

    def move(self, travel):
        """ Method that allows our hero to move on the map from its position to a new position """
        
        new_position = self.position + travel

        if new_position in self.gameboard:
            self.position = new_position

        if self.position == self.gameboard.goal:
            raise GameWon ("you made it!")

        # maybe add here the method to pick up weapons 


    #WORKING HERE NOW
    def store_items(self):
        """ method where the hero can keep his items """
        # hero's inventory. If hero's inventory == 3: 
        # raise 'You just build a weapon'

        # creating empty list to take in the items when hero finds it in labyrinth
        self.items = []
        # compteur while loop
        i = 0
        while i <= 3: # because only 3 items
            #if hero's position is on self.items.position in self.gameboard.passages:
            if self.position == self.items in self.gameboard.passages:
                # add self.items to the list
                self.items.append(self.items)
                i += 1

        #if bag != len(2) is False:

        #if self.position == 
