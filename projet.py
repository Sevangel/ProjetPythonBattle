import pygame
import sys
from Données import *
from Menu import *

#Chargement du jeu

pygame.init()

#Update du jeu / FPS

frame_per_second = pygame.time.Clock()

displaysurface = pygame.display.set_mode((LARGEUR,HAUTEUR))
pygame.display.set_caption("JOKE BATTLEROYAL")

#Chargement arrière-plan du jeu

background = pygame.image.load('Image.png')

#Chargement des plateformes


while True :

    #Mettre l'arrière-plan dans le jeu

    displaysurface.blit(background, (-400,-500))



    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.quit()
        elif event.type == pygame.K_ESCAPE

    pygame.display.update()
    frame_per_second.tick(FPS)