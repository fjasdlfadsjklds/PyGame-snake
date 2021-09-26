import os
import pygame
from pygame.locals import *

def get_absolute_coordinates(x, y, scalefactor):
    return (x * scalefactor, y * scalefactor)


def main():
    pygame.init()
    (width, height) = (600, 600)

    snake_position = (4,6)
    snake_length = 5
    scale_factor = 20
    snake_width = 1

    screen = pygame.display.set_mode((width, height))
    pygame.draw.line(
        screen,
        (255,255,255),
        get_absolute_coordinates(snake_position[0], snake_position[1], scale_factor),
        get_absolute_coordinates(snake_position[0]+snake_length, snake_position[1], scale_factor),
        snake_width * scale_factor
    )
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()