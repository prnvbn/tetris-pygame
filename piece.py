from defs import shapes
from defs import shape_colours

class Piece(object):
    
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape

        self.colour = shape_colours[shapes.index(shape)]
        self.rotation = 0