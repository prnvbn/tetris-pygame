import pygame
import random

from defs import *
from piece import Piece

def create_grid(locked_positions={}, hieght=20, width=20):
    """Creates a Grid!

    Parameters
    ----------

    locked_positions: dict{(i, j) : (r, g, b)}
        dictionary of position, colour pair as key value pairs
    hieght: int
        grid hieght, default is 20    
    width: int
        grid width, default is 10    
    """
    # initialising a black 20 x 10 grid
    # 20 rows and 10 colums
    grid = [[(0, 0, 0) for _ in range(hieght)] for _ in range(width)]

    # Colouring the locked positions
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if (col, row) in locked_positions:    
                colour = locked_positions[(col, row)]
                grid[row][j] = colour
    return grid

def get_shape():
    """Returns a random shape from [S, Z, I, O, J, L, T]"""
    return Piece(5, 0, random.choice(shapes))

def fill_grid(surface, grid):
    """Fills the Tetris gameboard grid"""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + i*block_size, block_size, block_size), 0)

    # Drawing the grid border
    pygame.draw.rect(surface, (0, 255, 0), (top_left_x, top_left_y, play_width, play_height), 4)      


def draw_window(surface, grid):
    """Draws the Tetris game window"""
    surface.fill((0, 0, 0))

    pygame.font.init()
    font  = pygame.font.SysFont('agencyfb', 60)
    label = font.render("Tetris", 1, (255, 255, 255))

    fill_grid(surface, grid)
    surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2), 30))
    pygame.display.update()

def valid_space(piece, grid):
    """Checks if a a piece is existing in a valid space on the grid"""
    pass

def main(win):
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    curr_piece = get_shape()
    next_piece = get_shape()

    clock = pygame.time.Clock()
    fall_time = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    curr_piece.x -= 1
                    if not valid_space(curr_piece, grid):
                        curr_piece.x +=1

                if event.key == pygame.K_RIGHT:
                    curr_piece.x += 1
                    if not valid_space(curr_piece, grid):
                        curr_piece.x -=1

                if event.key == pygame.K_DOWN:
                    curr_piece.y += 1
                    if not valid_space(curr_piece, grid):
                        curr_piece.y -=1

                if event.key == pygame.K_UP:
                    curr_piece.rotation += 1
                    if not valid_space(curr_piece, grid):
                        curr_piece.rotation -= 1

        draw_window(surface=win, grid=grid)                

def main_menu(win):
    main(win)

win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption("Tetris")
main_menu(win)