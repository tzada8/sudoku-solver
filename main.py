from custom_tkinter.CustomWindow import CustomTk, CustomTopLevel
from custom_tkinter.CustomLabel import CustomLabel
from custom_tkinter.CustomButton import CustomButton
from custom_tkinter.PopUp import PopUp

from colours import WINDOW_BG
from fonts import FONT

from boards import default_board
from Board import Board
from board_interface.BoardView import BoardView
from board_interface.BoardCreate import BoardCreate


# Prompts to visually see solution as it's being solved.
def prompt_to_solve(board, board_view):
    if PopUp.question() == PopUp.CONFIRM:
        if not board.solve(board_view, True):
            PopUp.info()
        board_view.refresh(board)
    else:
        if not board.solve(board_view, False):
            PopUp.info()
        board_view.place_known_values(board)


# User inputs values into entry boxes, such that they can solve any puzzle they want
def custom_board(board: Board, board_view: BoardView):
    top_level = CustomTopLevel("Create Sudoku Board")
    board_create = BoardCreate(top_level)

    instructions = CustomLabel(top_level, "Fill in the 9x9 grid with digits from 1 to 9", FONT["BUTTON"], WINDOW_BG)
    instructions.place(rely=0.015, relwidth=1)

    confirm_btn = CustomButton(top_level, "Confirm", lambda: board_create.confirm(board, board_view))
    confirm_btn.place(0.375, 0.25)


def main():
    root = CustomTk("Sudoku Solver")

    # Backend and GUI Boards.
    board = Board(default_board)
    board_view = BoardView(root, board)

    # Button to prompt how board will be solved.
    solve_btn = CustomButton(root, "Solve", lambda: prompt_to_solve(board, board_view))
    solve_btn.place(0.09, 0.2)

    # Button to create custom board.
    create_board_btn = CustomButton(root, "Create", (lambda: custom_board(board, board_view)))
    create_board_btn.place(0.715, 0.2)

    root.mainloop()


if __name__ == "__main__":
    main()
