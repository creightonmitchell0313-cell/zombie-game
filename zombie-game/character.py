# character.py
# (c) A+ Computer Science

import pygame
from pygame.locals import *

class Person:
    def __init__(self, newX, newY):
        self.x = newX
        self.y = newY
        self.speed = 10  # Match zombie speed

        # Load and scale images to 75% size
        self.images = [
            pygame.transform.scale(pygame.image.load("persond.png").convert_alpha(), (40, 40)),
            pygame.transform.scale(pygame.image.load("personU.png").convert_alpha(), (40, 40)),
            pygame.transform.scale(pygame.image.load("personR.png").convert_alpha(), (40, 40)),
            pygame.transform.scale(pygame.image.load("personL.png").convert_alpha(), (40, 40))
        ]

        self.cos = 0  # Costume index

    def draw(self, window):
        window.blit(self.images[self.cos], (self.x, self.y))

    def moveLeft(self):
        if self.x > 0:
            self.x -= self.speed
            self.cos = 3

    def moveRight(self):
        if self.x < 800 - 30:
            self.x += self.speed
            self.cos = 2

    def moveUp(self):
        if self.y > 0:
            self.y -= self.speed
            self.cos = 1

    def moveDown(self):
        if self.y < 600 - 45:
            self.y += self.speed
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
        return (self.x, self.y, myRec.width, myRec.height)