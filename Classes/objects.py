#!/usr/env/bin python3

import pygame
from Game.Classes.image import image
import random

class objects(object):

    def __init__(self, name, ecran, lifespawn = 300):
        self.ecran = ecran
        self.image = None
        self.name = name
        self.point = 15
        self.lifespawn = lifespawn
        self.getImage()
        self.posX = random.randint(60,self.ecran.get_width()-60)
        self.posY = random.randint(60,self.ecran.get_height()-60)

    def getImage(self):
        if self.image == None:
            self.image = pygame.image.load(image.getImagePath()+"object/" + self.name + ".png").convert_alpha()
        return self.image

    def refresh(self):
        self.ecran.blit(self.getImage(), (self.posX, self.posY))

    def despawn(self):
        self.lifespawn -= 1
        if(self.lifespawn == 0):
            return True
        return False

    @property
    def getUpperLeftCorner(self):
        return [self.posX, self.posY]

    @property
    def getLowerRightCorner(self):
        result = [self.posX + self.getImage().get_width(), self.posY + self.getImage().get_height()]
        return result
