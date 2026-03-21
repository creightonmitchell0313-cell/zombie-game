import pygame
import random

class PowerCube:
    def __init__(self):
        self.image = pygame.image.load("powercube.png").convert_alpha()
        self.x = random.randint(100, 700)
        self.y = random.randint(100, 500)

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def getRec(self):
        myRec = self.image.get_rect()
        return (self.x, self.y, myRec.width, myRec.height)
