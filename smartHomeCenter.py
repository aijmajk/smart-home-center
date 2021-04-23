import pygame, sys, time
from pygame.locals import *

pygame.init()
pygame.font.init()

screen_w = 1280
screen_h = 1024
fullscreen = 0
fontcolor = (255, 255, 255)
fontsize = 50

screen = pygame.display.set_mode((screen_w, screen_h), 0, 32)
myfont = pygame.font.SysFont("cmap", fontsize)

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

    # TIME
    current_time = time.localtime()
    hours = str(current_time[3])
    minutes = str(current_time[4])
    seconds = str(current_time[5])

    if len(minutes) == 1:
        minutes = "0"+minutes
    if len(seconds) == 1:
        seconds = "0"+seconds
    textsurface = myfont.render(hours+":"+minutes+":"+seconds, True, fontcolor)

    # DRAW
        # reset the screen
    screen.fill((0, 0, 0))
        # clock
    screen.blit(textsurface, (0, 0))

        # flip the display
    pygame.display.flip()
