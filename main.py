import pygame
from pygame import Vector2

import block as B
from draw import *

MOVEMENT_DELAY = 0.5


def main():
    # setup
    pygame.init()
    SCREENWIDTH = 720
    SCREENHEIGHT = 720
    screen = pygame.display.set_mode((SCREENHEIGHT, SCREENWIDTH))
    clock = pygame.time.Clock()
    running = True
    dt = 0
    # load level
    block = B.Block(Vector2(5, 3))
    movementTimeout = 0
    # game loop
    while running:
        #    check for user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

        if movementTimeout < 0:
            if keys[pygame.K_d]:
                block._pos += Vector2(1, 0)
                movementTimeout = MOVEMENT_DELAY
            if keys[pygame.K_a]:
                block._pos += Vector2(-1, 0)
                movementTimeout = MOVEMENT_DELAY

            if keys[pygame.K_w]:
                block._pos += Vector2(0, -1)
                movementTimeout = MOVEMENT_DELAY
            if keys[pygame.K_s]:
                block._pos += Vector2(0, 1)
                movementTimeout = MOVEMENT_DELAY
        #    check win/fail conditions

        #    animate
        screen.fill(GRAY)
        block.draw(screen)
        pygame.display.flip()

        movementTimeout -= dt

        dt = clock.tick(60) / 1000
    pygame.quit()


if __name__ == "__main__":
    main()
