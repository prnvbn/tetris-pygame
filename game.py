import defs as ds

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

def convert_shape_format(shape):
    pass

def valid_space(shape, grid):
    pass

def check_lost(positions):
    pass

def get_shape():
    return 

def draw_text_middle(text, size, color, surface):  
    pass
   
def draw_grid(surface, row, col):
    pass

def clear_rows(grid, locked):
    pass

def draw_next_shape(shape, surface):
    pass

def draw_window(surface):
    pass

def main():
    pass

def main_menu():
    pass

main_menu()  # start game    