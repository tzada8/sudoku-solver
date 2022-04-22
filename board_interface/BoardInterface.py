from custom_tkinter.CustomFrame import CustomFrame
from custom_tkinter.CustomCanvas import CustomCanvas
from Board import Board
from Tile import Tile


class BoardInterface(CustomFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.__create_blank_board()

    # Destroys and re-creates the board_frame.
    def reset(self):
        self.destroy()
        super().__init__(self.master)
        self.__create_blank_board()

    # Determines necessary padding for Tile frame to be placed.
    @staticmethod
    def determine_spacing(row, col, is_value_known):
        adjust_x = Tile.FRAME_SIZE * col
        adjust_y = Tile.FRAME_SIZE * row

        # If placing a known value, then position number itself.
        if is_value_known:
            adjust_x += 0.03
            adjust_y += 0.013

        return adjust_x, adjust_y

    # Creates the boxes, rows, and columns to distinguish tiles.
    def __create_blank_board(self):
        canvas = CustomCanvas(self)

        # Create all vertical and horizontal lines.
        box_width = 3
        ver_loc = 0
        hor_loc = 0
        for i in range(1, Board.SIZE):
            # Split board evenly into 9 sections.
            ver_loc += Tile.SIZE  # Move in x.
            hor_loc += Tile.SIZE  # Move in y.

            # Draw lines.
            if i % Board.BOX_SIZE == 0:  # Thick lines between boxes.
                canvas.create_line(0, hor_loc, CustomCanvas.SIZE, hor_loc, width=box_width)
                canvas.create_line(ver_loc, 0, ver_loc, CustomCanvas.SIZE, width=box_width)
            else:  # Thin lines between tiles.
                canvas.create_line(0, hor_loc, CustomCanvas.SIZE, hor_loc)
                canvas.create_line(ver_loc, 0, ver_loc, CustomCanvas.SIZE)
        canvas.place()
