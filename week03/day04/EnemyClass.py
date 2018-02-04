import pygame
from pygame.sprite import Sprite

from week03.day04.data import DISPLAY_HEIGHT


class Enemy(Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surface = pygame.image.load("./images/enemy1.png").convert_alpha()
        self.rect = self.surface.get_rect()
        self.boomIndex = 0
        self.isBoom = False
        self.mask = pygame.mask.from_surface(self.surface)
        self.speed = 8
        self.isActive = False
        self.booldbar = 100

    def move(self):
        if self.isActive :
            if self.rect.bottom > DISPLAY_HEIGHT:
                self.isActive = False
            else:
                self.rect.bottom +=self.speed
    def enemyBoom(self):

        if self.boomIndex == 1:
            self.surface =pygame.image.load("./images/enemy1_down1.png").convert_alpha()
        elif self.boomIndex ==2:
            self.surface = pygame.image.load("./images/enemy1_down2.png").convert_alpha()
        elif self.boomIndex ==3:
            self.surface = pygame.image.load("./images/enemy1_down3.png").convert_alpha()
        elif self.boomIndex ==4:
            self.surface = pygame.image.load("./images/enemy1_down4.png").convert_alpha()
            self.isActive = False
            self.boomIndex =0
            self.isBoom = False
            self.surface = pygame.image.load("./images/enemy1.png").convert_alpha()
    pass