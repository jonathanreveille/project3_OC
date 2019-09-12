#! /usr/bin/env python3
# coding : utf-8 
""" Module for pygame interface"""


import os
import pygame as pg
from config.settings import HERO, WIDTH, HEIGHT, BACKGROUND, VELOCITY, GUARD
from macgyver.views.needle import Needle
from macgyver.views.tube import Tube
from macgyver.views.ether import Ether
from macgyver.views.macgyver import MacGyver
from macgyver.views.guard import Guard

from macgyver.demo.gameboard import GameBoard

class Game:

    """ Class that represents the game for pygame"""

    def __init__(self): 
        """ All elements that are needed for the game"""

        # Initializer pygame
        pg.init() 
        
        #On définit la taille de l'écran
        self.screen = pg.display.set_mode((WIDTH, HEIGHT)) #Building the window in pixels
        
        #On définit l'image sur background
        self.background = pg.image.load(BACKGROUND).convert_alpha() #Building the background
    
        #On colle le background sur la taille du screen
        self.screen.blit(self.background, (0,0), self.screen.get_rect())# Putting the background on the screen surface with blit(). On vient de copier le background sur la surface. Blit veut dire : copier une image sur une surface (self.screen ci-dessus dans notre cas)
    
        #SPRITES
        #On créér une méthode dans un attribut qui ajoute et update les sprites qui bougent
        self.sprites = pg.sprite.RenderUpdates()

        self.sprites.add(MacGyver())
        self.sprites.add(Tube())
        self.sprites.add(Ether())
        self.sprites.add(Needle())
        self.sprites.add(Guard())
        
        #self.sprites.add(Wall())

        #self.screen.blit(self.tube,(150,90), self.screen.get_rect())
              
        #self.ether = Ether() 
        #self.screen.blit(self.ether,(420,90), self.screen.get_rect())
        
        
        #self.needle = Needle()
        #self.screen.blit(self.needle,(300,300), self.screen.get_rect())
        #self.screen.blit(self.needle.image,(self.gameboard.random), self.screen.get_rect())

        
        #we always update
        pg.display.update() 

        #the switch ON/OFF
        self.running = False  #to know if game runs or not in our while loop, we will use boolean values T or F

        #Title on screen
        pg.display.set_caption("MacGyver's Mad Escape")

        #for self.walls in self.gameboard:
            #faire un blit() sur le background
            #tout ce qui ne bouge pas, on peut le "bliter" dans background

#ADD A  LOAD_IMAGE FUNCTION HERE
#INITIALIZES IT IN __init__ 
#18:21 MERCREDI = AJOUTER LES OBJETS dans le package VIEWS


    def start(self): # method to launch the game
        """Method that launches the game"""

        clock = pg.time.Clock()
        self.running = True
       
        # loop for game launch
        while self.running:

            clock.tick(30)
            
            self._process_quit_events() #process de fermeture  de l'écran de jeu

            #1. Couvrir l'espace de jeu avec le background
            self.sprites.clear(self.screen, self.background) #  on clear notre self.screen, et on pause le bg par dessus
            
            #2. Appeler  la update sur toute  les sprites
            self.sprites.update()
            
            #3. Redessiner  ce qui doit l'être
            updated_sprites = self.sprites.draw(self.screen)
            
            pg.display.update(updated_sprites)



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
