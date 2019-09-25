#! /usr/bin/env python3
# coding : utf-8 

""" this module will allow us to determine the length (and width) of the gameboard (map) """

import os
import random
from random import sample

from config.settings import MAZE_LVL1, START_CHAR, GUARD_CHAR, WALL_CHAR, PASSAGES_CHAR, HERO_CHAR
from macgyver.models.position import Position
from macgyver.models.items import Item


class GameBoard:
    """ This class represents the gameboard and all its components"""

    def __init__(self):

        self.length= None
        self.width = None
        self.hero = None
        self.start = None
        self.goal = None
        self.passages = []
        self.walls = []
        self.maze = []
        self.items = {}
        self.random= None


    def load_from_file(self):
        """ Loads map from a file, specific characters, understand and 
        remembers each position """
        
            # We open the file with the method open()
            # Create a variable name maze
            # We decide to strip our lines in the text file 'f' to create an index for each characters
            # Then, we read the lines : line by line and transform into a list
            
        with open(MAZE_LVL1) as f:
            maze = [line.strip("") for line in f.readlines() if line.strip()]
            maze = list(maze)
        
        for n_lines,lines in enumerate(maze): #For each number of lines and lines in the maze
            for n_colonne, colonne in enumerate(lines): #For each number of colums and colums in the maze

                pos = Position(n_colonne, n_lines)  # We save our positions with pos variable as (x,y) for each characters
                
                if colonne  == PASSAGES_CHAR:       #if we have the '.', add the position into self.passages list:
                    self.passages.append(pos)                    
                
                elif colonne == START_CHAR:         # if we have the 'S', add the position into self.passages list:
                    self.passages.append(pos)
                    self.start = pos                #add position of 'S' to self.start
                
                elif colonne == GUARD_CHAR:         # if we have the 'G', add the position into self.passages list:
                    self.passages.append(pos)
                    self.goal = pos                 #add the position of 'G' to self.goal
                
                elif colonne == WALL_CHAR:          #if we have 'W':
                    self.walls.append(pos)          #add the position of 'W' to self.walls list

             
            self.width = n_colonne +1               # We add to self.width = +1 to n_colums
            self.length = n_lines +1                # We add to self.length +1 to n_lines

        self.random = random.sample(self.passages, k=len(self.passages)) #function to select random position from self.passages
        

    def __str__(self):
        """ Method that returns a string of the map """

        list_str = [] #empty list
        for line in range(self.length):
            for colonne in range(self.width):
                pos = Position(colonne, line)
                
                if pos == self.hero.position: # Check if the position is the one of the hero
                    list_str.append(HERO_CHAR) # Add to this list : the characters 'H'saved with pos in load_from_file():
                elif pos == self.start:
                    list_str.append(START_CHAR)
                elif pos == self.goal:
                    list_str.append(GUARD_CHAR)
                elif pos in self.items:
                    list_str.append(str(self.items[pos]))
                elif pos in self.passages:
                    list_str.append(PASSAGES_CHAR)
                elif pos in self.walls:
                    list_str.append(WALL_CHAR)
                     
            list_str.append("\n") # Go back at the line at the end of each line

        return "".join(list_str) #reassamble everything


    def add_items(self, item):
        """ Method that adds item on the maze passages randomly """
       
        item.position = self.random.pop() #selects a position out of the list and deletes it
        self.items[item.position] = item #it gives us the instance of item in Position
        return self.items

    
    def __contains__(self, position):
        """ This methods keeps the HERO in the MAP"""
        return position in self.passages



def main():
    g = GameBoard()
    g.load_from_file()

if __name__ == "__main__":
    main()
