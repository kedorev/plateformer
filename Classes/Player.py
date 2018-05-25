#!/usr/env/bin python3

import pygame

from pprint import pprint
from Game.Classes.image import image
from Game.Classes.perso import perso


class Player(perso):

    def __init__(self, name, ecran):

        super().__init__(name, ecran)
        self.score = 0
        self.ecran.blit(self.getImage(), (self.posX,self.posY))

    def getBonus(self, aBonus):
        for bonus in aBonus:
            if self.inHitBox(bonus.getUpperLeftCorner, bonus.getLowerRightCorner):
                self.score += bonus.point
                aBonus.remove(bonus)
                del bonus

    def hitEnnemy(self, aEnnemy):
        for ennemy in aEnnemy:
            if self.inHitBox(ennemy.getUpperLeftCorner, ennemy.getLowerRightCorner):
                return True
        return False

    def fall(self):
        self.action = 'fall'
        self.posY += self.fallSpeed

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

    def getImage(self, method='walk', type=""):
        if self.direction == '':
            direction = 'right'
        else:
            direction = self.direction
        if method == 'walk':
            self.image = pygame.image.load(self.imageDir + direction + str(self.step) + ".png").convert_alpha()
        elif method == 'jump':
            self.image = pygame.image.load(self.imageDir + "jump_" + direction + ".png").convert_alpha()
        elif method == 'fall':
            self.image = pygame.image.load(self.imageDir + "fall_" + direction + ".png").convert_alpha()
        return self.image

    def refresh(self):
        self.ecran.blit(self.getImage(self.action), (self.posX, self.posY))

    def inHitBox(self, upperLeft, lowerRight):
        if self.posX + self.getImage().get_width() >= upperLeft[0] and self.posX <= lowerRight[0]:
            if self.posY + self.getImage().get_height() >= lowerRight[1]-5 and self.posY <= upperLeft[1]+5:
                return True
        return False
