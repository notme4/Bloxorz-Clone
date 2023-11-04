from direct.interval.Interval import Interval
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from light_setup import setup_point_light
from panda3d.core import CollisionBox, CollisionTraverser, CollisionHandlerQueue, CollisionNode, BitMask32, \
    CollisionSphere, CollisionHandlerEvent

from panda3d.core import Point3

from block import *
from draw import *


class App(ShowBase):
    block: Block
    anim: Interval | Sequence | None = None

    def __init__(self) -> None:
        super().__init__()
        self.winner = False

        self.cTrav = CollisionTraverser()
        self.queue = CollisionHandlerQueue()

        self.queueWin = CollisionHandlerQueue()


        blockModel = self.loader.load_model("models/blockModel.egg")
        list = [[1,1,1,1],
                [1,1,1,1],
                [1,1,1,1],
                [1,1,1,1],
                [1,1,1,1],
                [1,1,1,1],
                [1,1,2,1],
                [1,1,1,1],
                [1,1,1,1]]
        for row in range(len(list)):
            for element in range(len(list[0])):
                if (list[row][element] == 1):
                    self.floor = self.loader.loadModel("models/basetile.egg")
                    self.floor.reparentTo(self.render)
                    self.floor.setPos(row-.5, element, -5)

                if (list[row][element] == 2):
                    self.winfloor = self.loader.loadModel("models/winTile.egg")
                    self.winfloor.reparentTo(self.render)
                    self.winfloor.setPos(row-.5, element, -5)
                    win_collison_node = CollisionNode("win-node")
                    win_node = CollisionSphere(0, 0, 4, .5)
                    win_collison_node.addSolid(win_node)
                    self.win_Collider = self.winfloor.attachNewNode(win_collison_node)


        self.set_background_color(0, 0, 0, 1)

        if blockModel is None:
            exit(1)

        setup_point_light(self.render, (20, 0, 20))

        blockModel.reparent_to(self.render)
        np = NodePath("np")
        np.reparent_to(self.render)
        self.block = Block(blockModel)
        self.task_mgr.add(self.spinCameraTask, "SpinCameraTask")
        self.task_mgr.add(self.update, "update")
        self.camera.setPos(0, -20, 3)
        self.camera.setHpr(0, 0, 0)
        self.accept("w", self.rotate, ["w"])
        self.accept("s", self.rotate, ["s"])
        self.accept("a", self.rotate, ["a"])
        self.accept("d", self.rotate, ["d"])

        collider_node = CollisionNode("box-coll")
        collider_node_2 = CollisionNode("box-coll-2")
        collider_node_3 = CollisionNode("box-coll-3")
        collider_node_4 = CollisionNode("box-coll-4")
        collider_node_5 = CollisionNode("box-coll-5")
        collider_node_6 = CollisionNode("box-coll-6")
        collider_node_7 = CollisionNode("box-coll-7")
        collider_node_8 = CollisionNode("box-coll-8")
        collider_node_win = CollisionNode("box-coll-win")

        coll_box_2 = CollisionSphere(1, -.5, -.5, .1)
        coll_box_3 = CollisionSphere(1, .5, -.5, .1)
        coll_box_4 = CollisionSphere(1, .5, .5, .1)
        coll_box_5 = CollisionSphere(1, -.5, .5, .1)

        coll_box = CollisionSphere(-1, -.5, -.5, .1)
        coll_box_6 = CollisionSphere(-1, .5,-.5, .1)
        coll_box_7 = CollisionSphere(-1, .5, .5, .1)
        coll_box_8 = CollisionSphere(-1, -.5, .5, .1)
        coll_box_Win_1 = CollisionSphere(-2, 0, 0, .1)
        coll_box_Win_2 = CollisionSphere(2, 0, 0, .1)

        collider_node.addSolid(coll_box)
        collider_node_2.addSolid(coll_box_2)
        collider_node_3.addSolid(coll_box_3)
        collider_node_4.addSolid(coll_box_4)
        collider_node_5.addSolid(coll_box_5)
        collider_node_6.addSolid(coll_box_6)
        collider_node_7.addSolid(coll_box_7)
        collider_node_8.addSolid(coll_box_8)
        collider_node_win.addSolid(coll_box_Win_1)
        collider_node_win.addSolid(coll_box_Win_2)

        collider = self.block.model.attachNewNode(collider_node)
        collider_2 = self.block.model.attachNewNode(collider_node_2)
        collider_3 = self.block.model.attachNewNode(collider_node_3)
        collider_4 = self.block.model.attachNewNode(collider_node_4)
        collider_5 = self.block.model.attachNewNode(collider_node_5)
        collider_6 = self.block.model.attachNewNode(collider_node_6)
        collider_7 = self.block.model.attachNewNode(collider_node_7)
        collider_8 = self.block.model.attachNewNode(collider_node_8)
        collider_9 = self.block.model.attachNewNode(collider_node_win)

        self.cTrav.addCollider(collider, self.queue)
        self.cTrav.addCollider(collider_2, self.queue)
        self.cTrav.addCollider(collider_3, self.queue)
        self.cTrav.addCollider(collider_4, self.queue)
        self.cTrav.addCollider(collider_5, self.queue)
        self.cTrav.addCollider(collider_6, self.queue)
        self.cTrav.addCollider(collider_7, self.queue)
        self.cTrav.addCollider(collider_8, self.queue)
        self.cTrav.addCollider(collider_9, self.queue)

        self.cTrav.addCollider(self.win_Collider, self.queueWin)

        collider.show()
        collider_2.show()
        collider_3.show()
        collider_4.show()
        collider_5.show()
        collider_6.show()
        collider_7.show()
        collider_8.show()
        collider_9.show()
        self.win_Collider.show()

    def spinCameraTask(self, task: Task.Task):
        from math import cos, pi, sin

        angleDegrees: float = -5.0
        angleRadians: float = angleDegrees * (pi / 180.0)
        self.camera.setPos(sin(angleRadians) - 5, -30 * cos(angleRadians), 10)
        self.camera.setHpr(angleDegrees - 15, -20, 0)
        return Task.cont

    def printStuff(self):
        print("stuff")

    def rotate(self, direction: str):
        if self.anim and not self.anim.isStopped():
            self.anim.finish()
            return
        self.anim = self.block.rotate(direction[0])
        self.anim.start()

    def update(self, task):
        if(not self.block.animation):
            if(len(self.queueWin.getEntries()) > 0):
                print("winner winner")
                self.winner = True

        if(not self.block.animation and not self.winner):
            if self.queue.getEntries():
                list = []
                for n in self.queue.getEntries():
                    list.append(n.getFrom())
                setList = set(list)
                if(len(setList) == 4):
                    self.block.setPos(0)
                else:
                    self.block.setPos(-.1)
            else:
                self.block.setPos(-.1)
        return task.cont


_TODO = None  # TODO

MOVEMENT_DELAY = 0.1


def main():
    # setup
    app = App()

    # load level

    # game loop
    app.run()


if __name__ == "__main__":
    main()
