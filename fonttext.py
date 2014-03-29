import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

fontObj = pygame.font.Font('GOST_A.ttf', 40)
textSurfaceObj = fontObj.render('Calm',1 , GREEN)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)
pygame.mixer.music.load('prepare_for_outside_(version2).ogg')
pygame.mixer.music.play(-1, 120.0)

while True: # main game loop
    DISPLAYSURF.fill((0,0,0))
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
