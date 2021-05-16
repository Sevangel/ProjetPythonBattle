import pygame
from Game import *
from Données import *
from Menu import *
from PlayerA import *
from PlayerB import *

class Run(pygame.sprite.Sprite) :
    def __init__(self) :
        super().__init__()
        self.screen = pygame.display.set_mode((LARGEUR,HAUTEUR))
        self.wordx = 300
        self.wordy = 400
        self.selecty = 40


    def wordpos(self, surface) :

        textfont = pygame.freetype.Font('Ressources/8bitwonder.ttf', 14)
        textsurftour, rect = textfont.render("Tour 1 Joueur 1", (255,48,48))

        self.screen.blit(textsurftour, (self.wordx,self.wordy))

        textfont = pygame.freetype.Font('Ressources/8bitwonder.ttf', 14)

        mot = ["",'','','']

        textsurf1, rect = textfont.render(mot[0], (0,0,0))
        textsurf2, rect = textfont.render(mot[1], (0,0,0))
        textsurf3, rect = textfont.render(mot[2], (0,0,0))
        textsurf4, rect = textfont.render(mot[3], (0,0,0))

        self.screen.blit(textsurf1, (self.wordx + 50,self.wordy + 40))
        self.screen.blit(textsurf2, (self.wordx + 50,self.wordy + 80))
        self.screen.blit(textsurf3, (self.wordx + 50,self.wordy + 120))
        self.screen.blit(textsurf4, (self.wordx + 50,self.wordy + 160))

    def selectionmot(self) :

        textfont = pygame.freetype.Font('Ressources/8bitwonder.ttf', 14)
        buttonmot, rect = textfont.render("X", (0,0,0))
        self.screen.blit(buttonmot, (self.wordx, self.wordy + self.selecty))


    def moveselectiondown(self) :

        if self.selecty >= 160 :
            self.selecty = self.selecty + 0
        else :
            self.selecty = self.selecty + 40
        
            
    def moveselectionup(self) :
    
        if self.selecty <= 40 :
            self.selecty = self.selecty - 0
        else :
            self.selecty = self.selecty - 40