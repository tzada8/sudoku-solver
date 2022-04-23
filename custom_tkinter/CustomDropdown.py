from tkinter import OptionMenu, StringVar
from utils.colours import BASE
from utils.fonts import FONT


class CustomDropdown(OptionMenu):
    DEFAULT_Y = 179 / 200  # 0.895.
    DEFAULT_HEIGHT = 2 / 25  # 0.08.

    def __init__(self, location, options, callback):
        self.clicked = StringVar()
        self.clicked.set(options[0])
        super().__init__(location, self.clicked, *options, command=callback)

        self.config(font=FONT["BUTTON"], bg=BASE["BLACK"], fg=BASE["WHITE"], highlightthickness=0, indicatoron=0)
        self["menu"].config(font=FONT["BUTTON"], bg="white", borderwidth=0)

    # Places custom dropdown on window.
    def place(self, x, width, y=DEFAULT_Y, height=DEFAULT_HEIGHT):
        super().place(relx=x, rely=y, relwidth=width, relheight=height)
