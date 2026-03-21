# zombierunner.py
# (c) A+ Computer Science

import pygame
import sys
from pygame.locals import *
from zombie import Zombie

# Initialize the screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Zombie Runner")

pygame.key.set_repeat(100, 100)

# Create zombie object
guy = Zombie(50, 50)

# For tracking redraw areas
changedRecs = []

# Initial draw
screen.fill((30, 30, 30))  # dark gray background for horror feel
pygame.display.update()

# Main Game Loop
while True:
    screen.fill((30, 30, 30))

    guy.draw(screen)
    changedRecs.append(guy.getRec())

    pygame.display.update(changedRecs)

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            changedRecs.append(guy.getRec())

            if event.key == K_UP:
                guy.moveUp()
            elif event.key == K_DOWN:
                guy.moveDown()
            elif event.key == K_LEFT:
                guy.moveLeft()
            elif event.key == K_RIGHT:
                guy.moveRight()

    pygame.time.wait(100)