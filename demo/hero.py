""" This module allows us to represent our hero on the map, it will define many parameter such as ..."""

from demo.position import Position
from demo.mouvement import Mouvement
from demo.gameboard import GameBoard
from demo.gamewon import GameWon


class Hero:
    """ This class will define the position of 
    the hero at start position,
    then his mouvement,
    and where he stands after his mouvement on the map """

    def __init__(self, gameboard):
       
        self.position = gameboard.start
        self.gameboard = gameboard
        self.gameboard.hero = self
        

    def move(self, travel):
        """ method allows our hero to move on the map """
        
        new_position = self.position + travel
        if new_position in self.gameboard:
            self.position = new_position


    def found_goal(self): # if hero stands on exit/goal
        """ Method that checks if hero is on position gameboard.goal, if TRUE,
        raise GameWon Exception 'you won !' . """

        if self.position == self.gameboard.goal:
            raise GameWon ("You made it, congrats !!")
      