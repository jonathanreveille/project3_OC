#! /usr/bin/env python3
# coding : utf-8 

""" This module allows us to represent our hero on the map, it will define many parameter such as ..."""

from demo.position import Position
from demo.mouvement import Mouvement
from demo.gameboard import GameBoard
from demo.gamewon import GameWon
from demo.items import Item
from demo.gameover import GameOver

class Hero:
    """ This class will define the position of 
    the hero at start position,
    then on the gameboard,
    and where the hero stands on the gameboard"""

    def __init__(self, gameboard):
       
        self.position = gameboard.start
        self.gameboard = gameboard
        self.gameboard.hero = self
        self.bag = []
        

    def move(self, travel):
        """ Method that allows our hero to move on the map from its position to a new position """

        new_position = self.position + travel

        if new_position in self.gameboard.items:
            self.position = new_position
            
            self.gameboard.items.remove('I') # that is the one to keep, but AttributeError occurs
            self.bag.append("I")

            #del self.gameboard.items[0]
            #self.gameboard.items.pop() or remove("I")
            print(self.bag)

        elif new_position in self.gameboard.passages:
            self.position = new_position
        
        elif new_position in self.gameboard.walls:
            return self.position
        
        elif new_position in self.gameboard.goal:
            self.position = new_position
        
        elif self.position == self.gameboard.goal and len(self.bag)==3:
            raise GameWon ("you made it Morty ! you have just killed the guard!")

        else:
            raise GameOver ("you just died...try again")
