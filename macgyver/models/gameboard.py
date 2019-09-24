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
    """ This class represents the gameboard and its
    different parameters (length, width)"""

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
        """ loads map from a file, specific characters, understand and remembers each position """
        
        # Donnons à nos attributs une valeurs en integers, car initialement elles ont None en valeur
        # Nous allons charger le labyrinthe en fichier texte se situant dans /levels/..., on créer la varible f pour la méthode
            # on décide de strip notre ligne de texte du fichier f pour créer un index pour chaque caractère présent
            # on demande ensuite au programme de lire notre texte : ligne par ligne et de la transformer en liste.
            # on isole cette méthode dans la variable maze, qui est au final une liste 
            
#/Users/jonathanreveille/dev/labyrinth/maze2.2.1./macgyver/demo/gameboard.py
        #with open('levels/maze1.txt') as f:
        #with open('/Users/jonathanreveille/dev/labyrinth/maze2.2.1./macgyver/demo/levels/maze1.txt') as f:
        with open(MAZE_LVL1) as f:
            maze = [line.strip("") for line in f.readlines() if line.strip()]
            maze = list(maze)
        
        for n_lines,lines in enumerate(maze): #Pour chaque numéro de ligne(x), et les lignes dans maze
            for n_colonne, colonne in enumerate(lines): #Pour chaque numéro de colonne(y), et colonne dans ligne
                
                pos = Position(n_colonne, n_lines) # on sauve dans 'pos' nos positions x et y selon le caractère rencontré dans notre fichier maze
                #if colonne  == ".":
                if colonne  == PASSAGES_CHAR: # Si nous avons dans colonne le caractere egale a ".", ajoute-le dans la liste self.passages
                    self.passages.append(pos)                    
                
                elif colonne == START_CHAR: # Si nous avons dans colonne le caractere egale a "S",  ajoute-le dans la liste self.passages
                    self.passages.append(pos)
                    self.start = pos
                
                elif colonne == GUARD_CHAR: # Si nous avons dans colonne le caractere egale a "G",  ajoute-le dans la liste self.passages
                    self.passages.append(pos)
                    self.goal = pos
                
                elif colonne == WALL_CHAR: # Si nous avons dans colonne le caractere egale a "W",  ajoute-le dans la liste self.walls
                    self.walls.append(pos)

            # on ajoute à width le nombre de colonne +1, ainsi que pour length on ajoute le nombre de n_lines +1 
            self.width = n_colonne +1
            self.length = n_lines +1

        #self.random = random.sample(self.passages, k=len(self.passages))
        #self.random : on tire 3 positions

        self.random = random.sample(self.passages, k=len(self.passages))
        
        #TEST
        #print(self.passages)
        #print(self.walls)
        #print(self.random)
        
        #random item positions created here
        #values =["Neddle","Tube", "Ether"] #name of the items
        #self.items = dict(zip(self.random, values))  # creating a dictionnary, key (position) and value (name)
  
        #self.random = random.sample(self.passages, k =len(self.passages)) # initiale et fonctionne, mais on ne connait pas quel Item est quel item
        #self.random = dict(zip(random.sample(["NEEDLE", "TUBE", "ETHER"], self.passages, k =len(self.passages)))


    def __str__(self):
        """ method that returns a string of the map """

        list_str = []

        for line in range(self.length):
            for colonne in range(self.width):
                pos = Position(colonne, line)
                # Verifier si c'est la position de McGaver
                if pos == self.hero.position:
                    list_str.append(HERO_CHAR)
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
                     
            list_str.append("\n") # ajoute un saut de ligne à chaque fin de ligne

        return "".join(list_str)


    def add_items(self, item):
        """ method that adds item on the map """
       
        item.position = self.random.pop()

        self.items[item.position] = item #ça nous met l'instance d'item  dans position

        return self.items # New line

    
    def __contains__(self, position):
        """ This methods keeps the HERO on the MAP horizontally and vertically, 
        he can't go outside the map's length or width """
        return position in self.passages



def main():
    g = GameBoard()
    g.load_from_file()

if __name__ == "__main__":
    main()
