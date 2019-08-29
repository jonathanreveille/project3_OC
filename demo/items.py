#! /usr/bin/env python3
# coding : utf-8 

""" 
This module will represent all different items on the map for McGaver"""

class Item:

    """ This class will create objects that are items in the game,
    those items are going to be positionned randomly on the map """

    def __init__(self, name):
        """ constructor for item Class objects"""
        self.name = name
        self.position = None
        self.x = None
        self.y = None

    def __repr__(self):
        """ method that allow us to see what data has an object from Item Class"""
        return f"Items(position={self.x},{self.y},name= ({self.name})"

    def __eq__(self, obj):
        """ method to see if two positions are matching with each other"""
        if not isinstance(obj, Item):
            self.position = obj
        else:
            self.position = obj.position
        return self.position == self.position

#items_dict = dict(zip(['NEEDLE', 'TUBE', 'ETHER'], [1, 2, 3]))
#print(items_dict)

N = Item("needle")

E = Item("ether")

T = Item("tube")




   # def __eq__(self, obj):
      #  """ method  to test if 2 positions are matching"""

      #  if isinstance(obj, Item):
      #      position = obj.position
      #  else:
       #     position = obj
       # return self.x == position.x and self.y == position.y
