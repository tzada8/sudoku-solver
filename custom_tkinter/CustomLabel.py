from tkinter import Label
from colours import BASE
from fonts import FONT


class CustomLabel(Label):
    def __init__(self, location, text, font=FONT["BOARD"], bg=BASE["WHITE"]):
        super().__init__(location, text=text, font=font, bg=bg, fg=BASE["BLACK"])
