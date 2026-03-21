import pygame
import sys
from pygame.locals import *
from ground import *
from character import *

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ground Runner")

# Create and draw background
background = pygame.Surface((800, 600))
drawGround(background)
screen.blit(background, (0, 0))
pygame.display.update()

# Set up movement key repeat
pygame.key.set_repeat(100, 100)

# Create the player
guy = Person(400, 300)
changedRecs = []

# Game loop
while True:
    screen.blit(background, (0, 0))
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
