from tkinter import Tk, Toplevel
from colours import WINDOW_BG

# Relative path to Sudoku Icon.
LOGO_PATH = "./images/sudoku_logo.ico"


class CustomTk(Tk):
    DEFAULT_WIDTH = 400
    DEFAULT_HEIGHT = 450
    DEFAULT_X = 150
    DEFAULT_Y = 75

    # Create main Tk() Window for app.
    def __init__(self, title, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT, x=DEFAULT_X, y=DEFAULT_Y):
        super().__init__()
        super().title(title)
        super().geometry(f'{width}x{height}+{x}+{y}')
        super().resizable(False, False)
        super().iconbitmap(LOGO_PATH)
        super().configure(background=WINDOW_BG)


class CustomTopLevel(Toplevel):
    DEFAULT_WIDTH = 400
    DEFAULT_HEIGHT = 475
    DEFAULT_X = 180
    DEFAULT_Y = 130

    # Create TopLevel() Window as child window in app.
    def __init__(self, title, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT, x=DEFAULT_X, y=DEFAULT_Y):
        super().__init__()
        super().title(title)
        super().geometry(f'{width}x{height}+{x}+{y}')
        super().resizable(False, False)
        super().iconbitmap(LOGO_PATH)
        super().configure(background=WINDOW_BG)

        # Adds attributes to the window to force it to stay active.
        super().attributes("-topmost", True)
        super().grab_set()
        super().overrideredirect(True)
