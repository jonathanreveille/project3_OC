#! /usr/bin/env python3
# coding : utf-8 

""" This module is the main program to run the game """

from macgyver.demo.gameboard import GameBoard
from macgyver.demo.hero import Hero
from macgyver.demo.gamewon import GameWon
from macgyver.demo.mouvement import left, right, up, down
from macgyver.demo.items import Item, N, E, T
from macgyver.demo.gameover import GameOver


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

    except GameWon as e:
        print(e)
    except GameOver as ko:
        print(ko)
    

if __name__ == "__main__":
    main()
