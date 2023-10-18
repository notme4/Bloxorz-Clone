import panda3d.core

from block import *
from draw import *

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

    # load level
    blockStartPos = _TODO
    block = Block(blockStartPos, Orientation.VERTICAL)
    movementTimeout = 0
    # game loop
    while running:
        #    check for user input

        #    check win/fail conditions

        #    animate
        running = False


if __name__ == "__main__":
    main()
