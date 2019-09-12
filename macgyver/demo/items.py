#! /usr/bin/env python3
# coding : utf-8 

""" This module will represent all different items on the map for McGaver"""

class Item:

    """ This class will create objects that are items in the game,
    those items are going to be positionned randomly on the map """

    def __init__(self, name):
        """ constructor for item Class objects"""
        self.name = name
        self.position = None


    def __repr__(self):
        """ method that allow us to see what data has an object from Item Class"""
        return f"Items(position={self.position},name= ({self.name})"


    def __str__(self):
        return self.name[0]


    def __eq__(self, obj):
        """ method to see if two positions are matching with each other"""
        if not isinstance(obj, Item):
            self.position = obj
        else:
            self.position = obj.position
        return self.position == self.position


N = Item("Needle")

E = Item("Ether")

T = Item("Tube")


def main():
    needle = Item('Needle')
    print(needle.name, needle.position)
    print(T.name, T.position)
    print(E.name, E.position)

if __name__ == "__main__":
    main()



   # def __eq__(self, obj):
      #  """ method  to test if 2 positions are matching"""

      #  if isinstance(obj, Item):
      #      position = obj.position
      #  else:
       #     position = obj
       # return self.x == position.x and self.y == position.y
