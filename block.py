from enum import Enum

from direct.interval.IntervalGlobal import FunctionInterval, Sequence
from direct.interval.LerpInterval import LerpHprInterval, LerpPosHprInterval
from panda3d.core import NodePath, Vec2, Vec3

from draw import *
from level import TileEnum


class Orientation(Enum):
    VERTICAL = 0
    HORIZONTAL = 1
    FORWARD = 2


class Block:
    pos: Vec3
    orientation: Orientation
    model: NodePath
    rotDir: Vec3

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
        orientation = self.orientation
        if direction == "w":
            if self.orientation == Orientation.VERTICAL:
                orientation = Orientation.FORWARD
                pivotPoint.set_pos(self.pos + (0, 0.5, -1))
                pos = Vec3(0, 1.5, 0)

            elif self.orientation == Orientation.HORIZONTAL:
                pivotPoint.set_pos(self.pos + (0, 0.5, -1))
                pos = Vec3(0, 1, 0)

            else:  # self.orientation == Orientation.FORWARD:
                orientation = Orientation.VERTICAL
                pivotPoint.set_pos(self.pos + (0, 1, -1))
                pos = Vec3(0, 1.5, 0)

            hpr = (0, -90, 0)

        elif direction == "s":
            if self.orientation == Orientation.VERTICAL:
                orientation = Orientation.FORWARD
                pivotPoint.set_pos(self.pos + (0, -0.5, -1))
                pos = Vec3(0, -1.5, 0)

            elif self.orientation == Orientation.HORIZONTAL:
                pivotPoint.set_pos(self.pos + (0, -0.5, -1))
                pos = Vec3(0, -1, 0)

            else:  # self.orientation == Orientation.FORWARD:
                orientation = Orientation.VERTICAL
                pivotPoint.set_pos(self.pos + (0, -1, -1))
                pos = Vec3(0, -1.5, 0)

            hpr = (0, 90, 0)

        elif direction == "a":
            if self.orientation == Orientation.VERTICAL:
                orientation = Orientation.HORIZONTAL
                pivotPoint.set_pos(self.pos + (-0.5, 0, -1))
                pos = Vec3(-1.5, 0, 0)

            elif self.orientation == Orientation.HORIZONTAL:
                orientation = Orientation.VERTICAL
                pivotPoint.set_pos(self.pos + (-1, 0, -1))
                pos = Vec3(-1.5, 0, 0)

            else:  # self.orientation == Orientation.FORWARD:
                pivotPoint.set_pos(self.pos + (-0.5, 0, -1))
                pos = Vec3(-1, 0, 0)

            hpr = (0, 0, -90)

        elif direction == "d":
            if self.orientation == Orientation.VERTICAL:
                orientation = Orientation.HORIZONTAL
                pivotPoint.set_pos(self.pos + (0.5, 0, -1))
                pos = Vec3(1.5, 0, 0)

            elif self.orientation == Orientation.HORIZONTAL:
                orientation = Orientation.VERTICAL
                pivotPoint.set_pos(self.pos + (1, 0, -1))
                pos = Vec3(1.5, 0, 0)

            else:  # self.orientation == Orientation.FORWARD:
                pivotPoint.set_pos(self.pos + (0.5, 0, -1))
                pos = Vec3(1, 0, 0)

            hpr = (0, 0, 90)

        else:
            print("direction invalid")
            hpr = (0, 0, 0)
            pos = Vec3(0, 0, 0)

        self.model.wrt_reparent_to(pivotPoint)
        animation_complete_handler = FunctionInterval(
            lambda: self.on_animation_complete(orientation, pos)
        )

        duration = 0.25
        self.animation = True
        self.rotDir = Vec3(hpr) / duration
        return Sequence(
            LerpHprInterval(pivotPoint, duration, hpr),
            FunctionInterval(self.model.get_ancestor(1).flatten_medium),
            animation_complete_handler,
        )

        # self._model.reparent_to(parent)

    def fall(self, tiles: list[TileEnum]):
        self.model.get_ancestor(1).flatten_medium()
        top = self.model.get_ancestor(1)
        pivotPoint = top.attach_new_node("pivotPoint")
        pivotPoint.set_pos(self.pos)
        self.model.wrt_reparent_to(pivotPoint)

        if tiles != list(filter(lambda t: t == TileEnum.AIR, tiles)):
            pass

        dur = 0.25
        hpr = self.rotDir * dur
        dpos = Vec3(0, 0, -10) * dur
        pos = self.pos + dpos
        return Sequence(
            LerpPosHprInterval(pivotPoint, dur, pos, hpr),
            FunctionInterval(self.model.get_ancestor(1).flatten_medium),
            FunctionInterval(
                lambda: self.on_animation_complete(self.orientation, dpos)
            ),
        )

    def on_animation_complete(
        self, orientation: Orientation, pos: Vec3 = Vec3(0, 0, 0)
    ) -> None:
        self.pos += pos
        self.orientation = orientation
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
