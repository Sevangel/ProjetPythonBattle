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
PersoJ1 = ""
PersoJ2 =""


#Boucle du jeu

while True :
    
    if ecran == "FirstPage" :
        menu.menuscreen()
        menu.menubutton()

    elif ecran == "APropos" :
        menu.Apropos()

    elif ecran == "SelectionJ1" :


        game.gameselectJ1()
        game.gameselectbutton()

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.quit()

            elif event.type == pygame.KEYDOWN :

                if event.key == pygame.K_DOWN :
                    game.gameselectmovedown()
 
                elif event.key == pygame.K_UP :
                    game.gameselectmoveup()

                elif event.key == pygame.K_ESCAPE and ecran == "SelectionJ1" :
                    ecran = "FirstPage"
                    
                elif event.key == pygame.K_RETURN and ecran == "SelectionJ1" :
                    if game.ybutton == 100 :
                        PersoJ1 = "Flynn"
                        ecran = "SelectionJ2"
                
                    elif game.ybutton == 180 :
                        PersoJ1 = "Abuelita"
                        ecran = "SelectionJ2"

                    elif game.ybutton == 260 :
                        PersoJ1 = "Shrek"
                        ecran = "SelectionJ2"

    elif ecran == "SelectionJ2" :

        game.gameselectJ2()
        game.gameselectbutton()

        for event in pygame.event.get() :

            if event.type == pygame.QUIT :
                pygame.quit()
                sys.quit()

            elif event.type == pygame.KEYDOWN :

                if event.key == pygame.K_DOWN :
                    game.gameselectmovedown()
 
                elif event.key == pygame.K_UP :
                    game.gameselectmoveup()

                elif event.key == pygame.K_ESCAPE and ecran == "SelectionJ1" :
                    ecran = "FirstPage"
                    
                elif event.key == pygame.K_RETURN and ecran == "SelectionJ2" :
                    if game.ybutton == 100 :
                        PersoJ2 = "Flynn"
                        print(PersoJ1)
                        print(PersoJ2) 
                        ecran = "Jeu"
                            
                    elif game.ybutton == 180 :
                        PersoJ2 = "Abuelita"
                        print(PersoJ1)
                        print(PersoJ2) 
                        ecran = "Jeu"

                    elif game.ybutton == 260 :
                        PersoJ2 = "Shrek"
                        print(PersoJ1)
                        print(PersoJ2) 
                        ecran = "Jeu"

                elif event.key == pygame.K_ESCAPE and ecran == "SelectionJ2" :
                    ecran = "SelectionJ1"

    elif ecran == "Jeu" :
        game.gameplay()

        for event in pygame.event.get() :

            if event.type == pygame.QUIT :
                pygame.quit()
                sys.quit()


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
                    ecran = "SelectionJ1"
                
                elif menu.ybutton == 180 :
                    ecran = "APropos"

                elif menu.ybutton == 260 :
                    pygame.quit()
                    sys.quit()

            elif event.key == pygame.K_ESCAPE and ecran == "APropos":
                ecran = "FirstPage"


    pygame.display.update()
    frame_per_second.tick(FPS)
