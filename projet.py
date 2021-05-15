import pygame
import pygame.freetype
import sys
from Game import *
from Données import *
from Menu import *

#Chargement du jeu

pygame.init()

#Update du jeu / FPS

frame_per_second = pygame.time.Clock()

#Appel des classes

game = Game()
menu = Menu()

#Etat de l'écran

ecran = "FirstPage"

#Boucle du jeu

while True :
    
    if ecran == "FirstPage" :

        menu.menuscreen()
        menu.menubutton()

    elif ecran == "APropos" :
        menu.Apropos()

    for event in pygame.event.get() :

        if event.type == pygame.QUIT :
            pygame.quit()
            sys.quit()

        elif event.type == pygame.KEYDOWN :

            if event.key == pygame.K_DOWN :

                menu.buttonmovedown()
 
            elif event.key == pygame.K_UP :
                menu.buttonmoveup()

            elif event.key == pygame.K_RETURN :
                if menu.ybutton == 100 :
                    game.playgame = True
                
                if menu.ybutton == 180 :
                    ecran = "APropos"

                if menu.ybutton == 260 :
                    pygame.quit()
                    sys.quit()

            elif event.key == pygame.K_ESCAPE :
                ecran = "FirstPage"

    pygame.display.update()
    frame_per_second.tick(FPS)
