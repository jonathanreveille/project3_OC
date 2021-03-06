#! /usr/bin/env python3
# coding : utf-8

""" This module will allows the programm to move
our hero from one case to the other one """


class Mouvement:
    """ This class will calculate how our hero will move from 1 spot
    to the next one. We will only change dx for x and dy for y """

    def __init__(self, dx, dy):
        """Constructor for Mouvement Class"""
        self.dx = dx
        self.dy = dy


# if our hero goes LEFT,
# we will decrease x by 1 - this is the object to go left.
left = Mouvement(dx=-1, dy=0)

# if our hero goes RIGHT,
# we will increase x by 1 - this is the object to go right.
right = Mouvement(dx=+1, dy=0)

# if our hero goes UP,
# we will decrease y by 1 - this is the object to up.
up = Mouvement(dx=0, dy=-1)

# if our hero goes DOWN,
# we will increase y by 1 - this is the object to down.
down = Mouvement(dx=0, dy=+1)


def main():
    pass


if __name__ == "__main__":
    main()
