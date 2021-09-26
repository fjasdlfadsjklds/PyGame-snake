import os
import pygame
from pygame.locals import *

def get_absolute_coordinates(x, y, scalefactor):
    return (x * scalefactor, y * scalefactor)

def move_snake(surface,):
    pass

def update_absolute_positions(snake_positions, scale_factor):
    snake_absolute_positions = list()
    for position in snake_positions:
        snake_absolute_positions.append((position[0] * scale_factor, position[1] * scale_factor))
    return snake_absolute_positions

def draw_mushroom(screen,scale_factor,x,y):
    mushroom = pygame.image.load_basic('mushroom.bmp')
    absolute_x = x*scale_factor-scale_factor/2
    absolute_y = y*scale_factor-scale_factor/2
    screen.blit(mushroom, (absolute_x,absolute_y))

# def update_mushroom_rects(mushrooms):
#
def main():
    pygame.init()
    (width, height) = (600, 600)

    scale_factor = 20
    snake_positions = [(4,6),(4,7),(4,8),(4,9),(5,9),(6,9)]
    snake_direction = (1,0)
    snake_length = 6
    screen = pygame.display.set_mode((width, height))
    mushrooms = [(10,10)]
    # mushroom_rects = update_mushroom_rects(mushrooms)
    snake_absolute_positions = update_absolute_positions(snake_positions, scale_factor)
    pygame.draw.lines(
        screen,
        (255,255,255),
        False,
        snake_absolute_positions,
        scale_factor
    )
    pygame.display.flip()
    snake_move_event = pygame.USEREVENT + 0
    pygame.time.set_timer(snake_move_event, 500)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake_direction = (0,-1)
                if event.key == pygame.K_DOWN:
                    snake_direction = (0,1)
                if event.key == pygame.K_LEFT:
                    snake_direction = (-1,0)
                if event.key == pygame.K_RIGHT:
                    snake_direction = (1,0)
            if event.type == snake_move_event:
                new_snake_x = snake_direction[0] + snake_positions[-1][0]
                new_snake_y = snake_direction[1] + snake_positions[-1][1]
                snake_positions.append((new_snake_x,new_snake_y))
                if snake_length < len(snake_positions):
                    del snake_positions[0]
                print(snake_positions)
                snake_absolute_positions = update_absolute_positions(snake_positions, scale_factor)
                screen.fill((0,0,0))
                pygame.draw.lines(
                    screen,
                    (255, 255, 255),
                    False,
                    snake_absolute_positions,
                    scale_factor
                )
                for mushroom in mushrooms:
                    draw_mushroom(screen, scale_factor, mushroom[0], mushroom[1])
                pygame.display.flip()



if __name__ == "__main__":
    main()