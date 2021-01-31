import tkinter as tk
from boards import board
from solver import find_empty_tile, valid_placement, empty_board
from tkinter import messagebox
from Tile import Tile


# Creates the boxes / rows / columns to distinguish each individual tile
def create_blank_board(location):
    # Create canvas to be able to draw lines
    canvas = tk.Canvas(location, width=one_tile * 9, height=one_tile * 9, bg='white', borderwidth=-100)

    # Create all vertical and horizontal lines
    ver_loc = 0
    hor_loc = 0
    for i in range(1, 9):
        # Entire screen evenly split into 9 sections
        ver_loc += one_tile  # Move in x
        hor_loc += one_tile  # Move in y

        # Draw lines
        if i % 3 == 0:  # Thick lines b/w boxes
            canvas.create_line(0, hor_loc, 500, hor_loc, width=3)
            canvas.create_line(ver_loc, 0, ver_loc, 500, width=3)
        else:  # Thin lines b/w tiles
            canvas.create_line(0, hor_loc, 500, hor_loc)
            canvas.create_line(ver_loc, 0, ver_loc, 500)
    canvas.place(relwidth=1, relheight=1)  # Place canvas in frame for entire size


# Function that determines spacing for where the frame for the number will be placed: x and y
def determine_spacing(row, col, is_known_val):
    # If placing a known value, then positioning number itself
    if is_known_val:
        adjust_x = 0.03
        adjust_y = 0.013
    else:  # Else number is not known, so green/red border frame is being positioned
        adjust_x = 0
        adjust_y = 0
    change = 0.111

    # Determines how many squares need to be moved over starting from left side of col 0
    for _ in range(0, col):
        adjust_x += change
    # Determines how many squares need to be moved over starting from left side of row 0
    for _ in range(0, row):
        adjust_y += change

    # Make adjustments for thick borders
    # For col
    if 3 <= col < 6:
        adjust_x += 0.002
    elif col >= 6:
        adjust_x += 0.004
    # For row
    if 3 <= row < 6:
        adjust_y += 0.002
    elif row >= 6:
        adjust_y += 0.004

    return adjust_x, adjust_y


# Function that inputs the already known values of the Sudoku board
def fill_known_vals(bo, location):
    for r in range(len(bo)):
        for c in range(len(bo[r])):
            # Place all tiles that aren't empty
            if bo[r][c] != 0:
                adjust_x, adjust_y = determine_spacing(r, c, True)
                tile_val = tk.Label(location, text=bo[r][c], font=tile_font, bg='white', fg='black')
                tile_val.place(relx=adjust_x, rely=adjust_y)


# Creates popup window to ask user if they want to see the board being solved or if they just want the answer
def popup_ask_to_show(bo, location):
    # Disable button so board cannot be "solved" again
    solve_btn['state'] = 'disabled'

    # Uses message boxes to ask if user wants to watch puzzle being solved or not
    response = messagebox.askquestion("Watch Solution Unfold?", "Would you like to watch the solution to the\n"
                                                                "Sudoku board unfold?")
    # If user wants to watch solution, then solve board with "True"
    if response == "yes":
        solve(bo, True)

        # Remove all green borders and create new frame to just have all values placed (no borders)
        location.destroy()
        final_frame = tk.Frame(root, bg='white', highlightbackground="black", highlightthickness=3)
        final_frame.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.84444)
        create_blank_board(final_frame)
        fill_known_vals(bo, final_frame)
    else:  # Else solve board with "False" since they just want answer
        solve(bo, False)
        fill_known_vals(bo, location)


# Creates a 2D array where each index is a Frame widget with a Label widget within it (for number)
def board_of_widgets(bo):
    total_widgets = []
    for r in range(len(bo)):
        col_widgets = []  # Creates List of 9 widgets, which are then added to total board widgets List
        for c in range(len(bo[r])):
            # Frame same size as empty tile, but with green border
            tile_border_frame = tk.Frame(board_frame, bg='white', highlightthickness=2)
            # Value placed in center of frame
            tile_val = tk.Label(tile_border_frame, text=bo[r][c], font=tile_font, bg='white', fg='black')

            col_widgets.append(Tile(tile_border_frame, tile_val))
        total_widgets.append(col_widgets)
    return total_widgets


# Try placing a value into board
def insert_num(row, col, bo):
    insert_or_remove_helper(row, col, bo[row][col], 'green')


# Value did not work in board, so need to backtrack / remove it from board
def remove_num(row, col):
    insert_or_remove_helper(row, col, 0, 'red')


# Helper function to simplify code that inserts/removes the tile into/out of the board
def insert_or_remove_helper(row, col, val, colour):
    adjust_x, adjust_y = determine_spacing(row, col, False)

    # Set frame border to red
    board_widgets[row][col].frame['highlightbackground'] = colour
    board_widgets[row][col].frame['highlightcolor'] = colour
    # Set label value to 0
    board_widgets[row][col].label['text'] = val

    # Place frame and label on screen
    board_widgets[row][col].frame.place(relx=adjust_x, rely=adjust_y, relwidth=0.111, relheight=0.111)
    board_widgets[row][col].label.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    board_frame.update()


# Goes through entire Sudoku board following the rules and solves it using recursion
def solve(bo, show_steps):
    empty_location = find_empty_tile(bo)
    if not empty_location:  # If board is full, then exit recursion
        return True
    else:  # If still some empty tiles, then assign empty tile to row, and col
        row, col = empty_location

    for i in range(1, 10):  # Try numbers 1-9
        # Value works, so place it in board and try next empty tile
        if valid_placement(i, row, col, bo):
            bo[row][col] = i
            if show_steps:  # Only show solution occurring if user wants to see it
                insert_num(row, col, bo)

            if solve(bo, show_steps):
                return True
            # Tile could not be filled, so empty it, then backtrack to previous step
            bo[row][col] = 0
            if show_steps:  # Only show solution occurring if user wants to see it
                remove_num(row, col)
    return False


# User inputs values into entry boxes, such that they can solve any puzzle they want
def input_board_values():
    global board_is_empty
    board_is_empty = False  # Change value since board is not empty

    return


# Clears all values from board; all values in 2D array are 0 and GUI board is empty (except for tile lines)
def clear_board(bo):
    global board_frame
    global board_is_empty
    board_is_empty = True  # Change value since board is now empty
    # Clears board from before
    board_frame.destroy()
    empty_board(bo)

    # Create board frame again and place border tiles on it
    board_frame = tk.Frame(root, bg='white', highlightbackground="black", highlightthickness=3, borderwidth=0)
    board_frame.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.84444)
    create_blank_board(board_frame)


if __name__ == "__main__":
    # Initializing GUI
    root = tk.Tk()
    root.title("Sudoku Solver")
    root.geometry("400x450+150+75")
    root.resizable(False, False)  # Window doesn't need to resize
    root.iconbitmap('c:/Users/zadat/PycharmProjects/SudokuSolver/images/sudoku_logo.ico')
    root.configure(background="#F8F8FF")

    # Creating central frame for board
    board_frame = tk.Frame(root, bg='white', highlightbackground="black", highlightthickness=3, borderwidth=0)
    board_frame.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.84444)

    one_tile = 374 / 9  # Each tile is approximately 41.55x41.55
    tile_font = ("Comic Sans", 18)
    btn_font = ("Helvetica", 12, 'bold')
    board_is_empty = True  # Used to determine if buttons should be shown/clickable


    # ABOVE VARIABLE board_is_empty IS ONLY USEFUL WHEN USER CAN INPUT VALUES FOR THEIR OWN BOARD
    # BOARD WILL NOT BE EMPTY LATER (WHEN FIXED SUCH THAT USER CAN ENTER VALUES)


    # Creates board with known values
    create_blank_board(board_frame)
    fill_known_vals(board, board_frame)

    # Each tile stored in 2D List as a widget, so called values can be easily changed instead of reinitialized
    board_widgets = board_of_widgets(board)

    # Button used to solve entire board by prompting user if they would like to see board being solved
    solve_btn = tk.Button(root, text="Solve", font=btn_font, bg='black', activebackground='white', fg='white',
                          activeforeground='black', borderwidth=0, cursor='hand2',
                          command=lambda: popup_ask_to_show(board, board_frame))
    solve_btn.place(relx=0.09, rely=0.9, relwidth=0.2, relheight=0.07)

    # Button only appears IF board is not empty, and used to have board be empty for new input
    reset_board_btn = tk.Button(root, text="Reset", font=btn_font, bg='black', activebackground='white', fg='white',
                                activeforeground='black', borderwidth=0, cursor='hand2',
                                command=lambda: clear_board(board))
    reset_board_btn.place(relx=0.4, rely=0.9, relwidth=0.2, relheight=0.07)

    # Button where use can input values into a board using entries
    create_board_btn = tk.Button(root, text="Create", font=btn_font, bg='black', activebackground='white', fg='white',
                                 activeforeground='black', borderwidth=0, cursor='hand2',
                                 command=input_board_values)
    create_board_btn.place(relx=0.715, rely=0.9, relwidth=0.2, relheight=0.07)

    root.mainloop()
