import copy

from custom_tkinter.CustomWindow import CustomTk, CustomTopLevel
from custom_tkinter.CustomButton import CustomButton
from custom_tkinter.CustomDropdown import CustomDropdown
from custom_tkinter.CustomLabel import CustomLabel
from custom_tkinter.PopUp import PopUp

from utils.colours import WINDOW_BG
from utils.fonts import FONT
from utils.boards import DEFAULT, BOARDS

from board_interface.Board import Board
from board_interface.BoardView import BoardView
from board_interface.BoardCreate import BoardCreate


# Prompts to visually see solution as it's being solved.
def prompt_to_solve():
    if PopUp.question() == PopUp.CONFIRM:
        __no_solution(True)
        board_view.refresh(board)
    else:
        __no_solution(False)
        board_view.place_known_values(board)


# Displays no solution exists message if none exists.
def __no_solution(is_visual):
    if not board.solve(board_view, is_visual):
        PopUp.info()


# Window to create custom board to solve.
def custom_board():
    top_level = CustomTopLevel("Create Sudoku Board")
    board_create = BoardCreate(top_level)

    instructions = CustomLabel(top_level, "Fill in the 9x9 grid with digits from 1 to 9", FONT["BUTTON"], WINDOW_BG)
    instructions.place(rely=0.015, relwidth=1)

    # Button to create custom board.
    confirm_btn = CustomButton(top_level, "Confirm", lambda: board_create.confirm(board, board_view))
    confirm_btn.place(0.375, 0.25)


# Callback when dropdown is selected, updating the backend and view boards with the chosen preset.
def choose_preset(selected_option):
    preset = copy.deepcopy(BOARDS[selected_option])
    board.set_bo(preset)
    board_view.refresh(board)


if __name__ == "__main__":
    root = CustomTk("Sudoku Solver")

    # Backend and GUI Boards.
    board = Board(copy.deepcopy(BOARDS[DEFAULT]))
    board_view = BoardView(root, board)

    # Button placements.
    __width = 0.2
    __solve_x = 0.09
    __create_x = 0.715
    __dropdown_x = (__solve_x + __create_x) / 2

    # Button to prompt how board will be solved.
    __solve_btn = CustomButton(root, "Solve", lambda: prompt_to_solve())
    __solve_btn.place(__solve_x, __width)

    # Select board from provided presets.
    __dropdown = CustomDropdown(root, list(BOARDS.keys()), choose_preset)
    __dropdown.place(__dropdown_x, __width)

    # Button to open custom board window.
    __create_board_btn = CustomButton(root, "Create", (lambda: custom_board()))
    __create_board_btn.place(__create_x, __width)

    root.mainloop()
