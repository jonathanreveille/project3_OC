#! /usr/bin/env python3
# coding : utf-8 

""" This module allows us to represent our hero on the map, it will define many parameter such as ..."""

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
            

       # elif self.position == self.gameboard.goal and len(self.bag) != 3:
    #       raise GameOver("you must have forgotten an item ! try again...")


    #def win_game(self):
   # """method that checks if the length of self.bag is 3, if true :
    #raise GameWon (message)
   # false : raise GameLost (message) """
    #    
       # if len(self.bag) == 3:
        #    if True:
          #      raise GameWon("you made it Morty ! you have just killed the guard!")
          #  print("it should launch GameWon")
           # else:
           #     raise GameOver("you forgot an item on the map, you just died...try again")
            #    print("it shoudl launch GameLost")


       # """ Allows the hero to add items into his bag when he passes over it"""
#
 #      # new_position = self.position + travel

 #      # if new_position == self.gameboard.items:
 #   #     self.position = new_position
        #    #self.gameboard.items.remove('I')#([0])
  #      #    self.bag.append("I")
   #    #     print(self.bag)

  #          #self.gameboard.items.remove('I') # that is the one to keep, but AttributeError occurs
  #          #self.gameboard.items.pop(0)
  #          #del self.gameboard.items[0]
  #          #self.bag.append("I")

        #    raise GameWon ("you made it Morty ! you have just killed theguard!"
            #if  len(self.bag)==3:
                #raise GameWon("you made it Morty ! you have just killed theguard!")
            #else:
                #raise GameOver("you forgot an item on the map, you just died...try again")

       # elif len(self.bag)== 3 and new_position in self.gameboard.goal:
        #)

        #else:
        #    raise GameOver(
                #"you forgot an item on the map, you just died...try again"
                #)

