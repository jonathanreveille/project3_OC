#! /usr/bin/env python3
# coding : utf-8 
""" Module for pygame interface"""


import pygame as pg
from config.settings import HERO, WIDTH, HEIGHT, BACKGROUND, VELOCITY, GUARD, WALL, SPRITE_HEIGHT, SPRITE_WIDTH, ETHER_PATH, TUBE_PATH, NEEDLE_PATH, PASSAGES, BOX
from macgyver.views.items import Items
from macgyver.views.macgyver import MacGyver
from macgyver.views.walls import Walls
from macgyver.views.guard import Guard
from macgyver.demo.gameboard import GameBoard
from macgyver.demo.hero import Hero
from macgyver.demo.items import Item, N, E, T

class Game:
    """ Class that represents the game for pygame"""

    def __init__(self): 
        """ All elements that are needed for the game"""

        self.gameboard = GameBoard()
        self.gameboard.load_from_file()
        self.hero = Hero(self.gameboard)
        self.tube = Item("Tube")
        self.ether = Item("Ether")
        self.needle  = Item("Needle")

        self.gameboard.add_items(self.tube) #from class in gameboard.py in models
        self.gameboard.add_items(self.ether) #from class in gameboard.py in models
        self.gameboard.add_items(self.needle) #from class in gameboard.py in models

        # Initializer pygame
        pg.init()
        #Title on screen
        pg.display.set_caption("MacGyver's Mad Escape")

        #On définit la taille de l'écran
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        #On définit l'image sur background
        self.background = pg.image.load(BACKGROUND).convert_alpha()

        #1- on charge l'image du wall
        #2- on ajoute les murs de gameboard.walls au background
        #3- on colle le background (avec les murs inclus) sur la taille du screen

        #Adding images of wall to walls..
        self.wall = pg.image.load(WALL).convert() 
        for wall in self.gameboard.walls:
            self.background.blit(self.wall, (wall.x*SPRITE_WIDTH, wall.y*SPRITE_HEIGHT))

        #Adding images of passage to passages...
        self.passages = pg.image.load(PASSAGES).convert()
        for passages in self.gameboard.passages:
            self.background.blit(self.passages,(passages.x*SPRITE_WIDTH, passages.y*SPRITE_HEIGHT))

        #Adding images of boxes instead of items for now...
        self.box = pg.image.load(BOX).convert_alpha()
        for items in self.gameboard.items:
            self.background.blit(self.box,(items.x*SPRITE_WIDTH, items.y*SPRITE_HEIGHT))

        #Putting the background on the screen surface with blit(). On vient de copier le background sur la surface. 
        #Blit veut dire : copier une image sur une surface (self.screen ci-dessus dans notre cas)
        self.screen.blit(self.background, (0,0), self.screen.get_rect())

        #SPRITES
        #On créér et on utilise une méthode pygame dans un attribut qui ajoute et update les sprites qui bougent
        self.sprites = pg.sprite.RenderUpdates() # nous permet de gérer nos diférentes sprites
        self.sprites.add(MacGyver(self.hero))
        self.sprites.add(Guard())

        self.sprites.add(Items(TUBE_PATH, self.tube))

        #we always update
        pg.display.update()

        #the switch ON/OFF
        self.running = False  #to know if game runs or not in our while loop, we will use boolean values T or F
 

    def start(self): # method to launch the game
        """Method that launches the game"""

        clock = pg.time.Clock()
        self.running = True
       
        # loop for game launch
        while self.running:

            clock.tick(40) #Frame per seconds, in order words : the speed of the loop
            
            self._process_quit_events() #process de fermeture  de l'écran de jeu

            #1. Couvrir l'espace de jeu avec le background
            self.sprites.clear(self.screen, self.background) #  on clear notre self.screen, et on pause le bg par dessus
            
            #2. Appeler  la update sur toute les sprites
            self.sprites.update() #appelle chacune des updates de chacune des classes sprites
            
            #3. Redessiner  ce qui doit l'être
            updated_sprites = self.sprites.draw(self.screen) #coller ou bliter les différentes images sur l'écran
            
            pg.display.update(updated_sprites) #retour la liste updater de sprites qui ont été modifié par rapprot au tour d'avant



    def _process_quit_events(self):
        """ method that quits the game when the user press the exit button on game window"""
        for _ in pg.event.get(pg.QUIT):
            self.running = False



def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()



    #def load_image(self, name):
        #""" method to load image for game """
        
        #fullname = os.path.join('demo/image/bg.png')
        #try:
        #    image = pg.image.load(fullname)
        #except FileNotFoundError:
        #    print("Cannot load the image : ", name)
        #image = image.convert()
        #return image
        




            #for event in pg.event.get():
                #if event.type == QUIT:
                #    self.running = False

            #    elif pg.event.type == pg.KEYDOWN and event.key == K_ESCAPE:
            #    self.running = False

            #    elif event.type == KEYDOWN and event.key == K_UP:
            #       hero.move()

            #   elif event.type == KEYDOWN and event.key == K_DOWN:
            #       hero.move()

                #elif event.type == KEYDOWN and event.key == K_LEFT:
                    #hero.move()

                #elif event.type == KEYDOWN and event.key == K_RIGHT:
                    #hero.move()
                
                #pg.display.update()





#1- It works, but no need anymore for now in def start from class Game :
        #self.running = True
        #while self.running:
            #pg.event.pump()

            #response = input('Do you want to quit the game?')
            #if response == "quit" or " quit":
                #self.running = False

#2- Following pygamechimp tutorial
#def main():
    #Example from the tutorial
    #Initialize everything
    #pg.init()
    #pg.display.set_mode((height,width))
    #pg.display.set_caption("McGaver")
    #pg.quit()


    #Create background
    #background = pygame.Surface(screen.get_size())  
    #background = background.convert()
    #background.fill((40,40,40)) # to choose black color for background, e.g. 255,255,255 would be white

    #Display the background
    #screen.blit(background,(0,0)) #blit veut dire 'coller' sur le screen & position (0,0) qui est en haut à gauche. Si on augmente x on va vers la droite, si on augmente y, on va vers le bas
    #pygame.display.flip() #mettre un jour l'écran, on peut aussi faire update pour mettre à jour l'affichage

    #Draw everything
    #screen.blit(background,(0, 0))
    #pygame.display.flip()

#CONVERT  
        #self.macgyver = pg.image.load(settings.HERO).convert() # .convert_alpha() : if MacGyver png file is already transparent, to make bg transparent
        #self.macgyver.set_colorkey(settings.COULEUR) Si je trouve une image jpeg du hero avec fond de couleur
        

#pg.display.FLIP() VS. pg.display.UPDATE()
#pg.display.flip() c'est une mise à jour de tout l'écran, un peu différent de update. Car quand on MOVE, c'est seulement une 
#case qui change. flip() me permet de mettre à jour toute la surface. Update rafraichi uniquement les mouvements

        
        # self.guard = pg.image.load(GUARD).convert_alpha()
        #self.background.blit(self.guard, self.guard*SPRITE_WIDTH, self.guard*SPRITE_HEIGHT)
        #for pos in self.gameboard.goal:
        #    self.background.blit(self.guard, (pos.x*SPRITE_WIDTH, pos.y*SPRITE_HEIGHT))
        
        #add guard image on gameboard.goal
        #self.gameboard.goal = pg.image.load(GUARD).convert_alpha()
        #self.guard = self.gameboard.goal
        #self.background.blit(self.guard, (300,400))
 
        #self.tube = pg.image.load(TUBE_PATH).convert_alpha()
        #for items in self.gameboard.items:
        #    self.background.blit(self.tube, (items.x*SPRITE_WIDTH, wall.y*SPRITE_HEIGHT))

        #self.ether = pg.image.load(ETHER_PATH).convert_alpha()
        #for items in self.gameboard.items:
        #    self.background.blit(self.ether, (items.x*SPRITE_WIDTH, wall.y*SPRITE_HEIGHT))

        #self.needle = pg.image.load(NEEDLE_PATH).convert_alpha()
        #for items in self.gameboard.items:
        #    self.background.blit(self.needle, (items.x*SPRITE_WIDTH, wall.y*SPRITE_HEIGHT))

