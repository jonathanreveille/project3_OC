#! /usr/bin/env python3
# coding : utf-8 

""" This module is the main program to run the game """

from macgyver.models.gameboard import GameBoard
from macgyver.models.hero import Hero
from macgyver.models.mouvement import left, right, up, down
from macgyver.models.items import Item, N, E, T
from macgyver.exceptions.gamewon import GameWon
from macgyver.exceptions.gameover import GameOver


def main():

    gameboard = GameBoard()
    gameboard.load_from_file()
    gameboard.add_items(N)
    gameboard.add_items(E)
    gameboard.add_items(T)
    hero = Hero(gameboard)

    user = ""

    try:
        
        while user != "quit":
            print(gameboard) # affichage
            
            #Ask user a value in string of the desired direction
            travel = input("Where do you want hero to go (right/left/up/down/quit)? ")

            if travel in ('left', 'right', 'up', 'down'):
                hero.move(globals()[travel])

    except GameWon as e: #if won
        print(e)
    except GameOver as ko: #if lost
        print(ko)
    

if __name__ == "__main__":
    main()
