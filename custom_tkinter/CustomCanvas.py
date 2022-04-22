from tkinter import Canvas
from colours import BASE


class CustomCanvas(Canvas):
    SIZE = 374

    def __init__(self, location):
        super().__init__(location, width=self.SIZE, height=self.SIZE, bg=BASE["WHITE"],
                         borderwidth=0, highlightthickness=0)

    # Places custom canvas on frame.
    def place(self):
        super().place(relwidth=1, relheight=1)
