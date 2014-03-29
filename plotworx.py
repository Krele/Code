import random, pygame, sys, math, time, world, platforms

import constants

from pygame.locals import *
from random import randrange
from spritesheet_functions import SpriteSheet



pygame.init()#*****************PROGRAMM****************
FPS = 30
m = 30
n = 10
WIDTH = 1200
HEIGHT = 700

global plot,layer
plot = [[0 for y in range(n)] for x in range(m)] #actually background layer 
layer =[[0 for y in range(n)] for x in range(m)] #upper layer

fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Plotworx')



def PlotGen():
    # 8-12 - ground
    # 0 - air
    # 2-7 - useless decorations
    for x in range (0,m):
        plot[x][n-1]=randrange(8,13)
        plot[x][n-2]=randrange(2,7)
        layer[x][n-2]=randrange(2,7)
PlotGen()    


def DisplayPlot():
    for x in range(m):
        for y in range(n):
            if plot[x][y]==8:
                i = 0
                j = 2
                screen.blit(sprite(i,j),(64*x,64*y))
            if plot[x][y]==9:
                i = 1
                j = 2
                screen.blit(sprite(i,j),(64*x,64*y))                
            if plot[x][y]==10:
                i = 2
                j = 2
                screen.blit(sprite(i,j),(64*x,64*y))
            if plot[x][y]==11:
                i = 3
                j = 2
                screen.blit(sprite(i,j),(64*x,64*y))
            if plot[x][y]==12:
                i = 4
                j = 2
                screen.blit(sprite(i,j),(64*x,64*y))
            if plot[x][y]==2:
                i = 0
                j = 0
                screen.blit(sprite(i,j),(64*x,64*y))
            if plot[x][y]==3:
                i = 1
                j = 0
                screen.blit(sprite(i,j),(64*x,64*y))                
            if plot[x][y]==4:
                i = 2
                j = 0
                screen.blit(sprite(i,j),(64*x,64*y))
            if plot[x][y]==5:
                i = 3
                j = 0
                screen.blit(sprite(i,j),(64*x,64*y))
            if plot[x][y]==6:
                i = 4
                j = 0
                screen.blit(sprite(i,j),(64*x,64*y))

    
def DisplayLayer():
    for x in range(m):
        for y in range(n):
            if layer[x][y]==2:
                i = 0
                j = 1
                screen.blit(sprite(i,j),(64*x,64*y))
            if layer[x][y]==3:
                i = 1
                j = 1
                screen.blit(sprite(i,j),(64*x,64*y))                
            if layer[x][y]==4:
                i = 2
                j = 1
                screen.blit(sprite(i,j),(64*x,64*y))
            if layer[x][y]==5:
                i = 3
                j = 1
                screen.blit(sprite(i,j),(64*x,64*y))
            if layer[x][y]==6:
                i = 4
                j = 1
                screen.blit(sprite(i,j),(64*x,64*y))

