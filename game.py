#! /usr/bin/env python3
# coding : utf-8 

""" This module is the main program to run the game """

from demo.gameboard import GameBoard
from demo.hero import Hero
from demo.gamewon import GameWon
from demo.mouvement import left, right, up, down
from demo.items import Item, N, E, T
from demo.gameover import GameOver

def main():
    
    gameboard = GameBoard()
    gameboard.load_from_file()
    gameboard.add_items(N)
    gameboard.add_items(E)
    gameboard.add_items(T)
    hero = Hero(gameboard)

    user = ""

    while True:

        try:
            while user != "quit":
                print(gameboard)
                
                #Ask user a value in string of the desired direction
                travel = input("Where do you want hero to go (right/left/up/down/quit)? ")

                if travel in ('left', 'right', 'up', 'down'):
                    hero.move(globals()[travel])

        except GameWon as e:
            print(e)
        except GameOver as ko:
            print(ko)
            break
    

main()