import tkinter as tk
from Board import Board
from Tile import Tile


class BoardGUI:
    SIZE = 374
    TILE_SIZE = SIZE / 9  # Each Tile is approximately 41.55x41.55.

    # Initializes a BoardGUI from a 2D array.
    def __init__(self, board: Board, location):
        self.board = board

        # Creating central frame for board with appropriate lines.
        self.root = location
        self.board_frame = tk.Frame(self.root.window, bg='white', highlightbackground="black", highlightthickness=3, borderwidth=0)
        self.__create_blank_board()

        # Creating 2D array of frames and labels from Board.
        self.board_widgets = self.__list_of_widgets()

    def clear(self):
        # Clear previous board.
        self.board_frame.destroy()
        self.board.clear()

        # Re-create empty board.
        self.board_frame = tk.Frame(self.root.window, bg='white', highlightbackground="black", highlightthickness=3, borderwidth=0)
        self.__create_blank_board()

    # Place known values in board.
    def fill_known_vals(self):
        for r in range(Board.SIZE):
            for c in range(Board.SIZE):
                # Place all tiles onto board that are not empty.
                if self.board.bo[r][c] != Board.EMPTY_VALUE:
                    adjust_x, adjust_y = BoardGUI.__determine_spacing(r, c, True)
                    tile_val = tk.Label(self.board_frame, text=self.board.bo[r][c], font=Tile.FONT, bg='white', fg='black')
                    tile_val.place(relx=adjust_x, rely=adjust_y)

    def insert_value(self, row, col):
        self.__insert_or_remove_value(row, col, self.board.bo[row][col], 'green')

    def remove_value(self, row, col):
        self.__insert_or_remove_value(row, col, 0, 'red')

    def __insert_or_remove_value(self, row, col, val, colour):
        adjust_x, adjust_y = BoardGUI.__determine_spacing(row, col, False)

        # Set frame border to parameter colour.
        self.board_widgets[row][col].border['highlightbackground'] = colour
        self.board_widgets[row][col].border['highlightcolor'] = colour
        # Set label value to parameter value.
        self.board_widgets[row][col].label['text'] = val

        # Place frame and label on main frame.
        self.board_widgets[row][col].border.place(relx=adjust_x, rely=adjust_y, relwidth=0.111, relheight=0.111)
        self.board_widgets[row][col].label.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        self.board_frame.update()

    # Creates the boxes, rows, and columns to distinguish tiles.
    def __create_blank_board(self):
        # Canvas to draw lines.
        canvas = tk.Canvas(self.board_frame, width=self.TILE_SIZE * 9, height=self.TILE_SIZE * 9, bg='white', borderwidth=0, highlightthickness=0)

        # Create all vertical and horizontal lines.
        ver_loc = 0
        hor_loc = 0
        for i in range(1, Board.SIZE):
            # Split board evenly into 9 sections.
            ver_loc += self.TILE_SIZE  # Move in x.
            hor_loc += self.TILE_SIZE  # Move in y.

            # Draw lines.
            if i % 3 == 0:  # Thick lines between boxes.
                canvas.create_line(0, hor_loc, self.SIZE, hor_loc, width=3)
                canvas.create_line(ver_loc, 0, ver_loc, self.SIZE, width=3)
            else:  # Thin lines between tiles.
                canvas.create_line(0, hor_loc, self.SIZE, hor_loc)
                canvas.create_line(ver_loc, 0, ver_loc, self.SIZE)
        canvas.place(relwidth=1, relheight=1)

    # Creates a 2D List containing Tile objects Frame widget with a Label widget within it (for number).
    def __list_of_widgets(self):
        total_widgets = []
        for r in range(Board.SIZE):
            col_widgets = []
            for c in range(Board.SIZE):
                # Frame takes size of tile's value.
                tile_border_frame = tk.Frame(self.board_frame, bg='white', highlightthickness=2)
                tile_val = tk.Label(tile_border_frame, text=self.board.bo[r][c], font=Tile.FONT, bg='white', fg='black')

                col_widgets.append(Tile(tile_border_frame, tile_val))
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
