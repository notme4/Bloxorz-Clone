from enum import Enum

import pygame


class Orientation(Enum):
    VERTICAL = 0  # |
    HORIZONTAL = 1  # —
    ORTHOGONAL = 2  # •


class Block:
    pos: pygame.Vector2
    texture: None  # | file?
    orientation: Orientation

    def draw(self):
        pass

    def rotate(self):
        pass
