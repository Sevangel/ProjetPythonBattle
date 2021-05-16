import pygame
import pygame.freetype
import sys
from Game import *
from Données import *
from Menu import *
from Run import *

#Chargement du jeu

pygame.init()

#Update du jeu / FPS

frame_per_second = pygame.time.Clock()

#Appel des classes

game = Game()
menu = Menu()
Joueur1 = PlayerA()
Joueur2 = PlayerB()
run = Run()

#Etat de l'écran

ecran = "FirstPage"
PersoJ1 = ""
PersoJ2 =""
screen = pygame.display.set_mode((LARGEUR,HAUTEUR))
WordChoice = ""

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
        Joueur1.healthbarJ1(screen)
        Joueur2.healthbarJ2(screen)
        Joueur1.textsideJ1(screen)
        Joueur2.textsideJ2(screen)

        if PersoJ1 == "Flynn" :
            Joueur1.J1Flynn()

        elif PersoJ1 == "Abuelita" :
            Joueur1.J1Abuelita()

        elif PersoJ1 == "Shrek" :
            Joueur1.J1Shrek()

        if PersoJ2 == "Flynn" :
            Joueur2.J2Flynn()

        elif PersoJ2 == "Abuelita" :
            Joueur2.J2Abuelita()

        elif PersoJ2 == "Shrek" :
            Joueur2.J2Shrek()

        game.gamescreen(screen)
        run.wordpos(screen)

        run.selectionmot()

        for event in pygame.event.get() :

            if event.type == pygame.QUIT :
                pygame.quit()
                sys.quit()

            elif event.type == pygame.KEYDOWN :

                if event.key == pygame.K_DOWN :
                    run.moveselectiondown()
 
                elif event.key == pygame.K_UP :
                    run.moveselectionup()

                elif event.key == pygame.K_RETURN and ecran == "Jeu" :
                    if run.selecty == 40 :
                        print("Choix 1")
                        WordChoice = "1"
                            
                    elif run.selecty == 80 :
                        print("Choix 2")
                        WordChoice = "2"

                    elif run.selecty == 120 :
                        print("Choix 3")
                        WordChoice = "3"

                    elif run.selecty == 160 :
                        print("Choix 4")
                        WordChoice = "4"




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
