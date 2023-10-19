import panda3d.core as core
import panda3d.egg as egg
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import LVecBase3, NodePath, Point3D, TransformState, Vec4

from block import *
from draw import *


class App(ShowBase):
    block: Block

    def __init__(self, fStartDirect: bool = True, windowType=None) -> None:
        super().__init__(fStartDirect, windowType)

        self.block = Block(Vec2(0, 0), self.render)

        self.task_mgr.add(self.spinCameraTask, "SpinCameraTask")
        self.camera.setPos(0, -20, 3)
        self.camera.setHpr(0, 0, 0)
        self.accept("w", self.block.rotate, [(1, 0)])
        self.accept("s", self.block.rotate, [(-1, 0)])
        self.accept("a", self.block.rotate, [(0, 1)])
        self.accept("d", self.block.rotate, [(0, -1)])

    def spinCameraTask(self, task: Task.Task):
        from math import cos, pi, sin

        angleDegrees: float = 0 * 20.0
        angleRadians: float = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

    def printStuff(self):
        print("stuff")


_TODO = None  # TODO

MOVEMENT_DELAY = 0.2


def main():
    # setup
    SCREENWIDTH = 720
    SCREENHEIGHT = 720
    screen = _TODO
    clock = _TODO
    running = True
    dt = 0

    app = App()

    # load level
    blockStartPos = _TODO
    block = Block(blockStartPos, Orientation.VERTICAL)
    movementTimeout = 0

    # game loop
    app.run()


if __name__ == "__main__":
    import createBlockModel

    createBlockModel.createBlockModel()
    main()
