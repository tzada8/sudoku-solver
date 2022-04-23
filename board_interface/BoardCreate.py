from custom_tkinter.PopUp import PopUp
from custom_tkinter.CustomEntry import CustomEntry

from board_interface.BoardInterface import BoardInterface
from board_interface.BoardView import BoardView
from board_interface.Board import Board


class BoardCreate(BoardInterface):
    Y = 37 / 500  # 0.074.
    HEIGHT = 4 / 5  # 0.8.

    def __init__(self, parent):
        super().__init__(parent)
        self.widgets = self.__list_of_widgets()
        self.place(y=self.Y, height=self.HEIGHT)

    # Confirms valid board created and updates BoardView and Board. If not valid, then shows error message.
    def confirm(self, board: Board, board_view: BoardView):
        confirm_board = self.to_board()
        if confirm_board.is_fully_valid():
            board_view.refresh(confirm_board)
            board.set_bo(confirm_board.get_bo())
            self.master.destroy()
        else:
            PopUp.error(self.master)

    # Converts created BoardInterface to a Board.
    def to_board(self):
        return Board([[int(val.get() or 0) for val in row] for row in self.widgets])

    # Creates a 2D List of Entries for custom boards.
    def __list_of_widgets(self):
        return [[self.__create_and_place_entry(row, col) for col in range(Board.SIZE)] for row in range(Board.SIZE)]

    # Creates and places entry widgets.
    def __create_and_place_entry(self, r, c):
        entry = CustomEntry(self)
        adjust_x, adjust_y = self.determine_spacing(r, c, False)
        entry.place(adjust_x, adjust_y)
        return entry
