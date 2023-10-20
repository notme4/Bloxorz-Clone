import panda3d.core as core
import panda3d.egg as egg
from direct.interval.Interval import Interval
from direct.showbase.ShowBase import ShowBase
from direct.task import Task

from block import *
from draw import *


class App(ShowBase):
    block: Block
    anim: Interval | None = None

    def __init__(self) -> None:
        super().__init__()

        blockModel = self.loader.load_model("models/blockModel.egg")

        if blockModel is None:
            exit(1)

        blockModel.reparent_to(self.render)
        np = NodePath("np")
        np.reparent_to(self.render)
        self.block = Block(blockModel)

        self.task_mgr.add(self.spinCameraTask, "SpinCameraTask")
        self.camera.setPos(0, -20, 3)
        self.camera.setHpr(0, 0, 0)
        self.accept("w", self.rotate, ["w"])
        self.accept("s", self.rotate, ["s"])
        self.accept("a", self.rotate, ["a"])
        self.accept("d", self.rotate, ["d"])

    def spinCameraTask(self, task: Task.Task):
        from math import cos, pi, sin

        angleDegrees: float = 0 * 20.0
        angleRadians: float = angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 5)
        self.camera.setHpr(angleDegrees, -5, 0)
        return Task.cont

    def printStuff(self):
        print("stuff")

    def rotate(self, direction: str):
        if self.anim and not self.anim.isStopped():
            self.anim.finish()
            return
        self.anim = self.block.rotate(direction[0])
        self.anim.start()


_TODO = None  # TODO

MOVEMENT_DELAY = 0.2


def main():
    # setup
    app = App()

    # load level

    # game loop
    app.run()


if __name__ == "__main__":
    import createBlockModel

    createBlockModel.createBlockModel()
    main()
