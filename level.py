from collections import defaultdict
from enum import Enum

from panda3d.core import CollisionNode, CollisionSphere, NodePath, Vec2


class TileEnum(Enum):
    AIR = 0
    FLOOR = 1
    WIN = 2
    START = 3


FloorPlan = defaultdict[Vec2, TileEnum]


class Level:
    floorPlan: FloorPlan
    startPos: Vec2
    path: str
    floor: NodePath
    winTile: NodePath
    win_Collider: NodePath

    def __init__(self, floorPlanPath: str, floorTile: NodePath, winTile: NodePath):
        self.path = floorPlanPath
        self.floorPlan = self.loadLevel(floorPlanPath)
        self.winTile = winTile

        self.win_Collider = None
        self.startPos = None

        self.floor = NodePath("Floor")
        for i in range(20):
            for j in range(20):
                tile = self.floorPlan[Vec2(i, j)]
                if tile == TileEnum.AIR:
                    continue
                elif tile == TileEnum.FLOOR:
                    floor = floorTile.copy_to(self.floor)
                    floor.setPos(i, j, -5)
                elif tile == TileEnum.WIN:
                    if self.win_Collider is not None:
                        print("invalid level data: 2 win positions")
                        exit(1)
                    winTile.reparent_to(self.floor)
                    winTile.setPos(i, j, -5)

                    win_collison_node = CollisionNode("win-node")
                    win_collison_node.addSolid(CollisionSphere(0, 0, 4, 0.5))
                    self.win_Collider = winTile.attachNewNode(win_collison_node)
                elif tile == TileEnum.START:
                    if self.startPos is not None:
                        print("invalid level data: 2 start positions")
                        exit(1)

                    floor = floorTile.copy_to(self.floor)
                    floor.setPos(i, j, -5)
                    self.startPos = Vec2(i, j)
        if self.startPos is None:
            print("invalid level data: no start pos")
            exit(1)
        if self.win_Collider is None:
            print("invalid level data no win position")
            exit(1)

    def loadLevel(self, floorPlanPath: str) -> FloorPlan:
        with open(floorPlanPath) as file:
            result: FloorPlan = defaultdict(lambda: TileEnum.AIR)
            for i, line in enumerate(file, 2):
                for j, char in enumerate(line.strip(), 2):
                    pos = Vec2(i, j)
                    if char == "x":
                        result[pos] = TileEnum.FLOOR
                    elif char == " ":
                        result[pos] = TileEnum.AIR
                    elif char == "w":
                        result[pos] = TileEnum.WIN
                    elif char == "s":
                        result[pos] = TileEnum.START
                    else:
                        print(f"invalid level data: invalid character `{char}'")
                        exit(1)
            return result
