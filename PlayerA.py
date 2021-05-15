import pygame

class PlayerA(pygame.sprite.Sprite) :
    def __init__(self):
        super().__init__()
        self.health = 100
        self.healthMax = 100
        self.image = pygame.image.load('Ressources\Abuelita.png')
        self.image = pygame.transform.scale(self.image, (200,400))
        self.rect = self.image.get_rect()
        self.rect.x = 80
        self.rect.y = 150