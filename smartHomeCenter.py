import pygame
import sys
from pygame.locals import *
import mainscreen

pygame.init()

screen_w = 1280
screen_h = 1024
fullscreen = 0
fontcolor = (255, 255, 255)
fontsize = 50

screen = pygame.display.set_mode((screen_w, screen_h), 0, 32)
firstscreen = mainscreen.Screen(screen_w, screen_h, "cmap", fontcolor)
# myfont = pygame.font.SysFont("cmap", fontsize)

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
