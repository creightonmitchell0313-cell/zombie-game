import pygame
import asyncio
import time
import random
from pygame.locals import *
from ground import drawGround
from character import Person
from zombie import Zombie


async def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Zombie Chase Survival")

    background = pygame.Surface((800, 600))
    drawGround(background)
    screen.blit(background, (0, 0))

    player = Person(400, 300)
    zombies = [Zombie(random.randint(0, 750), random.randint(0, 550))]

    power_cube = pygame.Rect(random.randint(0, 750), random.randint(0, 550), 50, 50)
    freeze_start_time = None
    is_frozen = False

    clock = pygame.time.Clock()
    start_time = time.time()
    last_zombie_time = start_time
    font = pygame.font.Font(None, 24)

    running = True
    game_over = False
    game_over_time = None

    while running:
        screen.blit(background, (0, 0))

        if game_over:
            text = font.render("GAME OVER", True, (255, 0, 0))
            screen.blit(text, (320, 250))
            survival_time = int(game_over_time - start_time)
            timer_text = font.render(f"You survived: {survival_time} seconds", True, (255, 255, 255))
            screen.blit(timer_text, (240, 290))
            restart_text = font.render("Press R to restart", True, (200, 200, 200))
            screen.blit(restart_text, (300, 330))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN and event.key == K_r:
                    player = Person(400, 300)
                    zombies = [Zombie(random.randint(0, 750), random.randint(0, 550))]
                    power_cube = pygame.Rect(random.randint(0, 750), random.randint(0, 550), 50, 50)
                    is_frozen = False
                    start_time = time.time()
                    last_zombie_time = start_time
                    game_over = False

            clock.tick(30)
            await asyncio.sleep(0)
            continue

        player.draw(screen)
        pygame.draw.rect(screen, (0, 255, 255), power_cube)

        if is_frozen and time.time() - freeze_start_time > 3:
            is_frozen = False

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
                game_over_time = time.time()

        elapsed = int(time.time() - start_time)
        timer_text = font.render(f"Time: {elapsed} sec", True, (255, 255, 255))
        screen.blit(timer_text, (10, 10))

        current_time = time.time()
        if current_time - last_zombie_time >= 5:
            zombies.append(Zombie(random.randint(0, 750), random.randint(0, 550)))
            last_zombie_time = current_time

        player_rect = pygame.Rect(player.x, player.y, 32, 32)
        if player_rect.colliderect(power_cube):
            is_frozen = True
            freeze_start_time = time.time()
            power_cube.topleft = (random.randint(0, 750), random.randint(0, 550))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
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
        await asyncio.sleep(0)

    pygame.quit()


asyncio.run(main())
