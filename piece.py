import environment

from defs import shapes
from defs import shape_colors

class Piece(object):
    
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape

        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0