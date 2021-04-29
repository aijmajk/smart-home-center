import pygame
import sys
from pygame.locals import *
import mainscreen
import deviceSetup as Ds

pygame.init()
pygame.font.init()

screen_w = Ds.setupFile["screen_w"]
screen_h = Ds.setupFile["screen_h"]
fullscreen = Ds.setupFile["fullscreen"]
fontcolor = Ds.setupFile["fontcolor"]

screen = pygame.display.set_mode((screen_w, screen_h), 0, 32)
pygame.display.set_caption('smart home center')
firstscreen = mainscreen.Screen(screen_w, screen_h, "./assets/fonts/OpenSans-Regular.ttf", fontcolor)

while True:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)
        # FULLSCREEN TOGGLE
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            if fullscreen == 0:
                screen = pygame.display.set_mode((screen_w, screen_h), FULLSCREEN, 32)
                fullscreen = 1
            else:
                screen = pygame.display.set_mode((screen_w, screen_h), 0, 32)
                fullscreen = 0

    # DRAW
    # reset the screen
    screen.fill((0, 0, 0))
    firstscreen.draw()
    screen.blit(firstscreen, (0, 0))

    # flip the display
    pygame.display.flip()
