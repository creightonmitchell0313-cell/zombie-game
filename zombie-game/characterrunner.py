# characterunner.py
# (c) A+ Computer Science

import pygame, sys
from pygame.locals import *
from character import Person

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Character Runner")

pygame.key.set_repeat(100, 100)

# Create character
guy = Person(50, 50)

# List to track screen areas that changed
changedRecs = []

# Draw initial screen
screen.fill((30, 30, 30))  # dark gray background
pygame.display.update()

# Game loop
while True:
    screen.fill((30, 30, 30))  # redraw background
    
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