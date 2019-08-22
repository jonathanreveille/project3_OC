#! /usr/bin/env python3
# coding : utf-8 

""" 
This module will represent all different tools that McGaver
can pick up in the maze.
The items will have random positions on the self.passages of the labyrinth,
the items will dispear from the map and appear in the inventory of 
Mcgaver,
Mcgavers (hero) should obtain a way to pick up and save up thos items 
"""

class Item:

    """ this class will create objects that will represent the items for the hero
    on the gameboard to pick-up,
    those items are going to be positionned randomly on self.gameboard.passages 
    with the help of the module random (to import) """

    def __init__(self, name):
        """ construit un objet item de la classes Items """
        self.name = name
        self.position = None
        self.x = None
        self.y = None
        

    def __repr__(self):
        #return f"Items(position={self.position})"
        return f"Items({self.x},{self.y})"


   # def __eq__(self, obj):
      #  """ method  to test if 2 positions are matching"""

      #  if isinstance(obj, Item):
      #      position = obj.position
      #  else:
       #     position = obj
       # return self.x == position.x and self.y == position.y

    def __eq__(self, obj):
        if not isinstance(obj, Item):
            self.position = obj
        else:
            self.position = obj.position
        return self.position == self.position

N = Item("needle")

E = Item("ether")

T = Item("tube")
