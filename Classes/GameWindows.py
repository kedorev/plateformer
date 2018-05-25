#!/usr/env/bin python3

import pygame

from Game.Classes.image import image
from Game.Classes.environment import environment
from Game.Classes.ennemy import ennemy

class GameWindow(object):

    def __init__(self, width = 0, height = 0):
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.player = None
        self.aEnnemies = []
        self.aEnvironment = []
        self.aBonus = []
        self.backgroundImage = ""
        if width == 0:
            self.ecran = self.defineScreen()
            width,height = pygame.display.get_surface().get_size()
        else:
            self.ecran = self.defineScreen(800, 600)
        self.width = width
        self.height = height

    def defineScreen(self, width = 0, height = 0):
        if width == 0:
            ecran = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            ecran = pygame.display.set_mode((width, height))
        self.backgroundImage = GameWindow._GetBackGroundImage()
        ecran.blit(self.backgroundImage, (0,0))
        return ecran

    def setContinuText(self):
        imageContinu = pygame.image.load(image.getImagePath()+"continu.png").convert_alpha()
        self.ecran.blit(imageContinu, ((self.width/2)-400, (self.height/2)-50))
        pygame.display.flip()

    def setBackground(self):
        self.ecran.blit(self.backgroundImage, (0, 0))

    def setCanvasPlay(self):
        lavaSize = 70
        self.setBackground()
        lavaPos=0
        while lavaPos < self.width:
            self.ecran.blit(pygame.image.load(image.getImagePath()+"lava.png").convert_alpha(), (lavaPos, self.height - lavaSize))
            lavaPos += lavaSize

    @classmethod
    def _GetBackGroundImage(cls):
        return pygame.image.load(image.getImagePath()+"background.png").convert_alpha()

    def refresh(self):
        self.setCanvasPlay()
        self.player.refresh()
        self.setScoreWindow()
        for environment in self.aEnvironment:
            environment.refresh()
        for gems in self.aBonus:
            gems.refresh()
        for ennemy in self.aEnnemies:
            ennemy.refresh(self.aEnvironment)
        pygame.display.flip()
        if(self.player.hitEnnemy(self.aEnnemies)):
            return False
        else:
            return True



    def setGameOverScreen(self):
        self.setBackground()
        imageGameOver= pygame.image.load(image.getImagePath()+"gameOver.png").convert_alpha()
        self.ecran.blit(imageGameOver, ((self.width/2)-99, (self.height/2)-127))
        pygame.display.flip()


    def setLvl1(self, player):
        self.setBackground()
        self.player = player

        self.aEnvironment.append(environment("platformLong",self.ecran,0,300))
        self.aEnvironment.append(environment("platformLong",self.ecran,400,600))
        self.aEnvironment.append(environment("platformShort",self.ecran,500,850))
        self.aEnvironment.append(environment("platformLong",self.ecran,100,900))
        self.aEnvironment.append(environment("platformShort",self.ecran,500,200))
        self.aEnvironment.append(environment("platformLong",self.ecran,350,400))
        self.aEnvironment.append(environment("platformLong",self.ecran,800,700))
        self.aEnvironment.append(environment("platformShort",self.ecran,400,600))
        self.aEnvironment.append(environment("platformLong",self.ecran,600,500))
        self.aEnvironment.append(environment("platformLong",self.ecran,900,800))
        self.aEnvironment.append(environment("platformShort",self.ecran,1300,950))
        self.aEnvironment.append(environment("platformShort",self.ecran,1300,450))
        self.aEnvironment.append(environment("platformLong",self.ecran,1400,700))

        self.aEnnemies.append(ennemy("griffin",self.ecran,500,850-72, 2))
        self.aEnnemies.append(ennemy("griffin",self.ecran,800,700-72, 2))

        pygame.display.flip()

    def setScoreWindow(self):
        self.ecran.blit(self.myfont.render(self.player.getPointText(), False, (0, 0, 0)), (0, 0))







