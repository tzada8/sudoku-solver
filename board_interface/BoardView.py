from custom_tkinter.CustomLabel import CustomLabel
from utils.colours import BORDER
from board_interface.BoardInterface import BoardInterface
from board_interface.Board import Board
from board_interface.Tile import Tile


class BoardView(BoardInterface):
    def __init__(self, parent, board: Board):
        super().__init__(parent)
        self.place_known_values(board)
        self.place()

    # Refreshes view board by destroying previous board, adding new values, then placing again.
    def refresh(self, board: Board):
        self.reset()
        self.place_known_values(board)
        self.place()

    # Place known values on board interface.
    def place_known_values(self, board: Board):
        self.widgets = self.__list_of_widgets(board)
        for row in range(Board.SIZE):
            for col in range(Board.SIZE):
                # Place all tiles onto board that are not empty.
                curr_val = board.get_val(row, col)
                if curr_val != Board.EMPTY_VALUE:
                    adjust_x, adjust_y = self.determine_spacing(row, col, True)
                    CustomLabel(self, curr_val).place(relx=adjust_x, rely=adjust_y)

    def insert_value(self, row, col, val):
        self.__update_tile(row, col, val, BORDER["INSERT"])

    def remove_value(self, row, col):
        self.__update_tile(row, col, Board.EMPTY_VALUE, BORDER["REMOVE"])

    def __update_tile(self, row, col, val, colour):
        adjust_x, adjust_y = self.determine_spacing(row, col, False)
        tile = self.widgets[row][col]
        tile.update(colour, val)
        tile.place(adjust_x, adjust_y)
        self.update()

    # Creates a 2D List of Tile objects from the original board.
    def __list_of_widgets(self, board):
        return [list(map(lambda val: Tile(self, val), row)) for row in board.get_bo()]
