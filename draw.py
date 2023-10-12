import pygame
from pygame import Color, Surface, Vector2

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

Y_HAT = Vector2(-50, 25)
X_HAT = Vector2(50, 25)


def CoordToScreen(Coord: Vector2) -> Vector2:
    return Coord.x * X_HAT + Coord.y * Y_HAT


def drawIsometricTop(
    surface: Surface,  # the surface to draw to
    color: Color,
    center: Vector2,
    width: int = 100,
    height: int = 50,
    outline: bool = False,
    outlineColor: Color = BLACK,
) -> None:
    """draws a top face in an isometric view

    Parameters
        surface (pygame.Surface): the surface to be drawn to
        color (pygame.Color): the color to draw the object
        center (pygame.Vector2): the center of the face, i.e. the intersection of the 2 diagonals
        width (int): the width of the horizontal direction, default 100
        height (int): the height of the vertical direction, default 50
        outline (bool): whether or not to outline the face, default false
        outlineColor (Color): the color to outline the face in, default black
    """

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
    """draws a right face in an isometric view

    Parameters
        surface (pygame.Surface): the surface to be drawn to
        color (pygame.Color): the color to draw the object
        center (pygame.Vector2): the center of the face, i.e. the intersection of the 2 diagonals
        width (int): the width of the antidiagonal (/) direction, default 100
        height (int): the height of the diagonal (\\) direction, default 50
        outline (bool): whether or not to outline the face, default false
        outlineColor (Color): the color to outline the face in, default black
    """

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
    """draws a left face in an isometric view

    Parameters
        surface (pygame.Surface): the surface to be drawn to
        color (pygame.Color): the color to draw the object
        center (pygame.Vector2): the center of the face, i.e. the intersection of the 2 diagonals
        width (int): the width of the diagonal (\\) direction, default 100
        height (int): the height of the antidiagonal (/) direction, default 50
        outline (bool): whether or not to outline the face, default false
        outlineColor (Color): the color to outline the face in, default black
    """

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
    """draws an isometric cube

    Parameters
        surface (pygame.Surface): the surface to be drawn to
        color (pygame.Color): the color to draw the object
        center (pygame.Vector2): the center of the face, i.e. the front corner
        sidelength (int): the length of a side of the cube
        outline (bool): whether or not to outline the face, default false
        outlineColor (Color): the color to outline the face in, default black
    """

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
