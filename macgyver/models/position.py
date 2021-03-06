#! /usr/bin/env python3
# coding : utf-8

""" This module allows us to know on which position
our hero is standing. It will help the module mouvement
to calculate its itinary """


class Position:
    """ This class will define where the hero is on the
    map with the coordinates (x,y) """

    def __init__(self, x, y):
        """ Construtor, x and y position has (x,y) """
        self.x = x
        self.y = y

    def __repr__(self):
        """ Method that returns with a string
        the positions by x and y """
        return f"Position({self.x},{self.y})"

    def __add__(self, mouvement):
        """ Method that calculates the x or y
        position after the mouvement """
        if self.x != self.x + mouvement.dx:
            return Position((self.x + mouvement.dx), self.y)

        elif self.y != self.y + mouvement.dy:
            return Position(self.x, (self.y + mouvement.dy))

    def __eq__(self, obj):
        """ Method  to test if 2 positions are matching together """
        if not isinstance(obj, Position):
            position = obj.position
        else:
            position = obj
        return self.x == position.x and self.y == position.y

    def __hash__(self):
        """ hash method, return an Hash value of position x and y """
        return hash((self.x, self.y))


def main():
    pass


if __name__ == "__main__":
    main()
