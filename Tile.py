# Class that holds each tile's border colour (within frame) and tile value (within label)
class Tile:

    def __init__(self, frame, label):
        self.frame = frame  # Holds frame with green/red border
        self.label = label  # Holds value of tile in center of frame
