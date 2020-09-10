import defs as ds

def create_grid(locked_positions={}):
    # initialising a 20 x 10 grid
    grid = [[(0, 0, 0) for _ in range(10)] for _ in range(20)]