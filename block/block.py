from enum import Enum


class Orientation(Enum):
    VERTICAL = 0 # |
    HORIZONTAL = 1 # —
    ORTHOGONAL = 2 # •

class Block:
    x: int
    y: int
    texture: None #| file? 
    orientation: Orientation

    def draw(self):
        pass

    def rotate(self):
        pass
