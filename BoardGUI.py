import pdb
import tkinter as tk
from custom_tkinter.CustomFrame import CustomFrame
from custom_tkinter.CustomCanvas import CustomCanvas
from colours import BORDER
from Board import Board
from Tile import Tile


class BoardGUI:
    # Initializes a BoardGUI from a 2D array.
    def __init__(self, board: Board, root):
        # Board's central frame with boxes drawn.
        self.root = root
        self.__create_board_frame()

        # 2D array storing board's values as frames/labels.
        self.board_widgets = self.__list_of_widgets(board)

    # Destroys and re-creates the board_frame.
    def reset(self):
        self.board_frame.destroy()
        self.__create_board_frame()

    # Place known values in board.
    def fill_known_vals(self, board: Board):
        for r in range(Board.SIZE):
            for c in range(Board.SIZE):
                # Place all tiles onto board that are not empty.
                curr_val = board.get_val(r, c)
                if curr_val != Board.EMPTY_VALUE:
                    adjust_x, adjust_y = BoardGUI.__determine_spacing(r, c, True)
                    tile_val = tk.Label(self.board_frame, text=curr_val, font=Tile.FONT, bg='white', fg='black')
                    tile_val.place(relx=adjust_x, rely=adjust_y)

    def insert_value(self, row, col, val):
        self.__update_tile(row, col, val, BORDER["INSERT"])

    def remove_value(self, row, col):
        self.__update_tile(row, col, Board.EMPTY_VALUE, BORDER["REMOVE"])

    def __update_tile(self, row, col, val, colour):
        adjust_x, adjust_y = BoardGUI.__determine_spacing(row, col, False)

        tile = self.board_widgets[row][col]
        tile.update(colour, val)
        tile.place(adjust_x, adjust_y)

        self.board_frame.update()

    # Creates board frame with boxes and places it on the screen.
    def __create_board_frame(self):
        self.board_frame = CustomFrame(self.root)
        self.__create_blank_board()
        self.board_frame.place()

    # Creates the boxes, rows, and columns to distinguish tiles.
    def __create_blank_board(self):
        canvas = CustomCanvas(self.board_frame)

        # Create all vertical and horizontal lines.
        ver_loc = 0
        hor_loc = 0
        for i in range(1, Board.SIZE):
            # Split board evenly into 9 sections.
            ver_loc += Tile.SIZE  # Move in x.
            hor_loc += Tile.SIZE  # Move in y.

            # Draw lines.
            if i % Board.BOX_SIZE == 0:  # Thick lines between boxes.
                canvas.create_line(0, hor_loc, CustomCanvas.SIZE, hor_loc, width=3)
                canvas.create_line(ver_loc, 0, ver_loc, CustomCanvas.SIZE, width=3)
            else:  # Thin lines between tiles.
                canvas.create_line(0, hor_loc, CustomCanvas.SIZE, hor_loc)
                canvas.create_line(ver_loc, 0, ver_loc, CustomCanvas.SIZE)
        canvas.place()

    # Creates a 2D List containing Tile objects Frame widget with a Label widget within it (for number).
    def __list_of_widgets(self, board):
        total_widgets = []
        for r in range(Board.SIZE):
            col_widgets = []
            for c in range(Board.SIZE):
                col_widgets.append(Tile(self.board_frame, board.get_val(r, c)))
            total_widgets.append(col_widgets)
        return total_widgets

    # Function that determines spacing for where the frame for the number will be placed: x and y
    @staticmethod
    def __determine_spacing(row, col, is_known_val):
        # If placing a known value, then positioning number itself
        if is_known_val:
            adjust_x = 0.03
            adjust_y = 0.013
        else:  # Else number is not known, so green/red border frame is being positioned
            adjust_x = 0
            adjust_y = 0
        change = 0.111

        # Determines how many squares need to be moved over starting from left side of col 0
        for _ in range(0, col):
            adjust_x += change
        # Determines how many squares need to be moved over starting from left side of row 0
        for _ in range(0, row):
            adjust_y += change

        # Make adjustments for thick borders
        # For col
        if 3 <= col < 6:
            adjust_x += 0.002
        elif col >= 6:
            adjust_x += 0.004
        # For row
        if 3 <= row < 6:
            adjust_y += 0.002
        elif row >= 6:
            adjust_y += 0.004

        return adjust_x, adjust_y
