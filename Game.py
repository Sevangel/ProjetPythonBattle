import pygame
import sys
from Menu import *
from Données import *

class Game() :
    def __init__(self) :
        self.run = True
        self.playgame = False
        self.titre = pygame.display.set_caption("Insults Battle")
                    
