""" This module allows us to represent our hero on the map, it will define many parameter such as ..."""

from demo.position import Position
from demo.mouvement import Mouvement
from demo.gameboard import GameBoard
from demo.gamewon import GameWon


class Hero:
    """ This class will define the position of 
    the hero at start position,
    then on the gameboard,
    and where the hero stands on the gameboard"""

    def __init__(self, gameboard):
       
        self.position = gameboard.start
        self.gameboard = gameboard
        self.gameboard.hero = self
        

    def move(self, travel):
        """ Method that allows our hero to move on the map from its position to a new position """
        
        new_position = self.position + travel

        if new_position in self.gameboard:
            self.position = new_position

        if self.position == self.gameboard.goal:
            raise GameWon ("you made it!")

 # WORKING HERE FOR NOW
    #def found_goal(self): # if hero stands on exit/goal
      #  """ Method that checks if the hero is on the position gameboard.goal, 
      #  if TRUE, raise GameWon Exception 'you won !' """
       


        #try:
           # if self.position != self.gameboard.passages:
            #    pass
            #elif self.position != self.gameboard.start:
            #    pass
        #except self.position == self.gameboard.goal:
                #raise GameWon ("Well Done, you made it alive !")


        #if self.position == self.gameboard.goal:
            #raise GameWonhygf ("You won ! There you go buddy")
        # does not work yet... 
        