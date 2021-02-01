# Class that holds each tile's border colour (within frame) and tile value (within label)
class Tile:

    def __init__(self, border, number):
        self.border = border  # Holds frame with green/red border
        self.number = number  # Holds value of tile in center of frame
