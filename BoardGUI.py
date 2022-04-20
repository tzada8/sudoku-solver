from Board import Board


class BoardGUI:
    # Initializes a board from a 2D array.
    def __init__(self, bo):
        if type(bo) != Board:
            raise ValueError('BoardGUI must be made from a Board.')
        self.bo = bo
