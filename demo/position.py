""" This module allows us to know on which position our hero is standing. It will help
the module mouvement to calculate its itinary """

from demo.mouvement import Mouvement

class Position(list):
    """ This class will define where the hero is on the map with the coordinates (x,y) """


    def __init__(self, x, y):
        """ Construtor, x and y position has (x,y) """
        self.x = x
        self.y = y


    def __str__(self):
        """ This method returns with a string the position of our hero """
        return f"Position({self.x},{self.y})"


    def __add__(self, mouvement):
        """ This methods calculates the x position after the mouvement,  """
       
        if self.x != self.x + mouvement.dx:
            return Position((self.x + mouvement.dx), self.y)
        elif self.y != self.y + mouvement.dy:
            return Position(self.x, (self.y + mouvement.dy))

       #return Position(self.x, (self.y + mouvement.dy)) and Position((self.x + mouvement.dx), self.y)

    def __eq__(self, other):
        """ method to test matching between 2 positions """
        return self.x == other.x and self.y == other.y