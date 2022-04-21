class Tile:
    FONT = ("Comic Sans", 18)

    def __init__(self, border, label):
        self.border = border  # Holds frame with green/red border
        self.label = label  # Holds value of tile in center of frame
