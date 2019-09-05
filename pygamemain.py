#! /usr/bin/env python3
# coding : utf-8 

import pygame


def main():
    print("launched game but it does not launch...bloody hell")
 
 
    #Initialize everything
    pygame.init()
    screen = pygame.display.set_mode((225,225))
    pygame.display.set_caption("McGaver")

    
    pygame.quit()

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
