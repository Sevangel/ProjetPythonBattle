from PlayerA import *
from PlayerB import *
import pygame
import pygame.freetype
import sys
from Menu import *
from Données import *

class Game() :
    def __init__(self) :
        self.run = True
        self.titre = pygame.display.set_caption("Insults Battle")
        self.screen = pygame.display.set_mode((LARGEUR,HAUTEUR))
        self.x = 50
        self.y = 150
        self.ybutton = 100

    def gamebulles(self) :
        bulleJ1 = pygame.image.load("Ressources/BulleJ1.png")
        bulleJ2 = pygame.image.load("Ressources/BulleJ2.png")

        self.screen.blit(bulleJ1,(150,20))
        self.screen.blit(bulleJ2,(180,-80))


    def gameselectJ1(self) :
        
        self.screen.fill((255,255,255))

        titlefont = pygame.freetype.Font('Ressources/8bitwonder.ttf',30)
        textfont = pygame.freetype.Font('Ressources/8bitwonder.ttf', 20)

        Joueur1, rect = titlefont.render("Joueur 1", (0,0,0))
        title, rect = titlefont.render("Selectionnez votre personnage", (0,0,0))
        perso1, rect = textfont.render("Flynn", (0,0,0))
        perso2, rect = textfont.render("Abuelita", (0,0,0))
        perso3, rect = textfont.render("Shrek", (0,0,0))

        self.screen.blit(Joueur1, (self.x, self.y - 80))
        self.screen.blit(title, (self.x,self.y))
        self.screen.blit(perso1, (self.x + 100, self.y + 100))
        self.screen.blit(perso2, (self.x + 100, self.y + 180))
        self.screen.blit(perso3, (self.x + 100, self.y + 260))

    def gameselectJ2(self) :
        
        self.screen.fill((255,255,255))

        titlefont = pygame.freetype.Font('Ressources/8bitwonder.ttf',30)
        textfont = pygame.freetype.Font('Ressources/8bitwonder.ttf', 20)

        Joueur1, rect = titlefont.render("Joueur 2", (0,0,0))
        title, rect = titlefont.render("Selectionnez votre personnage", (0,0,0))
        perso1, rect = textfont.render("Flynn", (0,0,0))
        perso2, rect = textfont.render("Abuelita", (0,0,0))
        perso3, rect = textfont.render("Shrek", (0,0,0))

        self.screen.blit(Joueur1, (self.x, self.y - 80))
        self.screen.blit(title, (self.x,self.y))
        self.screen.blit(perso1, (self.x + 100, self.y + 100))
        self.screen.blit(perso2, (self.x + 100, self.y + 180))
        self.screen.blit(perso3, (self.x + 100, self.y + 260))

    def gameselectbutton(self) :
        textfont = pygame.freetype.Font('Ressources/8bitwonder.ttf', 20)
        button, rect = textfont.render("X", (0,0,0))
        self.screen.blit(button, (self.x, self.y + self.ybutton))

    def gameselectmoveup(self) :
        if self.ybutton <= 130 :
            self.ybutton = self.ybutton - 0
        else :
            self.ybutton = self.ybutton - 80

    def gameselectmovedown(self) :
        if self.ybutton >= 250 :
            self.ybutton = self.ybutton + 0
        else :
            self.ybutton = self.ybutton + 80

    def gameplay(self) :
        self.screen = pygame.display.set_mode((LARGEUR,HAUTEUR))
        background = pygame.image.load("Ressources/Paysage.jpeg")
        background = pygame.transform.scale(background,(LARGEUR, HAUTEUR))

        self.screen.blit(background,(0,0))

    def gamescreen(self, surface):
        self.xrect = 270
        self.yrect = 380

        rectcolor = (255,255,255)
        backrectcolor = (0,0,0)

        rectpos = [self.xrect,self.yrect,400,200]
        backrectpos = [self.xrect-10,self.yrect-10,420,220]

        pygame.draw.rect(surface, backrectcolor, backrectpos)
        pygame.draw.rect(surface, rectcolor, rectpos)

    def FinManche(self, surface) :
        textfont = pygame.freetype.Font('Ressources/8bitwonder.ttf', 20)
        button, rect = textfont.render("Fin de la Manche !", (0,0,0))
        self.screen.blit(button, (self.x + 300, self.y + self.ybutton + 200))
