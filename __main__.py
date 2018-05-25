#!/usr/env/bin python3

import pygame
import math
import random

from Game.Classes.GameWindows import GameWindow
from Game.Classes.Player import Player
from Game.Classes.objects import objects

from pprint import pprint


pygame.init()
pygame.font.init()




ecran = GameWindow()
#ecran = GameWindow(800,600)

frameRate = 60
delayBetwwenImage = int(math.floor(1000 / frameRate))

bStartGame = True
ecran.setContinuText()
while bStartGame:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == 27:
                pygame.quit()
                #On partira du principe que la touche echap permet d'annuler le lancement du jeu
            else:
                bMain = True
            bStartGame = False
        pygame.display.flip()


ecran.setCanvasPlay()

etna = Player('Etna',ecran.ecran)
ecran.setLvl1(etna)
clock = pygame.time.Clock()
inJump = None
bGameOver = False
while bMain:

    #Le personnage est en train de saute ( phase ascendante )
    if inJump != None and inJump[0] <= inJump[1]:
        inJump = etna.jumpimg(inJump[0],inJump[1])
    else:
        inJump = None
        #Le personnage est en train de chuter
        if (ecran.player.touchGround(ecran.aEnvironment) == False ):
            etna.fall()
            pygame.event.clear()
        else:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == 27:
                        bMain = False
                    elif event.key == 275:
                        etna.moveRight()
                    elif event.key == 276:
                        etna.moveLeft()
                    elif event.key == 273:
                        inJump = etna.jumpimg()

    pygame.display.flip()
    pygame.time.wait(delayBetwwenImage)

    #On regarde si un bonus apparait sur cette frame
    if random.random() > 0.99:
        objectBonus = objects('gemRed', ecran.ecran)
        ecran.aBonus.append(objectBonus)

    #On gère la suppression des bonus
    for bonus in ecran.aBonus:
        if bonus.despawn():
            ecran.aBonus.remove(bonus)
            del bonus


    etna.move()
    if ecran.aBonus:
        etna.getBonus(ecran.aBonus)
    if etna.isInLava(ecran) == True:
        bMain = False
        bGameOver = True
    if not ecran.refresh():
        bMain = False
        bGameOver = True


ecran.setGameOverScreen()
while bGameOver:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pygame.quit()
            exit()
        pygame.display.flip()