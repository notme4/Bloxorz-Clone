from enum import Enum

import pygame
from pygame import Surface, Vector2

from draw import *


class Orientation(Enum):
    VERTICAL = 0  # |
    DIAGONAL = 1  # \
    ANTIDIAGONAL = 2  # /


class Block:
    _pos: pygame.Vector2
    _texture: None  # | file?
    _orientation: Orientation

    def __init__(
        self, pos: Vector2, orientation: Orientation = Orientation.ANTIDIAGONAL
    ):
        self._pos = pos
        self._orientation = orientation

    def draw(self, surface: Surface):
        if self._orientation == Orientation.VERTICAL:
            drawCube(surface, RED, self._pos, 50)
            drawCube(surface, RED, self._pos + Vector2(-1, -1), 50)
        elif self._orientation == Orientation.DIAGONAL:
            drawCube(surface, RED, self._pos, 50)
            drawCube(surface, RED, self._pos + Vector2(1, 0), 50)
        else:
            drawCube(surface, RED, self._pos, 50)
            drawCube(surface, RED, self._pos + Vector2(0, 1), 50)

    def rotate(self):
        pass
