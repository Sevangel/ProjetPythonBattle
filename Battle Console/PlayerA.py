from Données import *
import pygame

class PlayerA(pygame.sprite.Sprite) :
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.set_mode((LARGEUR,HAUTEUR))
        self.healthJ1 = 300
        self.healthMax = 300
        self.surf = pygame.Surface((100,200))
        self.rect = self.surf.get_rect(center = (LARGEUR/2, 75))

    def healthbarJ1(self, surface) :
        barcolor = (42,123,0)
        backbarcolor = (60,60,60)

        barpos = [0,50,self.healthJ1,20]
        backbarpos = [0,50,self.healthMax,20]

        pygame.draw.rect(surface, backbarcolor, backbarpos)
        pygame.draw.rect(surface, barcolor, barpos)

    def textsideJ1(self, surface) :
        textfont = pygame.freetype.Font('Ressources/8bitwonder.ttf', 20)

        textsideJ1, rect = textfont.render("Joueur 1", (255,255,255))


        self.screen.blit(textsideJ1, (20,100))

    def J1Flynn(self) :
        img = pygame.image.load("Ressources/FlynnRider.png")
        # Largeur de base de l'image = 1215
        # Hauteur de base de l'image = 3550
        img = pygame.transform.scale(img, (150, 375))

        self.screen.blit(img, (50,200))
    
    def J1Abuelita(self) :
        img = pygame.image.load("Ressources/Abuelita.png")
        # Largeur de base de l'image = 288
        # Hauteur de base de l'image = 500
        img = pygame.transform.scale(img, (216, 375))

        self.screen.blit(img, (50,200))
    
    def J1Shrek(self) :
        img = pygame.image.load("Ressources/Shrek.png")
        # Largeur de base de l'image = 288
        # Hauteur de base de l'image = 400
        img = pygame.transform.scale(img, (246, 375))

        self.screen.blit(img, (50,200))
