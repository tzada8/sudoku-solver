from tkinter import Canvas
from colours import BASE
from BoardGUI import BoardGUI


class CustomCanvas(Canvas):
    DEFAULT_Y = 179 / 200  # 0.895.
    DEFAULT_HEIGHT = 2 / 25  # 0.08.
    FONT = ("Helvetica", 12, 'bold')

    def __init__(self, location):
        super().__init__(location, width=BoardGUI.SIZE, height=BoardGUI.SIZE, bg=BASE["WHITE"],
                         borderwidth=0, highlightthickness=0)

    # Places custom canvas on frame.
    def place(self):
        super().place(relwidth=1, relheight=1)
