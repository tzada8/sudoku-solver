from custom_tkinter.CustomFrame import CustomFrame
from custom_tkinter.CustomLabel import CustomLabel
from custom_tkinter.CustomCanvas import CustomCanvas
from board_interface.Board import Board


class Tile:
    SIZE = CustomCanvas.SIZE / Board.SIZE  # Each Tile is approximately 41.55x41.55.
    FRAME_SIZE = 1 / Board.SIZE  # 0.111.
    LABEL_LOC = 1 / 10  # 0.1.
    LABEL_SIZE = 4 / 5  # 0.8.

    # Each tile has a frame for its border and a label centered inside the frame.
    def __init__(self, location, value):
        self.border = CustomFrame(location)
        self.label = CustomLabel(self.border, value)

    # Updates Tile's border colour and label.
    def update(self, colour, value):
        self.border["highlightbackground"] = colour
        self.border["highlightcolor"] = colour
        self.label["text"] = value

    # Places tile.
    def place(self, x, y):
        self.border.place(x, y, self.FRAME_SIZE, self.FRAME_SIZE)
        self.label.place(relx=self.LABEL_LOC, rely=self.LABEL_LOC, relwidth=self.LABEL_SIZE, relheight=self.LABEL_SIZE)
