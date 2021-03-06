#! /usr/bin/env python3
# coding : utf-8

""" This module will allow us to determine the length
 (and width) of the gameboard (map) """

import random
from config import settings
from macgyver.models.position import Position


class GameBoard:
    """ This class represents the gameboard and all its components"""

    def __init__(self):

        self.length = None
        self.height = None
        self.hero = None
        self.start = None
        self.goal = None
        self.passages = []
        self.walls = []
        self.maze = []
        self.items = {}
        self.random = None
        # We open the file with the method open()
        # Create a variable name maze
        # We decide to strip our lines in the text file 'f'
        # to create an index for each characters
        # Then, we read the lines : line by line and transform into a list

    def load_from_file(self):
        """ Loads map from a file, specific characters,understand and
        remembers each position """

        with open(settings.MAZE_LVL1) as f:
            maze = [line.strip("") for line in f.readlines() if line.strip()]
            maze = list(maze)

        # For each number of lines and lines in the maze
        for n_lines, lines in enumerate(maze):
            # For each number of colums and colums in the maze
            for n_column, column in enumerate(lines):

                # We save our positions with
                # pos variable as (x,y) for each characters
                pos = Position(n_column, n_lines)

                # if we have the '.', add the position into self.passages list:
                if column == settings.PASSAGES_CHAR:
                    self.passages.append(pos)

                # if we have the 'S', add the position into self.passages list:
                elif column == settings.START_CHAR:
                    self.passages.append(pos)
                    self.start = pos  # add position of 'S' to self.start

                # if we have the 'G', add the position into self.passages list:
                elif column == settings.GUARD_CHAR:
                    self.passages.append(pos)
                    self.goal = pos  # add the position of 'G' to self.goal

                elif column == settings.WALL_CHAR:
                    self.walls.append(pos)
            # We add to self.height = +1 to n_colums
            self.height = n_column + 1
            # We add to self.length +1 to n_lines
            self.length = n_lines + 1

        # function to select random position from self.passages
        self.random = random.sample(self.passages, k=len(self.passages))

    def __str__(self):
        """ Method that returns a string of the map """

        list_str = []
        for line in range(self.length):
            for column in range(self.height):
                pos = Position(column, line)

                # Check if the position is the one of the hero
                if pos == self.hero.position:
                    list_str.append(settings.HERO_CHAR)
                elif pos == self.start:
                    list_str.append(settings.START_CHAR)
                elif pos == self.goal:
                    list_str.append(settings.GUARD_CHAR)
                elif pos in self.items:
                    list_str.append(str(self.items[pos]))
                elif pos in self.passages:
                    list_str.append(settings.PASSAGES_CHAR)
                elif pos in self.walls:
                    list_str.append(settings.WALL_CHAR)

            # Go back at the line at the end of each line
            list_str.append("\n")

        return "".join(list_str)  # reassamble everything

    def add_items(self, item):
        """ Method that adds item on the maze passages randomly """

        # selects a position out of the list and deletes it
        item.position = self.random.pop()
        # it gives us the instance of item in Position
        self.items[item.position] = item
        return self.items

    def __contains__(self, position):
        """ This methods keeps the HERO in the MAP"""
        return position in self.passages


def main():
    g = GameBoard()
    g.load_from_file()


if __name__ == "__main__":
    main()
