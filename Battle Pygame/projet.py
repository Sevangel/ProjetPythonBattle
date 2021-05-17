import pygame
import pygame.freetype
import sys
from Game import *
from Données import *
from Menu import *
from Run import *
from Weakness import *

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
weak = Faiblesses()

#Etat de l'écran

ecran = "FirstPage"
PersoJ1 = ""
PersoJ2 =""
screen = pygame.display.set_mode((LARGEUR,HAUTEUR))
WordChoice = ""
PhraseJ1 =[]
PhraseJ2 =[]
comtJ1 = 0
sJ1 = 0
fJ1 = 0
aJ1 = 0
comtJ2 = 0
sJ2 = 0
fJ2 = 0
aJ2 = 0

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
        game.gamebulles()

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

        #LE JEU

        def Playgame() :
            
            global comtJ1
            global sJ1
            global fJ1
            global aJ1
            global comtJ2
            global sJ2
            global fJ2
            global aJ2
            game.gamescreen(screen)

            
            if run.T1J1 == True and run.T1 == True:
                run.Tour1joueur1(screen)
                run.wordpos(screen)
            elif run.T1J1 == False and run.T1 == True:
                run.Tour1joueur2(screen)
                run.wordpos(screen)
            elif run.T2J1 == True and run.T2 == True :
                run.Tour2joueur1(screen)
                run.T2wordpos(screen)
            elif run.T2J1 == False and run.T2 == True :
                run.Tour2joueur2(screen)
                run.T2wordpos(screen)
            elif run.T3J1 == True and run.T3 == True :
                run.Tour3joueur1(screen)
                run.T3wordpos(screen)
            elif run.T3J1 == False and run.T3 == True :
                run.Tour3joueur2(screen)
                run.T3wordpos(screen)
            elif run.T4J1 == True and run.T4 == True :
                run.Tour4joueur1(screen)
                run.T4wordpos(screen)
            elif run.T4J1 == False and run.T4 == True :
                run.Tour4joueur2(screen)
                run.T4wordpos(screen)
            elif run.T5J1 == True and run.T5 == True :
                run.Tour5joueur1(screen)
                run.T5wordpos(screen)
            elif run.T5J1 == False and run.T5 == True :
                run.Tour5joueur2(screen)
                run.T5wordpos(screen)


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

                        #TOUR 1

                        if run.selecty == 40 and run.T1 == True:
                            if run.T1J1 == True :
                                print("Choix 1")
                                PhraseJ1.append(run.word[0])
                                print(PhraseJ1)
                                run.T1J1 = False
                            elif run.T1J1 == False :
                                if PhraseJ1[0] == run.word[0] :
                                    print("Hey ce mot est déjà pris par le joueur 1 prend autre chose !")
                                else :
                                    PhraseJ2.append(run.word[0])
                                    print(PhraseJ2)
                                    run.T1 = False
                                    run.T2 = True
                                    run.T2J1 = True
                                
                        elif run.selecty == 80 and run.T1 == True:
                            if run.T1J1 == True :
                                print("Choix 2")
                                PhraseJ1.append(run.word[1])
                                print(PhraseJ1)
                                run.T1J1 = False
                            elif run.T1J1 == False :
                                if PhraseJ1[0] == run.word[1] :
                                    print("Hey ce mot est déjà pris par le joueur 1 prend autre chose !")
                                else :
                                    PhraseJ2.append(run.word[1])
                                    print(PhraseJ2)
                                    run.T1 = False
                                    run.T2 = True
                                    run.T2J1 = True

                        elif run.selecty == 120 and run.T1 == True :
                            if run.T1J1 == True :
                                print("Choix 3")
                                PhraseJ1.append(run.word[2])
                                print(PhraseJ1)
                                run.T1J1 = False
                            elif run.T1J1 == False :
                                if PhraseJ1[0] == run.word[2] :
                                    print("Hey ce mot est déjà pris par le joueur 1 prend autre chose !")
                                else :
                                    PhraseJ2.append(run.word[2])
                                    print(PhraseJ2)
                                    run.T1 = False
                                    run.T2 = True
                                    run.T2J1 = True

                        elif run.selecty == 160 and run.T1 == True :
                            if run.T1J1 == True :
                                print("Choix 4")
                                PhraseJ1.append(run.word[3])
                                print(PhraseJ1)
                                run.T1J1 = False
                            elif run.T1J1 == False :
                                if PhraseJ1[0] == run.word[3] :
                                    print("Hey ce mot est déjà pris par le joueur 1 prend autre chose !")
                                else :
                                    PhraseJ2.append(run.word[3])
                                    print(PhraseJ2)
                                    run.T1 = False
                                    run.T2 = True
                                    run.T2J1 = True
                        
                        #TOUR 2

                        elif run.selecty == 40 and run.T2 == True:
                            if run.T2J1 == True :
                                print("Choix 1")
                                PhraseJ1.append(run.sujet[0])
                                print(PhraseJ1)
                                run.T2J1 = False
                            elif run.T2J1 == False :
                                if PhraseJ1[1] == run.sujet[0] :
                                    print("Hey ce mot est déjà pris par le joueur 1 prend autre chose !")
                                else :
                                    PhraseJ2.append(run.sujet[0])
                                    print(PhraseJ2)
                                    run.T2 = False
                                    run.T3 = True
                                    run.T3J1 = True
                                
                        elif run.selecty == 80 and run.T2 == True:
                            if run.T2J1 == True :
                                print("Choix 2")
                                PhraseJ1.append(run.sujet[1])
                                print(PhraseJ1)
                                run.T2J1 = False
                            elif run.T2J1 == False :
                                if PhraseJ1[1] == run.sujet[1] :
                                    print("Hey ce mot est déjà pris par le joueur 1 prend autre chose !")
                                else :
                                    PhraseJ2.append(run.sujet[1])
                                    print(PhraseJ2)
                                    run.T2 = False
                                    run.T3 = True
                                    run.T3J1 = True

                        elif run.selecty == 120 and run.T2 == True :
                            if run.T2J1 == True :
                                print("Choix 3")
                                PhraseJ1.append(run.sujet[2])
                                print(PhraseJ1)
                                run.T2J1 = False
                            elif run.T2J1 == False :
                                if PhraseJ1[1] == run.sujet[2] :
                                    print("Hey ce mot est déjà pris par le joueur 1 prend autre chose !")
                                else :
                                    PhraseJ2.append(run.sujet[2])
                                    print(PhraseJ2)
                                    run.T2 = False
                                    run.T3 = True
                                    run.T3J1 = True

                        elif run.selecty == 160 and run.T2 == True :
                            if run.T2J1 == True :
                                print("Choix 4")
                                PhraseJ1.append(run.sujet[3])
                                print(PhraseJ1)
                                run.T2J1 = False
                            elif run.T2J1 == False :
                                if PhraseJ1[1] == run.sujet[3] :
                                    print("Hey ce mot est déjà pris par le joueur 1 prend autre chose !")
                                else :
                                    PhraseJ2.append(run.sujet[3])
                                    print(PhraseJ2)
                                    run.T2 = False
                                    run.T3 = True
                                    run.T3J1 = True

                        #TOUR 3

                        elif run.selecty == 40 and run.T3 == True:
                            if run.T3J1 == True :
                                print("Choix 1")
                                PhraseJ1.append(run.verbe[0])
                                print(PhraseJ1)
                                run.T3J1 = False
                            elif run.T3J1 == False :
                                if PhraseJ1[2] == run.verbe[0] :
                                    print("Hey ce mot est déjà pris par le joueur 1 prend autre chose !")
                                else :
                                    PhraseJ2.append(run.verbe[0])
                                    print(PhraseJ2)
                                    run.T3 = False
                                    run.T4 = True
                                    run.T4J1 = True
                                
                        elif run.selecty == 80 and run.T3 == True:
                            if run.T3J1 == True :
                                print("Choix 2")
                                PhraseJ1.append(run.verbe[1])
                                print(PhraseJ1)
                                run.T3J1 = False
                            elif run.T3J1 == False :
                                if PhraseJ1[2] == run.verbe[1] :
                                    print("Hey ce mot est déjà pris par le joueur 1 prend autre chose !")
                                else :
                                    PhraseJ2.append(run.verbe[1])
                                    print(PhraseJ2)
                                    run.T3 = False
                                    run.T4 = True
                                    run.T4J1 = True

                        elif run.selecty == 120 and run.T3 == True :
                            if run.T3J1 == True :
                                print("Choix 3")
                                PhraseJ1.append(run.verbe[2])
                                print(PhraseJ1)
                                run.T3J1 = False
                            elif run.T3J1 == False :
                                if PhraseJ1[2] == run.verbe[2] :
                                    print("Hey ce mot est déjà pris par le joueur 1 prend autre chose !")
                                else :
                                    PhraseJ2.append(run.verbe[2])
                                    print(PhraseJ2)
                                    run.T3 = False
                                    run.T4 = True
                                    run.T4J1 = True

                        elif run.selecty == 160 and run.T3 == True :
                            if run.T3J1 == True :
                                print("Choix 4")
                                PhraseJ1.append(run.verbe[3])
                                print(PhraseJ1)
                                run.T3J1 = False
                            elif run.T3J1 == False :
                                if PhraseJ1[2] == run.verbe[3] :
                                    print("Hey ce mot est déjà pris par le joueur 1 prend autre chose !")
                                else :
                                    PhraseJ2.append(run.verbe[3])
                                    print(PhraseJ2)
                                    run.T3 = False
                                    run.T4 = True
                                    run.T4J1 = True
                        
                        #TOUR 4

                        elif run.selecty == 40 and run.T4 == True:
                            if run.T4J1 == True :
                                print("Choix 1")
                                PhraseJ1.append(run.complement[0])
                                print(PhraseJ1)
                                run.T4J1 = False
                            elif run.T4J1 == False :
                                if PhraseJ1[3] == run.complement[0] :
                                    print("Hey ce mot est déjà pris par le joueur 1 prend autre chose !")
                                else :
                                    PhraseJ2.append(run.complement[0])
                                    print(PhraseJ2)
                                    run.T4 = False
                                    run.T5 = True
                                    run.T5J1 = True
                                
                        elif run.selecty == 80 and run.T4 == True:
                            if run.T4J1 == True :
                                print("Choix 2")
                                PhraseJ1.append(run.complement[1])
                                print(PhraseJ1)
                                run.T4J1 = False
                            elif run.T4J1 == False :
                                if PhraseJ1[3] == run.complement[1] :
                                    print("Hey ce mot est déjà pris par le joueur 1 prend autre chose !")
                                else :
                                    PhraseJ2.append(run.complement[1])
                                    print(PhraseJ2)
                                    run.T4 = False
                                    run.T5 = True
                                    run.T5J1 = True

                        elif run.selecty == 120 and run.T4 == True :
                            if run.T4J1 == True :
                                print("Choix 3")
                                PhraseJ1.append(run.complement[2])
                                print(PhraseJ1)
                                run.T4J1 = False
                            elif run.T4J1 == False :
                                if PhraseJ1[3] == run.complement[2] :
                                    print("Hey ce mot est déjà pris par le joueur 1 prend autre chose !")
                                else :
                                    PhraseJ2.append(run.complement[2])
                                    print(PhraseJ2)
                                    run.T4 = False
                                    run.T5 = True
                                    run.T5J1 = True

                        elif run.selecty == 160 and run.T4 == True :
                            if run.T4J1 == True :
                                print("Choix 4")
                                PhraseJ1.append(run.complement[3])
                                print(PhraseJ1)
                                run.T4J1 = False
                            elif run.T4J1 == False :
                                if PhraseJ1[3] == run.complement[3] :
                                    print("Hey ce mot est déjà pris par le joueur 1 prend autre chose !")
                                else :
                                    PhraseJ2.append(run.complement[3])
                                    print(PhraseJ2)
                                    run.T4 = False
                                    run.T5 = True
                                    run.T5J1 = True
                        
                        # TOUR 5

                        elif run.selecty == 40 and run.T5 == True:
                            if run.T5J1 == True :
                                print("Choix 1")
                                PhraseJ1.append(run.wordfin[0])
                                print(PhraseJ1)
                                run.T5J1 = False
                            elif run.T5J1 == False :
                                if PhraseJ1[4] == run.wordfin[0] :
                                    print("Hey ce mot est déjà pris par le joueur 1 prend autre chose !")
                                else :
                                    PhraseJ2.append(run.wordfin[0])
                                    print(PhraseJ2)
                                    run.T5 = False
                                    run.Fin = True
                                    run.Fin = True
                                
                        elif run.selecty == 80 and run.T5 == True:
                            if run.T5J1 == True :
                                print("Choix 2")
                                PhraseJ1.append(run.wordfin[1])
                                print(PhraseJ1)
                                run.T5J1 = False
                            elif run.T5J1 == False :
                                if PhraseJ1[4] == run.wordfin[1] :
                                    print("Hey ce mot est déjà pris par le joueur 1 prend autre chose !")
                                else :
                                    PhraseJ2.append(run.wordfin[1])
                                    print(PhraseJ2)
                                    run.T5 = False
                                    run.Fin = True


                        elif run.selecty == 120 and run.T5 == True :
                            if run.T5J1 == True :
                                print("Choix 3")
                                PhraseJ1.append(run.wordfin[2])
                                print(PhraseJ1)
                                run.T5J1 = False
                            elif run.T5J1 == False :
                                if PhraseJ1[4] == run.wordfin[2] :
                                    print("Hey ce mot est déjà pris par le joueur 1 prend autre chose !")
                                else :
                                    PhraseJ2.append(run.wordfin[2])
                                    print(PhraseJ2)
                                    run.T5 = False
                                    run.Fin = True


                        elif run.selecty == 160 and run.T5 == True :
                            if run.T5J1 == True :
                                print("Choix 4")
                                PhraseJ1.append(run.wordfin[3])
                                print(PhraseJ1)
                                run.T5J1 = False
                            elif run.T5J1 == False :
                                if PhraseJ1[4] == run.wordfin[3] :
                                    print("Hey ce mot est déjà pris par le joueur 1 prend autre chose !")
                                else :
                                    PhraseJ2.append(run.wordfin[3])
                                    print(PhraseJ2)
                                    run.T5 = False
                                    run.Fin = True


                if run.Fin == True :

                    for iJ1 in range(0, 5) :

                        if PersoJ2 == "Shrek" :

                            for sJ1 in range(0, 30) :

                                if weak.ShrekWeaknesses[sJ1] == PhraseJ1[iJ1] :
                                    weak.specialdamageJ1 = weak.specialdamageJ1 + 10

                                sJ1 = sJ1 + 1

                        elif PersoJ2 == "Flynn" :

                            for fJ1 in range(0, 30) :

                                if weak.FlynnWeaknesses[fJ1] == PhraseJ1[iJ1] :
                                    weak.specialdamageJ1 = weak.specialdamageJ1 + 10

                                fJ1 = fJ1 + 1

                        elif PersoJ2 == "Abuelita" :

                            for aJ1 in range(0, 30) :

                                if weak.AbuelitaWeaknesses[aJ1] == PhraseJ1[iJ1] :
                                    weak.specialdamageJ1 = weak.specialdamageJ1 + 10

                                aJ1 = aJ1 + 1

                        iJ1 = iJ1 + 1

                        # damageJ1 = weak.specialdamageJ1 + weak.damage
                        # Joueur1.healthJ1 = Joueur1.healthJ1 - damageJ1

                    for iJ2 in range(0, 5) :

                        if PersoJ1 == "Shrek" :

                            for sJ2 in range(0, 30) :

                                if weak.ShrekWeaknesses[sJ2] == PhraseJ1[iJ2] :
                                    weak.specialdamageJ2 = weak.specialdamageJ2 + 10

                                sJ2 = sJ2 + 1

                        elif PersoJ1 == "Flynn" :

                            for fJ2 in range(0, 30) :

                                if weak.FlynnWeaknesses[fJ2] == PhraseJ1[iJ2] :
                                    weak.specialdamageJ1 = weak.specialdamageJ1 + 10

                                fJ2 = fJ2 + 1

                        elif PersoJ1 == "Abuelita" :

                            for aJ2 in range(0, 30) :

                                if weak.AbuelitaWeaknesses[aJ2] == PhraseJ1[iJ2] :
                                    weak.specialdamageJ2 = weak.specialdamageJ2 + 10

                                aJ2 = aJ2 + 1

                        iJ2 = iJ2 + 1
                    
                        # damageJ2 = weak.specialdamageJ2 + weak.damage
                        # Joueur2.healthJ2 = Joueur2.healthJ2 - damageJ2

                    damageJ1 = weak.specialdamageJ1 + weak.damage
                    Joueur1.healthJ1 = Joueur1.healthJ1 - damageJ1

                    damageJ2 = weak.specialdamageJ2 + weak.damage
                    Joueur2.healthJ2 = Joueur2.healthJ2 - damageJ2



                    # while comtJ1 < len(PhraseJ1) :

                    #     if PersoJ2 == "Shrek" :

                    #         while sJ1 < len(weak.ShrekWeaknesses) :

                    #             if weak.ShrekWeaknesses[sJ1] == PhraseJ1[comtJ1] :
                    #                 weak.specialdamageJ1 = weak.specialdamageJ1 + 10

                    #             sJ1 = sJ1 + 1

                    #     elif PersoJ2 == "Flynn" :

                    #         while fJ1 < len(weak.FlynnWeaknesses) :

                    #             if weak.FlynnWeaknesses[fJ1] == PhraseJ1[comtJ1] :
                    #                 weak.specialdamageJ1 = weak.specialdamageJ1 + 10

                    #             fJ1 = fJ1 + 1

                    #     elif PersoJ2 == "Abuelita" :

                    #         while aJ1 < len(weak.AbuelitaWeaknesses) :

                    #             if weak.AbuelitaWeaknesses[aJ1] == PhraseJ1[comtJ1] :
                    #                 weak.specialdamageJ1 = weak.specialdamageJ1 + 10

                    #             aJ1 = aJ1 + 1


                    #     comtJ1 = comtJ1 + 1

                    #     damageJ1 = weak.specialdamageJ1 + weak.damage
                    #     Joueur1.healthJ1 = Joueur1.healthJ1 - damageJ1

                    # while comtJ2 < len(PhraseJ1) :

                    #     if PersoJ2 == "Shrek" :

                    #         while sJ2 < len(weak.ShrekWeaknesses) :

                    #             if weak.ShrekWeaknesses[sJ2] == PhraseJ1[comtJ2] :
                    #                 weak.specialdamageJ2 = weak.specialdamageJ2 + 10

                    #             sJ2 = sJ2 + 1

                    #     elif PersoJ2 == "Flynn" :

                    #         while fJ2 < len(weak.FlynnWeaknesses) :

                    #             if weak.FlynnWeaknesses[fJ2] == PhraseJ1[comtJ2] :
                    #                 weak.specialdamageJ2 = weak.specialdamageJ2 + 10

                    #             fJ2 = fJ2 + 1

                    #     elif PersoJ2 == "Abuelita" :

                    #         while aJ2 < len(weak.AbuelitaWeaknesses) :

                    #             if weak.AbuelitaWeaknesses[aJ2] == PhraseJ1[comtJ2] :
                    #                 weak.specialdamageJ2 = weak.specialdamageJ2 + 10

                    #             aJ2 = aJ2 + 1


                    #     comtJ2 = comtJ2 + 1

                    #     damageJ2 = weak.specialdamageJ2 + weak.damage
                    #     Joueur2.healthJ2 = Joueur2.healthJ2 - damageJ2



        Playgame()




            








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
