#! /usr/bin/env python3
# coding : utf-8 

""" this module will allow us to determine the length (and width) of the gameboard (map) """

from random import sample
from demo.position import Position
from demo.items import Item
import random


class GameBoard():
    """ This class represents the gameboard and its
    different parameters (length, width)"""

    def __init__(self):

        self.length= None
        self.width = None
        self.start = None
        self.goal = None
        self.passages = []
        self.walls = []
        self.maze = []
        self.hero = None

        self.items = []
        self.random_pos= []


    def load_from_file(self):
        """ This method will load map from a file """
        
        # donnons à nos attributs une valeurs en integers, car initialement elles ont None en valeur
        # cette valeurs en integers permettra au programme de comprendre le nombre de ligne et de colonne
        self.width = int()
        self.length = int()

        #Nous allons charger le labyrinthe en fichier texte se situant dans /levels/..., on créer la varible f pour la méthode
            # on décide de strip notre ligne de texte du fichier f pour créer un index pour chaque caractère présent
            # on demande ensuite au programme de lire notre texte : ligne par ligne et de la transformer en liste.
            # on isole cette méthode dans la variable maze, qui est au final une liste      
        with open('levels/maze1.txt') as f:
            maze = [line.strip("") for line in f.readlines() if line.strip()]
            maze = list(maze)
        #Pour chaque numéro de ligne(x), et ligne dans maze
            #Pour chaque numéro de colonne(y), et colonne dans ligne
        for n_lines,lines in enumerate(maze):
            for n_colonne, colonne in enumerate(lines):
                # on sauve dans 'pos' nos positions x et y selon le caractère rencontré dans notre fichier maze
                pos = Position(n_colonne, n_lines)
                # Si nous avons dans colonne le caractere egale a ".", ajoute-le dans la liste self.passages
                if colonne  == ".":
                    self.passages.append(pos)                    
                # Si nous avons dans colonne le caractere egale a "S",  ajoute-le dans la liste self.passages
                if colonne == "S":
                    self.passages.append(pos)
                    self.start = pos
                # Si nous avons dans colonne le caractere egale a "G",  ajoute-le dans la liste self.passages
                if colonne == "G":
                    self.passages.append(pos)
                    self.goal = pos
                # Si nous avons dans colonne le caractere egale a "W",  ajoute-le dans la liste self.walls
                elif colonne == "W" : #It's a wall
                    self.walls.append(pos)

                   # self.random_pos = sample(self.passages, k=3)
                    #self.passages.append(self.random_pos)
            
            # on ajoute à width le nombre de colonne +1, ainsi que pour length on ajoute le nombre de n_lines +1 
            self.width = n_colonne +1
            self.length = n_lines +1

        self.random = random.sample(self.passages, k=len(self.passages))


    def __str__(self):
        """ method that returns a string of the maze map """

       #with open('levels/maze1.txt') as f:
            # self.maze = [line.strip("") for line in f.readlines() if line.strip()]  ONLY in LOAD_FROM_FILE

        list_str = []

        for line in range(self.length):
            for colonne in range(self.width):
                pos = Position(colonne, line)
                # Verifier si c'est la position de McGaver
                if pos == self.hero.position:
                    list_str.append("H")
                elif pos == self.start:
                    list_str.append("S")
                elif pos == self.goal:
                    list_str.append("G")
                elif pos in self.items:
                    list_str.append("I")
                elif pos in self.passages:
                    list_str.append(".")
                elif pos in self.walls:
                    list_str.append("W")
                     
            list_str.append("\n")

        return "".join(list_str)


    def add_items(self, item):
        """ method that adds item on the map """
       
        item.position = self.random.pop()

        self.items.append(item)


    def __contains__(self, position):
        """ This methods keeps the HERO on the MAP horizontally, he can't go outside the map's length or width """
        
        return position in self.passages

        # faire vérification pour voir si cette position existe dans liste I
        # liste WALL, LIste passages, Liste Items 
        # True or False

        # Si oui, on ajoute dans inventaire
        # on supprime de la liste I 
        # Si c'est dans la liste I on supprime la position dans I et on la rajoute dans passage
        # liste passage on ajoute la position
        # on enregistre dans notre inventaire qu'on enregistre sur I


#def main():
   # gameboard = GameBoard()
    #gameboard.load_from_file('maze1.py')
    #print(gameboard)


#if __name__ == "__main__":
   # main()
