import pygame
from pygame.sprite import Sprite

from week03.day04.data import *

class Hero(Sprite):
    def __init__(self):
        super(Hero, self).__init__()
        heroSurface1 = pygame.image.load("./images/me1.png").convert_alpha()
        heroSurface2 = pygame.image.load("./images/me2.png").convert_alpha()
        self.surfaces = (heroSurface1,heroSurface2)
        self.rect = self.surfaces[1].get_rect()
        self.rect.left = DISPLAY_WIDTH // 2 - self.rect.width // 2
        self.rect.top = DISPLAY_HEIGHT - self.rect.height - OFFSIDE
        self.width = self.rect.width
        self.height = self.rect.height
        self.mask = pygame.mask.from_surface(self.surfaces[0])

        self.isbomm = False

        self.booldbar = 100
        # hero 移动的速度
        self.speed = 10
        pass

    # hero向上移动
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





if __name__ == "__main__":
    print("ss")
    pass
