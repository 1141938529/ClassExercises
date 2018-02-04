import pygame
from pygame.sprite import Sprite

from week03.day04.data import DISPLAY_HEIGHT


class wpBullet(Sprite):
    def __init__(self):
        super(wpBullet, self).__init__()
        self.surface = pygame.image.load("./images/bullet2.png").convert_alpha()
        self.rect = self.surface.get_rect()
        self.speed = 15
        self.isActive = False
        self.mask = pygame.mask.from_surface(self.surface)

    def move(self):
        if self.rect.top < DISPLAY_HEIGHT:
            self.rect.top += self.speed
        else:
            self.isActive = False

