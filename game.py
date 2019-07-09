""" This module is the main program to run the game """

from demo.gameboard import GameBoard
from demo.hero import Hero
from demo.gamewon import GameWon
from demo.mouvement import left, right, up, down

def main():
    gameboard = GameBoard()
    gameboard.load_from_file()
    hero = Hero(gameboard)

    user = ""

    while True:
        try:
            while user != "quit":
                print(gameboard)
                
                travel = input("Where do you want hero to go (right/left/up/down/quit)?  ")
                if travel in ('left', 'right', 'up', 'down'):
                    hero.move(globals()[travel])
                

        except GameWon as e:
            print(e)
    

main()