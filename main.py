import os
import random

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

# def update_mushroom_rects(mushrooms, scale_factor):
#     mushroom_rects = list()
#     for mushroom in mushrooms:
#         mushroom_rects.append(Rect(mushroom[0]*scale_factor-scale_factor/2,
#                                    mushroom[1]*scale_factor-scale_factor/2,
#                                    scale_factor,
#                                    scale_factor))
#     return mushroom_rects


def main():
    pygame.init()
    (width, height) = (600, 600)

    scale_factor = 20
    snake_positions = [(10,10),(11,10),(12,10),(13,10),]
    snake_direction = (1,0)
    global snake_length
    #new constant global variable for keys
    global ARROW_KEYS
    ARROW_KEYS = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
    snake_length = 4
    screen = pygame.display.set_mode((width, height))
    mushrooms = list()
    # mushroom_rects = update_mushroom_rects(mushrooms, scale_factor)
    # print(mushroom_rects)
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
    #new variable moved
    pressed = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                #you cannot switch directions to right behind you anymore
                if event.key == ARROW_KEYS[0] and not snake_direction == (0,1):
                    snake_direction = (0,-1)
                if event.key == ARROW_KEYS[1] and not snake_direction == (0,-1):
                    snake_direction = (0,1)
                if event.key == ARROW_KEYS[2] and not snake_direction == (1,0):
                    snake_direction = (-1,0)
                if event.key == ARROW_KEYS[3] and not snake_direction == (-1,0):
                    snake_direction = (1,0)
                #set pressed to true after key is pressed
                if event.key in ARROW_KEYS:
                    pressed = True

            if event.type == snake_move_event:
                #reset pressed
                pressed = False
                new_snake_x = snake_direction[0] + snake_positions[-1][0]
                new_snake_y = snake_direction[1] + snake_positions[-1][1]
                snake_positions.append((new_snake_x,new_snake_y))
                if snake_length < len(snake_positions):
                    del snake_positions[0]
                # print(snake_positions)
                snake_absolute_positions = update_absolute_positions(snake_positions, scale_factor)
                # print(snake_absolute_positions)
                screen.fill((0,0,0))
                pygame.draw.lines(
                    screen,
                    (255, 255, 255),
                    False,
                    snake_absolute_positions,
                    scale_factor
                )

                # head_coords = [snake_positions[-1][0]-scale_factor/2,
                #                snake_positions[-1][1]-scale_factor/2,
                #                snake_positions[-1][0]+scale_factor/2,
                #                snake_positions[-1][1]+scale_factor/2]
                chance = random.randint(1,100)
                if chance <=10:
                    mushrooms.append((random.randint(1,29), random.randint(1,29)))

                result = []
                for mushroom in mushrooms:
                    # print("rects:", mushroom_rects[mushrooms.index(mushroom)])
                    # print(head_coords)
                    if mushroom in snake_positions:
                        # print("Collision")
                        snake_length += 1
                    else:
                        draw_mushroom(screen, scale_factor, mushroom[0], mushroom[1])
                        result.append(mushroom)
                mushrooms = result

                if snake_positions[-1][0]<1 or snake_positions[-1][1]<1 or snake_positions[-1][0]>29 or snake_positions[-1][1]>29:
                    running = False
                if len(snake_positions) != len(set(snake_positions)):
                    running = False
                pygame.display.flip()



if __name__ == "__main__":
    main()
    print("Game Over")
    print("Your score:", snake_length)
