""" 
This module will represent all different tools that McGaver
can pick up in the maze.
The items will have random positions on the self.passages of the labyrinth,
the items will dispear from the map and appear in the inventory of 
Mcgaver,
Mcgavers (hero) should obtain a way to pick up and save up thos items 
"""

import random



class Items:

    """ this class will create objects that will represent the items for the hero
    on the gameboard to pick-up,
    those items are going to be positionned randomly on self.gameboard.passages 
    with the help of the module random (to import) """

    def __init__(self):
        """ construit un objet item de la classes Items """
        self.items = ""
        self.position = None

needle = Items()

ether = Items()

tube = Items()



    #def sample(self): PUT IT IN GAMEBOARD PERHAPS 
        # On créer une liste 'random_position' vide

        #random_position = []
        # on utilise la fonction random.sample(population qui est une séquence donc self.passages, k=3 on tire 3 positions)
        ##random_position = []
        #random.sample(self.passages, k=3)
        ##gameboard.load_from_file()


        #importer GameBoard dans ce module

        

       # on tire 3 positions dans self.passages

        #random.sample(self.passages, k=3)