from tkinter import Frame


class CustomFrame:
    DEFAULT_X = 1 / 40  # 0.025.
    DEFAULT_Y = 1 / 40  # 0.025.
    DEFAULT_WIDTH = 19 / 20  # 0.95.
    DEFAULT_HEIGHT = 38 / 45  # 0.84444.

    def __init__(self, location): # Maybe need to pass 'borderwidth' as parameter for one of the frames.
        self.frame = Frame(location, bg="white", highlightbackground="black", highlightthickness=3, borderwidth=0)

    # Places custom frame on the board.
    def place(self, x=DEFAULT_X, y=DEFAULT_Y, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT):
        self.frame.place(relx=x, rely=y, relwidth=width, relheight=height)
