import panda3d.core as core
import panda3d.egg as egg
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import LVecBase3, NodePath, Point3D, TransformState, Vec4

from block import *
from draw import *


class App(ShowBase):
    scene: NodePath

    def __init__(self, fStartDirect: bool = True, windowType=None) -> None:
        super().__init__(fStartDirect, windowType)
        scene = self.loader.load_model("models/blockModel.egg")

        if scene == None:
            exit(1)

        self.scene = scene

        self.scene.reparent_to(self.render)
        self.task_mgr.add(self.spinCameraTask, "SpinCameraTask")
        self.camera.setPos(0, -20, 3)
        self.camera.setHpr(0, 0, 0)
        self.accept("w", self.rotateModel, [LVecBase3(0, 90, 0)])
        self.accept("w-repeat", self.rotateModel, [LVecBase3(0, 90, 0)])
        self.accept("s", self.rotateModel, [LVecBase3(0, -90, 0)])
        self.accept("s-repeat", self.rotateModel, [LVecBase3(0, -90, 0)])
        self.accept("d", self.rotateModel, [LVecBase3(0, 0, 90)])
        self.accept("d-repeat", self.rotateModel, [LVecBase3(0, 0, 90)])
        self.accept("a", self.rotateModel, [LVecBase3(0, 0, -90)])
        self.accept("a-repeat", self.rotateModel, [LVecBase3(0, 0, -90)])

    def spinCameraTask(self, task: Task.Task):
        from math import cos, pi, sin

        angleDegrees: float = 0 * 20.0
        angleRadians: float = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

    def rotateModel(self, dir: LVecBase3):
        ts = self.scene.getTransform()
        ts = ts.set_hpr(ts.get_hpr() + dir)

        self.scene.setTransform(ts)

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
