""" this module will allow us to determine the length (and width) of the gameboard (map) """

from demo.position import Position

class GameBoard(set):
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
            #Pour chaque numéro de colonne(y), et colonne dans maze
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
            # on ajoute à width et lenght une colonne et ligne en '+'
            self.width = n_colonne +1
            self.length = n_lines +1


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
                elif pos in self.passages:
                    list_str.append(".")
                elif pos in self.walls:
                    list_str.append("W")
                    
            list_str.append("\n")

        return "".join(list_str)


    def __contains__(self, position):
        """ This methods keeps the HERO on the MAP horizontally, he can't go outside the map's length or width """
        
        return position in self.passages



    #def add_hero_on_map(self):
        # pas debesoin d'ajouter hero sur map. dans instance de notre hero : position déprt sur la position de depart de la map
        # on créer dans hero : attribut Poosition : positionner le héro sur la map --> fixer attibut positiond e notre hero sur gameboard.start
        
      #  """ this method is to insert the Hero into the map """



    #    if self.hero.position == self.start:
    #        return True

    #    if self.hero.position.mouvement == self.passages:
    #        return True 
        
     #   if self.hero.position == self.walls:
     #       return False
        
     #   if self.hero.position.mouvement == self.walls:
      #      return False 

    
    # hero in gameboard represented by "H"
    # if hero is in self.passages = True 
    # if hero is in self.walls = False
    # if hero mouvement in self.passages = True 
    # if hero mouvement in self.walls = False

        #initialize hero's position : at this position [0][0]
        #hero position : (maze[0][0])


#def main():
   # gameboard = GameBoard()
    #gameboard.load_from_file('maze1.py')
    #print(gameboard)


#if __name__ == "__main__":
   # main()

# )
#GameBoard créer un attribut qui est une liste de passage
#Dés qu'on rencontre un point, on rajoute les coordonnées de ce point dans la liste
#ce qui est # on ne l'ajoute pas 
#ce qui est . on l'ajoute 
#car . est un passage autorisé 
#tout ca dans GameBoard

#Adapter la méthode str pour afficher le labyrinthe

#Approprié de __contains__

#position est dans la liste des passages

#Adapter classe mouvement (x et y)


#Parcourir les lignes. Et colonnes d’un fichier 

# With open (map1.txt, « r ») as fichier:
# for n_ligne, ligne in enumerate(fichier): 
    #for n_colonne, colonne in enumerate(ligne): 
   # faire quelque chose avec les Position(n_colonne, n_ligne)
# fichier <- ouvrir le fichier


#with open(map1.txt, "r") as fichier:
 #   for n_ligne, ligne in enumerate(fichier):
 #      for n_colonne, colonne in enumerate(ligne):


# . = passage
# = mur 
#s = start
#e = end

#15 lignes de 15 caractères
#GameBoard créer un attribut qui est une liste de passage
#Dés qu'on rencontre un point, on rajoute les coordonnées de ce point dans la liste
#ce qui est # on ne l'ajoute pas 
#ce qui est . on l'ajoute 
#car . est un passage autorisé 
#tout ca dans GameBoard

#Adapter la méthode str pour afficher le labyrinthe

#Approprié de __contains__
#position est dans la liste des passages
#Adapter classe mouvement (x et y)