import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self):
        super(Bullet, self).__init__()
        self.surface = pygame.image.load("./images/bullet1.png").convert_alpha()
        self.rect = self.surface.get_rect()
        self.speed = 15
        self.isActive = False
        self.mask = pygame.mask.from_surface(self.surface)
    def move(self):
        if self.rect.top > -self.rect.height:
            self.rect.top -= self.speed
        else:
            self.isActive = False
        pass
