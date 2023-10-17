from enum import Enum

from draw import *

type TODO = None

class Orientation(Enum):
    VERTICAL = 0  # |
    DIAGONAL = 1  # \
    ANTIDIAGONAL = 2  # /


class Block:
    _pos: TODO
    _texture: None  # | file?
    _orientation: Orientation

    def __init__(
        self, pos: TODO, orientation: Orientation = Orientation.ANTIDIAGONAL
    ) -> None:
        self._pos = pos
        self._orientation = orientation

    def draw(self) -> None:
        ...

    def rotate(self, direction: TODO) -> None:
        ...
