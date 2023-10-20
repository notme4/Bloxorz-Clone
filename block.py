from enum import Enum
from math import pi

from direct.interval.IntervalGlobal import FunctionInterval, Sequence
from direct.interval.LerpInterval import LerpHprInterval
from panda3d.core import Mat4D, NodePath, Vec3

from draw import *

STARTING_ANGLE = 0
STARTING_ANGLE_RAD = pi * STARTING_ANGLE / 180


class Orientation(Enum):
    VERTICAL = 0
    HORIZONTAL = 1
    FORWARD = 2


class Block:
    _pos: Vec3
    _orientation: Orientation
    _model: NodePath

    def __init__(
        self,
        blockModel: NodePath,
        orientation: Orientation = Orientation.HORIZONTAL,
    ) -> None:
        self._pos = Vec3(0, 0, 0)
        self._orientation = orientation
        self._model = blockModel
        self._model.set_hpr((STARTING_ANGLE, 0, 0))

    def rotate(self, direction: str) -> Sequence:
        from math import cos, sin

        print("rotate " + str(direction))

        top = self._model.get_top()
        pivotPoint = top.attach_new_node("pivotPoint")

        if direction == "w":
            if self._orientation == Orientation.VERTICAL:
                self._orientation = Orientation.FORWARD
                pivotPoint.set_pos(self._pos + (0, 0.5, -0.5))
                self._pos += (0, 1.5, 0)

            elif self._orientation == Orientation.HORIZONTAL:
                pivotPoint.set_pos(self._pos + (0, 0.5, -0.5))
                self._pos += (0, 1, 0)

            elif self._orientation == Orientation.FORWARD:
                self._orientation = Orientation.VERTICAL
                pivotPoint.set_pos(self._pos + (0, 1, -0.5))
                self._pos += (0, 1.5, 0)

            hpr = (0, -90, 0)

        elif direction == "s":
            if self._orientation == Orientation.VERTICAL:
                self._orientation = Orientation.FORWARD
                pivotPoint.set_pos(self._pos + (0, -0.5, -0.5))
                self._pos += (0, -1.5, 0)

            elif self._orientation == Orientation.HORIZONTAL:
                pivotPoint.set_pos(self._pos + (0, -0.5, -0.5))
                self._pos += (0, -1, 0)

            elif self._orientation == Orientation.FORWARD:
                self._orientation = Orientation.VERTICAL
                pivotPoint.set_pos(self._pos + (0, -1, -0.5))
                self._pos += (0, -1.5, 0)

            hpr = (0, 90, 0)

        elif direction == "a":
            if self._orientation == Orientation.VERTICAL:
                self._orientation = Orientation.HORIZONTAL
                pivotPoint.set_pos(self._pos + (-0.5, 0, -0.5))
                self._pos += (-1.5, 0, 0)

            elif self._orientation == Orientation.HORIZONTAL:
                self._orientation = Orientation.VERTICAL
                pivotPoint.set_pos(self._pos + (-1, 0, -0.5))
                self._pos += (-1.5, 0, 0)

            elif self._orientation == Orientation.FORWARD:
                pivotPoint.set_pos(self._pos + (-0.5, 0, -0.5))
                self._pos += (-1, 0, 0)

            hpr = (0, 0, -90)

        elif direction == "d":
            if self._orientation == Orientation.VERTICAL:
                self._orientation = Orientation.HORIZONTAL
                pivotPoint.set_pos(self._pos + (0.5, 0, -0.5))
                self._pos += (1.5, 0, 0)

            elif self._orientation == Orientation.HORIZONTAL:
                self._orientation = Orientation.VERTICAL
                pivotPoint.set_pos(self._pos + (1, 0, -0.5))
                self._pos += (1.5, 0, 0)

            elif self._orientation == Orientation.FORWARD:
                pivotPoint.set_pos(self._pos + (0.5, 0, -0.5))
                self._pos += (1, 0, 0)

            hpr = (0, 0, 90)

        else:
            print("direction invalid")
            hpr = (0, 0, 0)

        self._model.wrt_reparent_to(pivotPoint)
        return Sequence(
            LerpHprInterval(pivotPoint, 0.5, hpr),
            FunctionInterval(self._model.get_top().flatten_medium),
        )

        # self._model.reparent_to(parent)
