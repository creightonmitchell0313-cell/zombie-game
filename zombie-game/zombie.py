# zombie.py
# (c) A+ Computer Science

import pygame
from pygame.locals import *

class Zombie:
    def __init__(self, newX, newY):
        self.x = float(newX)
        self.y = float(newY)

        # Load images with transparency support
        self.images = [
            pygame.image.load("zombieD.png").convert_alpha(),
            pygame.image.load("zombieU.png").convert_alpha(),
            pygame.image.load("zombieR.png").convert_alpha(),
            pygame.image.load("zombieL.png").convert_alpha()
        ]

        self.cos = 0  # Costume index

    def draw(self, window):
        window.blit(self.images[self.cos], (int(self.x), int(self.y)))

    def moveLeft(self):
        if self.x > 0:
            self.x -= 1.5
            self.cos = 3

    def moveRight(self):
        if self.x < 750:
            self.x += 1.5
            self.cos = 2

    def moveUp(self):
        if self.y > 0:
            self.y -= 1.5
            self.cos = 1

    def moveDown(self):
        if self.y < 550:
            self.y += 1.5
            self.cos = 0

    def collide(self, other):
        myRec = self.getRec()
        otherRec = other.getRec()
        oRight = otherRec[0] + otherRec[2]
        oBottom = otherRec[1] + otherRec[3]
        right = myRec[0] + myRec[2]
        bottom = myRec[1] + myRec[3]

        return (otherRec[0] <= right and oRight >= self.x and
                otherRec[1] <= bottom and oBottom >= self.y)

    def getRec(self):
        myRec = self.images[self.cos].get_rect()
        return (int(self.x), int(self.y), myRec.width, myRec.height)