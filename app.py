#! /usr/bin/env python3
# coding : utf-8

""" This module is the main program to run the game """

from macgyver.models.gameboard import GameBoard
from macgyver.models.hero import Hero
from macgyver.models import mouvement  # movement
from macgyver.models.items import N, E, T
from macgyver.exceptions.gamewon import GameWon
from macgyver.exceptions.gameover import GameOver


def main():
    """this is the main to launch the game"""
    gameboard = GameBoard()
    gameboard.load_from_file()
    gameboard.add_items(N)
    gameboard.add_items(E)
    gameboard.add_items(T)
    hero = Hero(gameboard)

    user = ""

    try:

        while user != "quit":  # loop
            print(gameboard)  # show us the maze, with (__str__) from gameboard

            # Ask user a value in string of the desired direction
            travel = input(
                "Where do you want hero to go (right/left/up/down/quit)? ")

            if travel in ('left', 'right', 'up', 'down'):
                hero.move(getattr(mouvement, travel))

    except GameWon as e:  # if won
        print(e)  # show message

    except GameOver as ko:  # if lost
        print(ko)  # show message


if __name__ == "__main__":
    main()
