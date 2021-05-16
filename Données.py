import pygame
import random
import sys

FPS = 60
HAUTEUR = 600
LARGEUR = 960


def Accroche() :

    Accroches = [
            "Hey tête de gland,",
            "Bonjour mon mignon,",
            "Écoute moi bien petit malin,",
            "Je ne me répéterai pas,",
            "Soyons clair,"
    ]

    mot = random.sample(Accroches, 4)
    print(mot)