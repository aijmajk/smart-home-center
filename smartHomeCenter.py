import pygame
import sys
from pygame.locals import *
import mainscreen
from deviceSetup import setupFile

pygame.init()
pygame.font.init()

screen_w = setupFile["main_settings"][0]["screen_w"]
screen_h = setupFile["main_settings"][0]["screen_h"]
fullscreen = setupFile["main_settings"][0]["fullscreen"]
fontcolor = setupFile["main_settings"][0]["fontcolor"]
font = "./assets/fonts/OpenSans-Regular.ttf"

screen = pygame.display.set_mode((screen_w, screen_h), 0, 32)
pygame.display.set_caption('smart home center')
firstscreen = mainscreen.Screen(screen_w, screen_h, font, fontcolor)

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
