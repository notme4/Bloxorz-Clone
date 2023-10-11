import pygame

import block.block as B


def main():
    # setup
    pygame.init()
    SCREENWIDTH = 720
    SCREENHEIGHT = 720
    screen = pygame.display.set_mode((SCREENHEIGHT, SCREENWIDTH))
    clock = pygame.time.Clock()
    running = True
    dt = 0
    # load level

    # game loop
    while running:
        #    check for user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

        #    check win/fail conditions

        #    animate
        screen.fill("black")
        pygame.display.flip()

        dt = clock.tick(60) / 1000
    pygame.quit()


if __name__ == "__main__":
    main()
