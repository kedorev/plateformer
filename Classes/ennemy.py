#!/usr/env/bin python3

import pygame

from pprint import pprint
from Game.Classes.image import image
from Game.Classes.perso import perso


class ennemy(perso):

    def __init__(self, name, ecran, posX, posY, nbStepMax = 4):
        super().__init__(name, ecran, nbStepMax)
        self.direction = 'right'
        self.imageDir = image.getImagePath()+"ennemy/"+name+"/"
        self.posX = posX
        self.posY = posY
        self.moveSpeed = 2
        self.width = 70
        self.height = 72

        self.ecran.blit(self.getImage(), (self.posX,self.posY))



    def isInLava(self, screen):
        if self.posY > screen.height - 35 - self.height:
            return True
        else:
            return False

    def jumpimg(self, step=1, max=20):
        self.action = 'jump'
        self.posY -= self.fallSpeed * round(step / 4)
        if step <= max:
            step += 1
            return [step, max]
        else:
            return None

    @property
    def getUpperLeftCorner(self):
        return [self.posX, self.posY]

    @property
    def getLowerRightCorner(self):
        result = [self.posX + self.getImage().get_width(), self.posY + self.getImage().get_height()]
        return result

    def getImage(self):
        direction = self.direction
        self.image = pygame.image.load(self.imageDir+direction+str(self.step)+".png").convert_alpha()
        return self.image

    def refresh(self, aEnvironment):
        self.moveEnnemies(aEnvironment)
        self.ecran.blit(self.getImage(), (self.posX, self.posY))

    def moveEnnemies(self, aEnvironment):
        self.move()
        if not self.touchGround(aEnvironment):
            if self.direction == 'right':
                self.direction = 'left'
            else:
                self.direction = 'right'
            self.move()

