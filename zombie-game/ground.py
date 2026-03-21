# Ground.py
#(c) A+ Computer Science
#www.apluscompsci.com

import pygame
import random
from pygame.locals import *

def drawGround(window):
    # Horror-style colors
    blood_red = (120, 0, 0)
    grimy_edge = (80, 40, 20)
    dark_road = (50, 50, 50)
    broken_gray = (90, 90, 90)

    tile_size = 50

    for xPos in range(0, 800, tile_size):
        for yPos in range(0, 600, tile_size):
            if yPos <= 50 or yPos >= 550:
                pygame.draw.rect(window, blood_red, (xPos, yPos, tile_size, tile_size))
            elif yPos == 100 or yPos == 500:
                pygame.draw.rect(window, grimy_edge, (xPos, yPos, tile_size, tile_size))
            else:
                tile_color = broken_gray if random.randint(0, 9) == 0 else dark_road
                pygame.draw.rect(window, tile_color, (xPos, yPos, tile_size, tile_size))

    # Fog overlay
    fog = pygame.Surface((800, 600), pygame.SRCALPHA)
    fog.fill((100, 100, 100, 80))
    window.blit(fog, (0, 0))