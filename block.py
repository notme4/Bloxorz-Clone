from enum import Enum

import pygame
from pygame import Vector2


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

    def draw(self):
        pass

    def rotate(self):
        pass
