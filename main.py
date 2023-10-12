import pygame
from pygame import Color, Surface, Vector2

import block as B

# COLORS
WHITE = Color(255, 255, 255)
LIGHTGRAY = Color(160, 160, 160)
GRAY = Color(64, 64, 64)
BLACK = Color(0, 0, 0)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
CYAN = Color(0, 255, 255)
BLUE = Color(0, 0, 255)

MOVEMENT_DELAY = 0.5

Y_HAT = Vector2(-50, 25)
X_HAT = Vector2(50, 25)


def drawIsometricTop(
    surface: Surface,
    color: Color,
    center: Vector2,
    width: int = 100,
    height: int = 50,
    outline: bool = False,
    outlineColor: Color = BLACK,
) -> None:
    """draws a top facing square face in an isometric view"""
    p1 = Vector2(center.x - width / 2, center.y)
    p2 = Vector2(center.x, center.y + height / 2)
    p3 = Vector2(center.x + width / 2, center.y)
    p4 = Vector2(center.x, center.y - height / 2)
    coordinates = [p1, p2, p3, p4]
    pygame.draw.polygon(surface, color, coordinates)
    if outline:
        pygame.draw.line(surface, outlineColor, p1, p2)
        pygame.draw.line(surface, outlineColor, p3, p2)
        pygame.draw.line(surface, outlineColor, p3, p4)
        pygame.draw.line(surface, outlineColor, p1, p4)


def drawIsometricRight(
    surface: Surface,
    color: Color,
    center: Vector2,
    width: int = 100,
    height: int = 50,
    outline: bool = False,
    outlineColor: Color = BLACK,
) -> None:
    """draws a right facing square face in an isometric view"""
    p1 = Vector2(center.x - width / 4, center.y + height / 4 - height / 2)
    p2 = Vector2(center.x - width / 4, center.y + height / 4 + height / 2)
    p3 = Vector2(center.x + width / 4, center.y - height / 4 + height / 2)
    p4 = Vector2(center.x + width / 4, center.y - height / 4 - height / 2)
    coordinates = [p1, p2, p3, p4]
    pygame.draw.polygon(surface, color, coordinates)
    if outline:
        pygame.draw.line(surface, outlineColor, p1, p2)
        pygame.draw.line(surface, outlineColor, p3, p2)
        pygame.draw.line(surface, outlineColor, p3, p4)
        pygame.draw.line(surface, outlineColor, p1, p4)


def drawIsometricLeft(
    surface: Surface,
    color: Color,
    center: Vector2,
    width: int = 100,
    height: int = 50,
    outline: bool = False,
    outlineColor: Color = BLACK,
) -> None:
    """draws a left facing square face in an isometric view"""
    p1 = Vector2(center.x + width / 4, center.y + height / 4 - height / 2)
    p2 = Vector2(center.x + width / 4, center.y + height / 4 + height / 2)
    p3 = Vector2(center.x - width / 4, center.y - height / 4 + height / 2)
    p4 = Vector2(center.x - width / 4, center.y - height / 4 - height / 2)
    coordinates = [p1, p2, p3, p4]
    pygame.draw.polygon(surface, color, coordinates)
    if outline:
        pygame.draw.line(surface, outlineColor, p1, p2)
        pygame.draw.line(surface, outlineColor, p3, p2)
        pygame.draw.line(surface, outlineColor, p3, p4)
        pygame.draw.line(surface, outlineColor, p1, p4)


def drawCube(
    surface: Surface,
    color: Color,
    center: Vector2,
    sideLength: int,
    outline: bool = True,
    outlineColor: Color = BLACK,
) -> None:
    """draws an isometric cube"""
    drawIsometricTop(
        surface=surface,
        color=color,
        center=Vector2(center.x, center.y - sideLength / 2),
        width=sideLength * 2,
        height=sideLength,
        outline=outline,
        outlineColor=outlineColor,
    )
    drawIsometricRight(
        surface=surface,
        color=color,
        center=Vector2(center.x + sideLength / 2, center.y + sideLength / 4),
        width=sideLength * 2,
        height=sideLength,
        outline=outline,
        outlineColor=outlineColor,
    )
    drawIsometricLeft(
        surface=surface,
        color=color,
        center=Vector2(center.x - sideLength / 2, center.y + sideLength / 4),
        width=sideLength * 2,
        height=sideLength,
        outline=outline,
        outlineColor=outlineColor,
    )


def CoordToScreen(Coord: Vector2) -> Vector2:
    return Coord.x * X_HAT + Coord.y * Y_HAT


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
    cubePos = Vector2(3, 1)
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
                cubePos += Vector2(1, 0)
                movementTimeout = MOVEMENT_DELAY
            if keys[pygame.K_a]:
                cubePos -= Vector2(1, 0)
                movementTimeout = MOVEMENT_DELAY

            if keys[pygame.K_w]:
                cubePos -= Vector2(0, 1)
                movementTimeout = MOVEMENT_DELAY
            if keys[pygame.K_s]:
                cubePos += Vector2(0, 1)
                movementTimeout = MOVEMENT_DELAY
        #    check win/fail conditions

        #    animate
        screen.fill(GRAY)
        drawCube(screen, RED, CoordToScreen(cubePos), 50)
        pygame.display.flip()

        movementTimeout -= dt

        dt = clock.tick(60) / 1000
    pygame.quit()


if __name__ == "__main__":
    main()
