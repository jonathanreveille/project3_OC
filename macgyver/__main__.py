#! /usr/bin/env python3
# coding : utf-8 
""" Module for pygame interface"""

import pygame as pg

#from config.settings import settings
from config import settings #HERO, WIDTH, HEIGHT, BACKGROUND, VELOCITY, GUARD, WALL, SPRITE_HEIGHT, SPRITE_WIDTH, ETHER_PATH, TUBE_PATH, NEEDLE_PATH, PASSAGES, WON, LOST, INTRO
from macgyver.views.macgyver import MacGyver
from macgyver.views.items import ItemSprite
from macgyver.views.walls import Walls
from macgyver.views.guard import Guard
from macgyver.models.gameboard import GameBoard
from macgyver.models.hero import Hero
from macgyver.models.items import Item, N, E, T
from macgyver.exceptions.gamewon import GameWon
from macgyver.exceptions.gameover import GameOver


class Game:
    """ Class that represents the game for pygame"""

    def __init__(self): 
        """ All elements that are needed for the game"""

        self.gameboard = GameBoard()
        self.gameboard.load_from_file()
        self.gameboard.add_items(N)
        self.gameboard.add_items(E)
        self.gameboard.add_items(T)
        self.hero = Hero(self.gameboard)

        pg.init() # Initializer pygame
        
        pg.display.set_caption("MacGyver's Mad Escape") #Title on screen

        #1. On définit la taille de l'écran
        self.screen = pg.display.set_mode((settings.WIDTH, settings.HEIGHT))
        #2. On définit l'image sur background
        self.background = pg.image.load(settings.BACKGROUND).convert_alpha()

        self.lost = pg.image.load(settings.LOST).convert_alpha()
        self.won = pg.image.load(settings.WON).convert_alpha()

        #1- on charge l'image du wall
        #2- on ajoute les murs de gameboard.walls au background
        #3- on colle le background (avec les murs inclus) sur la taille du screen

        #Adding images of wall to walls.
        self.wall = pg.image.load(settings.WALL).convert_alpha() 
        for wall in self.gameboard.walls:
            self.background.blit(self.wall, (wall.x*settings.SPRITE_WIDTH, wall.y*settings.SPRITE_HEIGHT))

        #Adding images of passage to passages...
        self.passages = pg.image.load(settings.PASSAGES).convert_alpha()
        for passages in self.gameboard.passages:
            self.background.blit(self.passages,(passages.x* settings.SPRITE_WIDTH, passages.y* settings.SPRITE_HEIGHT))
  
        #Putting the background on the screen surface with blit(). On vient de copier le background sur la surface. 
        #Blit veut dire : copier une image sur une surface (self.screen ci-dessus dans notre cas)
        self.screen.blit(self.background, (0,0), self.screen.get_rect())

        #SPRITES
        #On créér et on utilise une méthode pygame dans un attribut qui ajoute et update les sprites qui bougent
        self.sprites = pg.sprite.RenderUpdates() # nous permet de gérer nos diférentes sprites
        self.sprites.add(MacGyver(self.hero))
        self.sprites.add(Guard())
        self.sprites.add(ItemSprite(settings.TUBE_PATH, T, self.gameboard))
        self.sprites.add(ItemSprite(settings.ETHER_PATH, E, self.gameboard))
        self.sprites.add(ItemSprite(settings.NEEDLE_PATH, N, self.gameboard))

        #self.sprites.add(Items(ETHER_PATH, self.gameboard))
        #self.sprites.add(Items(NEEDLE_PATH, self.gameboard))

        #Allows  the player to keep on pressing down the key and hero moves
        pg.key.set_repeat(500, 100)

        #we always update
        pg.display.update()

        #the switch ON/OFF
        self.running = False  #to know if game runs or not in our while loop, we will use boolean values T or F
 

    def start(self): # method to launch the game
        """Method that launches the game"""

        clock = pg.time.Clock()
        self.running = True
       
        # loop for game launch
        try:
            
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

        
        except GameWon as e:
            print(e)
            self.running = True
            self.display_message(self.won)


        except GameOver as e:
            print(e)
            self.running = True
            self.display_message(self.lost)


    def _process_quit_events(self):
        """ method that quits the game when the user press the exit button on game window"""
        for _ in pg.event.get(pg.QUIT):
            self.running = False


    def display_message(self, image):
        """ method to add a screen for GameOver or GameWon"""
        self.running = True
        self.background = image
        self.screen.blit(self.background, self.screen.get_rect())
        pg.display.update()
        self.start()


def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()