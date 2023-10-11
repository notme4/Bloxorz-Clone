import pygame
from pygame import Color, Surface, Vector2

import block.block as B


def drawIsometric(
    surface: Surface,
    color: Color,
    center: Vector2 = Vector2(0, 0),
    width: int = 100,
    height: int = 50,
) -> None:
    p1 = Vector2(center.x - width / 2, center.y)
    p2 = Vector2(center.x, center.y + height / 2)
    p3 = Vector2(center.x + width / 2, center.y)
    p4 = Vector2(center.x, center.y - height / 2)
    coordinates = [p1, p2, p3, p4]
    pygame.draw.polygon(surface, color, coordinates)


# COLORS
WHITE = Color(255, 255, 255)
LIGHTGRAY = Color(160, 160, 160)
GRAY = Color(100, 100, 100)
BLACK = Color(0, 0, 0)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
CYAN = Color(0, 255, 255)
BLUE = Color(0, 0, 255)


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

    # game loop
    while running:
        #    check for user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

        #    check win/fail conditions

        #    animate
        screen.fill(BLACK)
        drawIsometric(screen, LIGHTGRAY, Vector2(100, 100))
        drawIsometric(screen, GRAY, Vector2(150, 125))
        pygame.display.flip()

        dt = clock.tick(60) / 1000
    pygame.quit()


if __name__ == "__main__":
    main()
