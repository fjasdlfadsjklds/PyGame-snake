import os
import pygame
from pygame.locals import *

def get_absolute_coordinates(x, y, scalefactor):
    return (x * scalefactor, y * scalefactor)


def main():
    pygame.init()
    (width, height) = (600, 600)

    scale_factor = 20
    snake_positions = [(4,6),(4,7),(4,8),(4,9),(5,9),(6,9)]
    snake_absolute_positions = list()
    for position in snake_positions:
        snake_absolute_positions.append((position[0] * scale_factor, position[1] * scale_factor))
    # snake_length = 5


    screen = pygame.display.set_mode((width, height))
    pygame.draw.lines(
        screen,
        (255,255,255),
        False,
        snake_absolute_positions,
        scale_factor
    )
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()