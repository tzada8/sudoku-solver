from tkinter import Entry
from utils.colours import BASE
from utils.fonts import FONT
from board_interface.Board import Board


class CustomEntry(Entry):
    SIZE = 2 / 25  # 0.08.
    BUFFER = 3 / 200  # 0.015.

    def __init__(self, location):
        vcmd = (location.register(self.__validate), '%P')
        super().__init__(location, font=FONT["BOARD"], fg=BASE["BLACK"], selectbackground=BASE["BLACK"],
                         selectforeground=BASE["WHITE"], justify="center", width=2, cursor="xterm", bd=0,
                         validate="key", validatecommand=vcmd)

    # Places custom entry in frame.
    def place(self, x, y, width=SIZE, height=SIZE):
        super().place(relx=x + self.BUFFER, rely=y + self.BUFFER, relwidth=width, relheight=height)

    # Confirms input for Entry is acceptable; must be a 1 character-long number.
    @staticmethod
    def __validate(ans: str):
        is_1_char_long_num = len(ans) == 1 and ans.isdigit() and int(ans) != Board.EMPTY_VALUE
        return True if len(ans) == 0 or is_1_char_long_num else False
