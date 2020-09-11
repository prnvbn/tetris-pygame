import pygame
import random

from defs import *
from piece import Piece

def create_grid(locked_positions={}):
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
    grid = [[(0, 0, 0) for _ in range(board_cols)] for _ in range(board_rows)]

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


def draw_gridlines(surface, grid):
    """Draws the Tetris gameboard grid lines"""
    sx = top_left_x
    sy = top_left_y 

    for i in range(len(grid)):
        # Horixontal lines
        pygame.draw.line(surface, (128, 128, 128), (sx, sy + i*block_size), (sx + play_width, sy + i*block_size))
        for j in range(len(grid[i])):
            # Vertical lines
            pygame.draw.line(surface, (128, 128, 128), (sx + j*block_size, sy), (sx + j*block_size, sy + play_height))

def draw_window(surface, grid):
    """Draws the Tetris game window"""
    surface.fill((0, 0, 0))

    pygame.font.init()
    font  = pygame.font.SysFont('agencyfb', 60)
    label = font.render("Tetris", 1, (255, 255, 255))

    fill_grid(surface, grid)
    surface.blit(label, (top_left_x + play_width/2 - (label.get_width()/2), 30))
    draw_gridlines(surface, grid)
    pygame.display.update()

def valid_space(piece, grid):
    """Checks if a a piece is existing in a valid space on the grid"""
    valid_positions = [[(j, i) for j in range(board_cols) if grid[i][j] == (0, 0, 0)] for i in range(board_rows)]
    valid_positions = [pos for sublist in valid_positions for pos in sublist] #Flattening the above list

    piece_positions = convert_piece(piece)

    for pos in piece_positions:
        if pos not in valid_positions:
            if pos[1] > -1: # accounting for the y offset when the piece is spawned
                return False
    return True            


def convert_piece(piece):
    """Returns a list of positions for the given piece"""
    positions = []
    orientation = piece.shape[piece.rotation % len(piece.shape)]

    for i, line in enumerate(orientation):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((piece.x + j, piece.y +i)) 

    # Removing the existing period offsets (see defs.py)
    for i, pos in enumerate(positions):
        position[i] = (pos[0] - 2, pos[1] - 4)

def lost(positions):
    """Checks if the player has lost
    Checks if any of the positions are causing the player to 
    have the piece above the gameboard hieght limit"""
    for pos in positions:
        x, y = pos
        if y < 1:
            return True 



def main(win):
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    curr_piece = get_shape()
    next_piece = get_shape()

    clock = pygame.time.Clock()
    fall_time  = 0
    fall_speed = 0.27

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time/1_000 > fall_speed:
                fall_time = 0
                curr_piece.y += 1
                if not valid_space(curr_piece, grid) and curr_piece.y > 0:
                    curr_piece.y -= 1
                    change_piece = True    

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