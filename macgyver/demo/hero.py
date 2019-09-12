#! /usr/bin/env python3
# coding : utf-8 

""" This module allows us to represent our hero on the map, it will define many parameter such as ..."""

from macgyver.demo.mouvement import Mouvement
from macgyver.demo.gameboard import GameBoard
from macgyver.demo.gamewon import GameWon
from macgyver.demo.items import Item
from macgyver.demo.gameover import GameOver

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

        if new_position in self.gameboard.passages:
            self.position = new_position

            if new_position in self.gameboard.items:
                self.add_to_bag()

            elif new_position == self.gameboard.goal:
                self.level_achieved()


    def add_to_bag(self):
        """method that allows you to take the item from gameboard, and put it into our bag"""
        
        item = self.gameboard.items[self.position]
        del self.gameboard.items[self.position]
        self.bag.append(item)
        print(self.bag)
        return ("you just found an item")


    def level_achieved(self):
        """check if the hero has 3 items to win the game """

        if len(self.bag) != 3:
            raise GameOver("you must have forgotten an item ! try again...")
        else:
            raise GameWon("you made it McGaver! freedom")
            

def main():
    pass

if __name__ == "__main__":
    main()
