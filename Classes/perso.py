#!/usr/env/bin python3

import pygame

from pprint import pprint
from Game.Classes.image import image

class perso(object):

    def __init__(self, name, ecran, nbStepMax = 4):

        self.moveSpeed = 4
        self.fallSpeed = 5
        self.imageDir = image.getImagePath()+name+"/"
        self.name = name
        self.image = None
        self.posX = 0
        self.posY = 60
        self.width = 105
        self.height = 160
        self.step = 0
        self.timerSwitchMoveImage = 0
        self.direction = ''
        self.ecran = ecran
        self.action = 'walk'
        self.type = ""
        self.nbStepMax = nbStepMax


    def move(self):
        if self.direction == 'left':
            self.posX -= self.moveSpeed
            if self.posX < 0:
                self.posX = 0
            self.timerSwitchMoveImage += 1
            if self.timerSwitchMoveImage == 5:
                self.timerSwitchMoveImage = 0
                self.step += 1
            if self.step == self.nbStepMax:
                self.step = 0
        elif self.direction == 'right':
            self.posX += self.moveSpeed
            if self.posX + self.width > self.ecran.get_width():
                self.posX = self.ecran.get_width() - self.width
            self.timerSwitchMoveImage += 1
            if self.timerSwitchMoveImage == 5:
                self.timerSwitchMoveImage = 0
                self.step += 1
            if self.step == self.nbStepMax:
                self.step = 0

    def moveRight(self):
        self._MoveHorizontaly('right')


    def moveLeft(self):
        self._MoveHorizontaly('left')




    def _MoveHorizontaly(self, direction):
        if direction == 'left':
            if self.direction != "left":
                self.step = 0
                self.direction = 'left'
        elif direction == 'right':
            if self.direction != "right":
                self.step = 0
                self.direction = 'right'






    def touchGround(self, aEnvironment):
        for environment in aEnvironment:
            if environment.posY >= self.posY + self.height and environment.posY <= self.posY + self.fallSpeed + self.height:
                pos_x = self.posX
                #25 correspond à la taille de l'image que l'on doit retranché
                if environment.startPosX <= self.posX +  self.width -25 and environment.endPosX >= pos_x +25:
                    self.action = 'walk'
                    return True
        return False

    def getPointText(self):
        return "Points : "+ str(self.score)
