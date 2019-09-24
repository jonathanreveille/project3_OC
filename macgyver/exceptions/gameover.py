#! /usr/bin/env python3
# coding : utf-8 

""" This module was created to allow pop up the message 
GameOver once the hero has reached the exit of the maze, but does not have 3 items """

class GameOver(Exception):
    """method that shows us when the hero does not have 3 items to build the seringue"""
    pass


def main():
    print("You are in gameover.py")
    
if __name__ == "__main__":
    main()
