# import pygame
# import pygame.freetype
# import sys
from Game import *
from Données import *

# class Menu(pygame.sprite.Sprite) :

#     def __init__(self) :
#         super().__init__()
#         self.screen = pygame.display.set_mode((LARGEUR,HAUTEUR))
#         self.x = 50
#         self.y = 150
#         self.ybutton = 100
         
#     def  menuscreen(self) :

#         titlefont = pygame.freetype.Font('Ressources/8bitwonder.ttf',50)
#         textfont = pygame.freetype.Font('Ressources/8bitwonder.ttf', 30)
#         self.screen.fill((255,255,255))
#         title, rect = titlefont.render("Insults Battle", (0,0,0))
#         menu1, rect = textfont.render("Jouer", (0,0,0))
#         menu2, rect = textfont.render("A propos", (0,0,0))
#         menu3, rect = textfont.render("Quitter", (0,0,0))


#         self.screen.blit(title, (self.x,self.y))

#         self.screen.blit(menu1, (self.x + 100, self.y + 100))

#         self.screen.blit(menu2, (self.x + 100, self.y + 180))

#         self.screen.blit(menu3, (self.x + 100, self.y + 260))

#     def menubutton(self) :
#         textfont = pygame.freetype.Font('Ressources/8bitwonder.ttf', 30)
#         button, rect = textfont.render("X", (0,0,0))
#         self.screen.blit(button, (self.x, self.y + self.ybutton))

#     def buttonmovedown(self) :
#         if self.ybutton >= 250 :
#             self.ybutton = self.ybutton + 0
#         else :
#             self.ybutton = self.ybutton + 80

#     def buttonmoveup(self) :
#         if self.ybutton <= 130 :
#             self.ybutton = self.ybutton - 0
#         else :
#             self.ybutton = self.ybutton - 80

#     def Apropos(self) :

#         titlefont = pygame.freetype.Font('Ressources/8bitwonder.ttf',40)
#         textfont = pygame.freetype.Font('Ressources/8bitwonder.ttf', 16)
#         self.screen.fill((255,255,255))

#         title, rect = titlefont.render("A Propos", (0,0,0))
#         self.screen.blit(title, (self.x,self.y))

#         text1, rect = textfont.render("Conception par", (0,0,0))
#         text2, rect = textfont.render("Thomas Latour  Julie Cesana et Severine Bourin", (0,0,0))
#         text3, rect = textfont.render("Insults Battle est un divertissement", (0,0,0))
#         text4, rect = textfont.render("Ne prenez pas ces combats pour vous et amusez vous", (0,0,0))

#         self.screen.blit(text1, (self.x, self.y + 100))
#         self.screen.blit(text2, (self.x, self.y + 130))
#         self.screen.blit(text3, (self.x, self.y + 190))
#         self.screen.blit(text4, (self.x, self.y + 220))

class Menu() :
    def Menu() :
        print("==== INSULTS BATTLE ====")

        print("Hey ! Bienvenue en jeu ! Choisis ta proposition avec les numéros !")
        print("1. Jouer")
        print("2. A Propos")
        print("3. Quitter")

        Choix = int(input())

        if Choix == 1 :
            print("C'est parti !")
            Game.SelectPlayer1()
        elif Choix == 2 :
            print("Notre jeu est réalisé par Julie Cesana, Thomas Latour et Séverine Bourin dans le cadre d'un projet de fin d'année ! Le contexte est l'univers des films d'animation : notamment Disney et Shrek !")
            Menu.Menu()
        elif Choix == 3 :
            quit()
        else :
            print("Choix invalide, il faut choisir entre 1 et 3 ;) ")