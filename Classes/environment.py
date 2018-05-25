#!/usr/env/bin python3

import pygame
from Game.Classes.image import image

class environment(object):

    def __init__(self, name, ecran, posX = 0, posY = 0):
        self.ecran = ecran
        self.posX = posX
        self.posY = posY
        self.name = name
        self.image = None



    def getImage(self):
        if self.image == None:
            self.image = pygame.image.load(image.getImagePath()+"Environment/" + self.name + ".png").convert_alpha()
        return self.image

    @property
    def startPosX(self):
        return self.posX

    @property
    def endPosX(self):
        return self.posX + self.image.get_width()

    def refresh(self):
        self.ecran.blit(self.getImage(), (self.posX, self.posY))