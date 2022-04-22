from tkinter import Frame, Label
from custom_tkinter.CustomFrame import CustomFrame
from colours import BASE


class Tile:
    FONT = ("Comic Sans", 18)
    REL_FRAME_SIZE = 1 / 9  # 0.111.
    REL_LABEL_LOC = 1 / 10  # 0.1.
    REL_LABEL_SIZE = 4 / 5  # 0.8.

    def __init__(self, location, value):
        # Frame for green/red border.
        self.border = CustomFrame(location)

        # Value in center of frame.
        self.label = Label(self.border, text=value, font=self.FONT, bg=BASE["WHITE"], fg=BASE["BLACK"])

    # Updates Tile's border colour and label.
    def update(self, colour, value):
        self.border["highlightbackground"] = colour
        self.border["highlightcolor"] = colour
        self.label["text"] = value

    # Places tile.
    def place(self, x, y):
        self.border.place(x, y, self.REL_FRAME_SIZE, self.REL_FRAME_SIZE)
        self.label.place(relx=self.REL_LABEL_LOC, rely=self.REL_LABEL_LOC, relwidth=self.REL_LABEL_SIZE, relheight=self.REL_LABEL_SIZE)
