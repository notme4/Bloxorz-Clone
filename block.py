from enum import Enum

from direct.interval.IntervalGlobal import FunctionInterval, Sequence
from direct.interval.LerpInterval import LerpHprInterval
from panda3d.core import NodePath, Vec2, Vec3

from draw import *


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
        orientation: Orientation = Orientation.VERTICAL,
    ) -> None:
        self.pos = Vec3(blockModel.get_pos())
        self.orientation = orientation
        self.model = blockModel
        self.animation = False
        self.model.set_hpr((0, 0, 0))

    def rotate(self, direction: str) -> Sequence:
        print("rotate " + str(direction))

        top = self.model.get_ancestor(1)
        pivotPoint = top.attach_new_node("pivotPoint")
        if direction == "w":
            if self.orientation == Orientation.VERTICAL:
                self.orientation = Orientation.FORWARD
                pivotPoint.set_pos(self.pos + (0, 0.5, -1))
                self.pos += (0, 1.5, 0)

            elif self.orientation == Orientation.HORIZONTAL:
                pivotPoint.set_pos(self.pos + (0, 0.5, -1))
                self.pos += (0, 1, 0)

            elif self.orientation == Orientation.FORWARD:
                self.orientation = Orientation.VERTICAL
                pivotPoint.set_pos(self.pos + (0, 1, -1))
                self.pos += (0, 1.5, 0)

            hpr = (0, -90, 0)

        elif direction == "s":
            if self.orientation == Orientation.VERTICAL:
                self.orientation = Orientation.FORWARD
                pivotPoint.set_pos(self.pos + (0, -0.5, -1))
                self.pos += (0, -1.5, 0)

            elif self.orientation == Orientation.HORIZONTAL:
                pivotPoint.set_pos(self.pos + (0, -0.5, -1))
                self.pos += (0, -1, 0)

            elif self.orientation == Orientation.FORWARD:
                self.orientation = Orientation.VERTICAL
                pivotPoint.set_pos(self.pos + (0, -1, -1))
                self.pos += (0, -1.5, 0)

            hpr = (0, 90, 0)

        elif direction == "a":
            if self.orientation == Orientation.VERTICAL:
                self.orientation = Orientation.HORIZONTAL
                pivotPoint.set_pos(self.pos + (-0.5, 0, -1))
                self.pos += (-1.5, 0, 0)

            elif self.orientation == Orientation.HORIZONTAL:
                self.orientation = Orientation.VERTICAL
                pivotPoint.set_pos(self.pos + (-1, 0, -1))
                self.pos += (-1.5, 0, 0)

            elif self.orientation == Orientation.FORWARD:
                pivotPoint.set_pos(self.pos + (-0.5, 0, -1))
                self.pos += (-1, 0, 0)

            hpr = (0, 0, -90)

        elif direction == "d":
            if self.orientation == Orientation.VERTICAL:
                self.orientation = Orientation.HORIZONTAL
                pivotPoint.set_pos(self.pos + (0.5, 0, -1))
                self.pos += (1.5, 0, 0)

            elif self.orientation == Orientation.HORIZONTAL:
                self.orientation = Orientation.VERTICAL
                pivotPoint.set_pos(self.pos + (1, 0, -1))
                self.pos += (1.5, 0, 0)

            elif self.orientation == Orientation.FORWARD:
                pivotPoint.set_pos(self.pos + (0.5, 0, -1))
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
            FunctionInterval(self.model.get_ancestor(1).flatten_medium),
            animation_complete_handler,
        )

        # self._model.reparent_to(parent)

    def on_animation_complete(self):
        self.animation = False

    def addPos(self, position: Vec3):
        self.pos += position
        self.model.set_pos(self.model.get_pos() + position)

    def getTilePositions(self) -> list[Vec2]:
        if self.orientation == Orientation.VERTICAL:
            return [Vec2(self.pos.x, self.pos.y)]
        elif self.orientation == Orientation.HORIZONTAL:
            return [
                Vec2(self.pos.x + 0.5, self.pos.y),
                Vec2(self.pos.x - 0.5, self.pos.y),
            ]
        else:  # self.orientation == Orientation.FORWARD
            return [
                Vec2(self.pos.x, self.pos.y + 0.5),
                Vec2(self.pos.x, self.pos.y - 0.5),
            ]
