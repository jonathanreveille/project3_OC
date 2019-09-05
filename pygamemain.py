#! /usr/bin/env python3
# coding : utf-8 

import pygame as pg
from demo.config import settings


class Game:
    """ Class that represents the game for pygame"""


    def __init__(self): # initializer
        pg.init()
        self.screen = pg.display.set_mode((settings.WIDTH,settings.HEIGHT))
        self.background = pg.image.load(settings.BACKGROUND)


    def start(self): # method to launch the game
        pass





def main():
    game = Game()
    game.start()

 


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


if __name__ == "__main__":
    main()
