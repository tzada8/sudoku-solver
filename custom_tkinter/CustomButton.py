from tkinter import Button
from colours import BASE
from fonts import FONT


# Allows a Button to run multiple commands.
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)

    return combined_func


class CustomButton(Button):
    DEFAULT_Y = 179 / 200  # 0.895.
    DEFAULT_HEIGHT = 2 / 25  # 0.08.

    def __init__(self, location, text, funcs):
        super().__init__(location, text=text, font=FONT["BUTTON"], bg=BASE["BLACK"], activebackground=BASE["WHITE"],
                         fg=BASE["WHITE"], activeforeground=BASE["BLACK"], borderwidth=0, cursor="hand2",
                         command=combine_funcs(funcs))

    # Places custom button on window.
    def place(self, x, width, y=DEFAULT_Y, height=DEFAULT_HEIGHT):
        super().place(relx=x, rely=y, relwidth=width, relheight=height)
