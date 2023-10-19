from enum import Enum

from direct.showbase.ShowBase import ShowBase
from panda3d.core import NodePath, Vec2

from draw import *


class Orientation(Enum):
    VERTICAL = 0  # |
    DIAGONAL = 1  # \
    ANTIDIAGONAL = 2  # /


class Block:
    _pos: Vec2
    _texture: None  # | file?
    _orientation: Orientation

    def __init__(
        self,
        pos: Vec2,
        parent: NodePath,
        orientation: Orientation = Orientation.ANTIDIAGONAL,
    ) -> None:
        self._pos = pos
        self._orientation = orientation
        model = ShowBase.loader.load_model("models/blockModel.egg")

        if model == None:
            exit(1)

        self._model = model

        self._model.reparent_to(parent)

    def rotate(self, direction: Vec2) -> None:
        ...
