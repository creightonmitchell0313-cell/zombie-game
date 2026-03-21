import pygame
import sys
import time
import random
from pygame.locals import *
from ground import drawGround
from character import Person
from zombie import Zombie

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Zombie Chase Survival")

# Create and draw background
background = pygame.Surface((800, 600))
drawGround(background)
screen.blit(background, (0, 0))

# Player setup
player = Person(400, 300)

# Zombies setup
zombies = [Zombie(random.randint(0, 750), random.randint(0, 550))]

# Power Cube setup
power_cube = pygame.Rect(random.randint(0, 750), random.randint(0, 550), 50, 50)
freeze_start_time = None
is_frozen = False

# Timing
clock = pygame.time.Clock()
start_time = time.time()
last_zombie_time = start_time
font = pygame.font.SysFont("Arial", 24)

# Game loop
running = True
game_over = False
while running:
    screen.blit(background, (0, 0))

    if game_over:
        text = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(text, (320, 250))
        survival_time = int(time.time() - start_time)
        timer_text = font.render(f"You survived: {survival_time} seconds", True, (255, 255, 255))
        screen.blit(timer_text, (280, 290))
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()

    # Draw player
    player.draw(screen)

    # Draw power cube
    pygame.draw.rect(screen, (0, 255, 255), power_cube)

    # Handle freezing timer
    if is_frozen and time.time() - freeze_start_time > 3:
        is_frozen = False

    # Move and draw zombies
    for z in zombies:
        if not is_frozen:
            dx = player.x - z.x
            dy = player.y - z.y
            if abs(dx) > abs(dy):
                if dx > 0:
                    z.moveRight()
                else:
                    z.moveLeft()
            else:
                if dy > 0:
                    z.moveDown()
                else:
                    z.moveUp()

        z.draw(screen)

        if z.collide(player):
            game_over = True

    # Timer for survival
    elapsed = int(time.time() - start_time)
    timer_text = font.render(f"Time: {elapsed} sec", True, (255, 255, 255))
    screen.blit(timer_text, (10, 10))

    # Add a new zombie every 5 seconds
    current_time = time.time()
    if current_time - last_zombie_time >= 5:
        zombies.append(Zombie(random.randint(0, 750), random.randint(0, 550)))
        last_zombie_time = current_time

    # Check if player touches the power cube
    player_rect = pygame.Rect(player.x, player.y, 32, 32)
    if player_rect.colliderect(power_cube):
        is_frozen = True
        freeze_start_time = time.time()
        power_cube.topleft = (random.randint(0, 750), random.randint(0, 550))

    pygame.display.update()

    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                player.moveUp()
            elif event.key == K_DOWN:
                player.moveDown()
            elif event.key == K_LEFT:
                player.moveLeft()
            elif event.key == K_RIGHT:
                player.moveRight()

    clock.tick(30)

pygame.quit()
