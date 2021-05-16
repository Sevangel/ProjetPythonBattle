from Données import *
import pygame

class PlayerB(pygame.sprite.Sprite) :
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.set_mode((LARGEUR,HAUTEUR))
        self.health = 300
        self.healthMax = 300
        self.attack = 30
        self.surf = pygame.Surface((100,200))
        self.rect = self.surf.get_rect(center = (LARGEUR/2, 75))

    def healthbarJ2(self, surface) :
        barcolor = (42,123,0)
        backbarcolor = (60,60,60)

        barpos = [660,50,self.health,20]
        backbarpos = [660,50,self.healthMax,20]


        pygame.draw.rect(surface, backbarcolor, backbarpos)
        pygame.draw.rect(surface, barcolor, barpos)

    def textsideJ2(self, surface) :
        textfont = pygame.freetype.Font('Ressources/8bitwonder.ttf', 20)

        textsideJ2, rect = textfont.render("Joueur 2", (255,255,255))


        self.screen.blit(textsideJ2, (780,100))


    def J2Flynn(self) :
        img = pygame.image.load("Ressources/FlynnRider.png")
        # Largeur de base de l'image = 1215
        # Hauteur de base de l'image = 3550
        img = pygame.transform.scale(img, (150, 375))

        #Pour mettre le J2 à 50 pixel du bord droit, on prend la largeur total moins les 50 pixels, moins la largeur du personnage
        #Ici 960-50-150 = 760

        self.screen.blit(img, (760,200))
    
    def J2Abuelita(self) :
        img = pygame.image.load("Ressources/Abuelita.png")
        # Largeur de base de l'image = 288
        # Hauteur de base de l'image = 500
        img = pygame.transform.scale(img, (216, 375))

        #Pour mettre le J2 à 50 pixel du bord droit, on prend la largeur total moins les 50 pixels, moins la largeur du personnage
        #Ici 960-50-216 = 694

        self.screen.blit(img, (694,200))
    
    def J2Shrek(self) :
        img = pygame.image.load("Ressources/Shrek.png")
        # Largeur de base de l'image = 288
        # Hauteur de base de l'image = 400
        img = pygame.transform.scale(img, (246, 375))

        #Pour mettre le J2 à 50 pixel du bord droit, on prend la largeur total moins les 50 pixels, moins la largeur du personnage
        #Ici 960-50-246 = 664

        self.screen.blit(img, (664,200))
