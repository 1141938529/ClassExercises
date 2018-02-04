import pygame
from pygame.sprite import Sprite

from week03.day04.data import *


class wingPlace(Sprite):

    def __init__(self):
        super(wingPlace, self).__init__()
        # heroSurface1 = pygame.image.load("./images/me1.png").convert_alpha()
        self.surface = pygame.image.load("./images/enemy2.png").convert_alpha()
        self.rect = self.surface.get_rect()
        self.rect.top = 0
        self.rect.left= DISPLAY_WIDTH//2-self.rect.width//2
        self.speed =10
        self.mask = pygame.mask.from_surface(self.surface)
        self.booldbar = 100
    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        pass

    # hero向下移动
    def moveDown(self):
        if self.rect.bottom < DISPLAY_HEIGHT:
            self.rect.top+=self.speed
        pass

    # hero向左移动
    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        pass

    # hero向右移动
    def moveRight(self):
        if self.rect.right < DISPLAY_WIDTH:
            self.rect.left+=self.speed
        pass

    pass
