from enum import Enum
from math import pi

from direct.interval.IntervalGlobal import FunctionInterval, Sequence
from direct.interval.LerpInterval import LerpHprInterval
from panda3d.core import NodePath, Vec3

from draw import *

STARTING_ANGLE = 0
STARTING_ANGLE_RAD = pi * STARTING_ANGLE / 180


class Orientation(Enum):
    VERTICAL = 0
    HORIZONTAL = 1
    FORWARD = 2


class Block:
    pos: Vec3
    orientation: Orientation
    model: NodePath


    def __init__(
        self,
        blockModel: NodePath,
        orientation: Orientation = Orientation.HORIZONTAL,
    ) -> None:
        self.pos = Vec3(0, 0, 0)
        self.orientation = orientation
        self.model = blockModel
        self.animation = False
        self.model.set_hpr((STARTING_ANGLE, 0, 0))

    def rotate(self, direction: str) -> Sequence:
        print("rotate " + str(direction))

        top = self.model.get_top()
        pivotPoint = top.attach_new_node("pivotPoint")
        if direction == "w":
            if self.orientation == Orientation.VERTICAL:
                self.orientation = Orientation.FORWARD
                pivotPoint.set_pos(self.pos + (0, 0.5, -0.5))
                self.pos += (0, 1.5, 0)

            elif self.orientation == Orientation.HORIZONTAL:
                pivotPoint.set_pos(self.pos + (0, 0.5, -0.5))
                self.pos += (0, 1, 0)

            elif self.orientation == Orientation.FORWARD:
                self.orientation = Orientation.VERTICAL
                pivotPoint.set_pos(self.pos + (0, 1, -0.5))
                self.pos += (0, 1.5, 0)

            hpr = (0, -90, 0)

        elif direction == "s":
            if self.orientation == Orientation.VERTICAL:
                self.orientation = Orientation.FORWARD
                pivotPoint.set_pos(self.pos + (0, -0.5, -0.5))
                self.pos += (0, -1.5, 0)

            elif self.orientation == Orientation.HORIZONTAL:
                pivotPoint.set_pos(self.pos + (0, -0.5, -0.5))
                self.pos += (0, -1, 0)

            elif self.orientation == Orientation.FORWARD:
                self.orientation = Orientation.VERTICAL
                pivotPoint.set_pos(self.pos + (0, -1, -0.5))
                self.pos += (0, -1.5, 0)

            hpr = (0, 90, 0)

        elif direction == "a":
            if self.orientation == Orientation.VERTICAL:
                self.orientation = Orientation.HORIZONTAL
                pivotPoint.set_pos(self.pos + (-0.5, 0, -0.5))
                self.pos += (-1.5, 0, 0)

            elif self.orientation == Orientation.HORIZONTAL:
                self.orientation = Orientation.VERTICAL
                pivotPoint.set_pos(self.pos + (-1, 0, -0.5))
                self.pos += (-1.5, 0, 0)

            elif self.orientation == Orientation.FORWARD:
                pivotPoint.set_pos(self.pos + (-0.5, 0, -0.5))
                self.pos += (-1, 0, 0)

            hpr = (0, 0, -90)

        elif direction == "d":
            if self.orientation == Orientation.VERTICAL:
                self.orientation = Orientation.HORIZONTAL
                pivotPoint.set_pos(self.pos + (0.5, 0, -0.5))
                self.pos += (1.5, 0, 0)

            elif self.orientation == Orientation.HORIZONTAL:
                self.orientation = Orientation.VERTICAL
                pivotPoint.set_pos(self.pos + (1, 0, -0.5))
                self.pos += (1.5, 0, 0)

            elif self.orientation == Orientation.FORWARD:
                pivotPoint.set_pos(self.pos + (0.5, 0, -0.5))
                self.pos += (1, 0, 0)

            hpr = (0, 0, 90)

        else:
            print("direction invalid")
            hpr = (0, 0, 0)

        self.model.wrt_reparent_to(pivotPoint)
        animation_complete_handler = FunctionInterval(self.on_animation_complete)
        self.animation = True
        return Sequence(
            LerpHprInterval(pivotPoint, 0.25, hpr),
            FunctionInterval(self.model.get_top().flatten_medium),
            animation_complete_handler
        )


        # self._model.reparent_to(parent)

    def on_animation_complete(self):

        self.animation = False


    def setPos(self, position):

        self.pos += (0, 0, position)
        # print(f"getPos: {self.model.getPos()}")
        # print(f"self.pos: {self.pos}")
        self.model.setZ(self.model.getZ() + position)








