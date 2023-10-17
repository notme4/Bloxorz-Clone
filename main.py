import panda3d

import block as B
from draw import *

type TODO = None

MOVEMENT_DELAY = 0.2


def main():
    # setup
    SCREENWIDTH = 720
    SCREENHEIGHT = 720
    screen = TODO
    clock = TODO
    running = True
    dt = 0
    # load level
    blockStartPos = TODO
    block = B.Block(blockStartPos, B.Orientation.VERTICAL)
    movementTimeout = 0
    # game loop
    while running:
        #    check for user input
        
        #    check win/fail conditions

        #    animate
        pass


if __name__ == "__main__":
    main()
