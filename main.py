from enum import Enum

from direct.interval.Interval import Interval
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import AmbientLight, DirectionalLight, PointLight

from block import *
from draw import *
from level import *

# from light_setup import setup_point_light

MOVEMENT_DELAY = 0.1


class GameState(Enum):
    PLAYING = 0
    FAIL = 1
    WIN = 2
    PAUSE = 3  # currently unused


class App(ShowBase):
    block: Block
    anim: Interval | Sequence | None = None
    state: GameState
    floorTile: NodePath
    level: Level

    def __init__(self) -> None:
        super().__init__()
        self.set_background_color(0, 0, 0, 1)

        self.setupLight()
        self.task_mgr.add(self.setupCamera, "setupCamera")

        self.task_mgr.add(self.update, "update")

        self.loadLevel("levels/test.txt")

        self.state = GameState.PLAYING

        self.accept("w", self.rotate, ["w"])
        self.accept("s", self.rotate, ["s"])
        self.accept("a", self.rotate, ["a"])
        self.accept("d", self.rotate, ["d"])

        self.accept("r", self.resetLevel)

    def loadModel(self, modelPath: str) -> NodePath:
        model = self.loader.load_model(modelPath)
        if model is None:
            print(f"error loading model at: {modelPath}")
            exit(1)
        return model

    def loadLevel(self, level: str):
        floorTile = self.loadModel("models/baseTilePy.egg")
        winTile = self.loadModel("models/winTilePy.egg")

        self.level = Level(level, floorTile, winTile)
        self.level.floor.reparent_to(self.render)

        self.loadBlock()

    def loadBlock(self):
        blockModel = self.loadModel("models/blockModel.egg")
        blockModel.setPos(self.level.startPos.x, self.level.startPos.y, -3.5)
        self.block = Block(blockModel)
        self.block.model.reparent_to(self.render)

    def resetLevel(self):
        self.state = GameState.PLAYING
        self.block.model.remove_node()
        self.loadBlock()

    def rotate(self, direction: str):
        if self.anim and not self.anim.isStopped():
            self.anim.finish()
            return
        if self.state != GameState.PLAYING:
            return
        self.anim = self.block.rotate(direction[0])
        self.anim.start()

    def update(self, task: Task.Task):
        if self.anim and not self.anim.isStopped():
            return task.cont
        blockTilePos = self.block.getTilePositions()
        blockTiles = list(map(lambda a: self.level.floorPlan[a], blockTilePos))
        if TileEnum.AIR in blockTiles:
            self.state = GameState.FAIL
            self.anim = self.block.fall(blockTiles)
            self.anim.start()
            print("fall")
        elif len(blockTiles) == 1 and blockTiles[0] == TileEnum.WIN:
            self.state = GameState.WIN
            print("on winTile")

        return task.cont

    def setupLight(self):
        dlight = DirectionalLight("dlight")
        dlight.setShadowCaster(True)
        dlight.setColor((1, 1, 1, 1))
        dlnp = self.render.attachNewNode(dlight)
        dlnp.setHpr(0, -60, 0)
        self.render.setLight(dlnp)

    def setupCamera(self, task: Task.Task):
        # angleDegrees: float = -5.0
        # angleRadians: float = angleDegrees * (pi / 180.0)
        # self.camera.setPos(sin(angleRadians) - 5, -30 * cos(angleRadians), 10)
        # self.camera.setHpr(angleDegrees - 15, -20, 0)
        self.camera.setPos(-5.08, -29.89, 10)
        self.camera.setHpr(-20, -20, 0)
        return task.cont


def main():
    # setup
    app = App()

    # load level

    # game loop
    app.run()


if __name__ == "__main__":
    main()
