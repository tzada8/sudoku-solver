from tkinter import Label
from utils.colours import BASE
from utils.fonts import FONT


class CustomLabel(Label):
    def __init__(self, location, text, font=FONT["BOARD"], bg=BASE["WHITE"]):
        super().__init__(location, text=text, font=font, bg=bg, fg=BASE["BLACK"])
