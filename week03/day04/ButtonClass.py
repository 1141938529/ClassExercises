import pygame
from pygame.sprite import Sprite

from week03.day04.data import *


class Button(Sprite):
    def __init__(self):
        super(Button, self).__init__()
        buttonSurface1 = pygame.image.load("./images/pause_nor.png").convert_alpha()
        buttonSurface2 = pygame.image.load("./images/pause_pressed.png").convert_alpha()
        buttonSurface3 = pygame.image.load("./images/resume_nor.png").convert_alpha()
        buttonSurface4 = pygame.image.load("./images/resume_pressed.png").convert_alpha()
        self.buttonSurfaces =(buttonSurface1,buttonSurface2,buttonSurface3,buttonSurface4)
        self.btnSurface = self.buttonSurfaces[0]
        self.rect = self.buttonSurfaces[0].get_rect()
        self.rect.left = PAUSE_ICON_LEFT
        self.rect.top = PAUSE_ICON_TOP


        self.isPause = False
        self.isOver = False

    def Btn_PauseGame(self):
        if self.isPause:
            self.btnSurface = self.buttonSurfaces[2]
        else:
            self.btnSurface = self.buttonSurfaces[0]

    def Btn_MosueOver(self):
        if self.isPause and self.isOver :
            self.btnSurface = self.buttonSurfaces[3]
        elif not self.isPause and self.isOver :
            self.btnSurface = self.buttonSurfaces[1]
        elif  self.isPause and not self.isOver :
            self.btnSurface = self.buttonSurfaces[2]
        else:
            self.btnSurface = self.buttonSurfaces[0]
    pass