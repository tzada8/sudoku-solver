import tkinter as tk
from boards import board
from solver import combine_funcs, find_empty_tile, valid_placement, empty_board
from tkinter import messagebox
from Tile import Tile


# Creates the boxes / rows / columns to distinguish each individual tile
def create_blank_board(location):
    # Create canvas to be able to draw lines
    canvas = tk.Canvas(location, width=one_tile * 9, height=one_tile * 9, bg='white', borderwidth=0,
                       highlightthickness=0)

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


# Creates a 2D List where each index is a Frame widget with a Label widget within it (for number)
def board_of_widgets(bo):
    total_widgets = []
    for r in range(len(bo)):
        col_widgets = []  # Creates List of 9 widgets, which are then added to total board widgets List
        for c in range(len(bo[r])):
            # Frame same size as empty tile
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


# Transfers all values from entry to 2D board List
def transfer_vals(entries):
    for r in range(len(board)):
        for c in range(len(board[r])):
            if len(entries[r][c].get()) != 0:  # Entry has input, so add accordingly
                board[r][c] = int(entries[r][c].get())
            else:  # Entry has no input, so insert a 0 in that spot
                board[r][c] = 0
    fill_known_vals(board, board_frame)


# Looks at entry in Entry widget and ensures it is acceptable; 1 character and a number
def validate(item):
    if len(item) == 0:  # If entry is empty, then it's valid
        return True
    elif len(item) == 1 and item.isdigit() and int(item) != 0:  # If entry is 1 character long and is a number
        return True
    else:  # Any other input is not valid
        return False


# User inputs values into entry boxes, such that they can solve any puzzle they want
def input_board_values(bo):
    # Enable SOLVE and RESET board buttons, and disable CREATE button
    solve_btn['state'] = 'normal'
    reset_board_btn['state'] = 'normal'
    create_board_btn['state'] = 'disabled'

    # Creates popup window so user can create their own board that needs to be solved
    create_bo_window = tk.Toplevel()
    create_bo_window.title("Create Sudoku Board")
    create_bo_window.geometry("400x475+180+130")
    create_bo_window.resizable(False, False)
    create_bo_window.iconbitmap('c:/Users/zadat/PycharmProjects/SudokuSolver/images/sudoku_logo.ico')
    create_bo_window.attributes("-topmost", True)
    create_bo_window.configure(bg='light grey')
    create_bo_window.grab_set()  # User cannot click off this window until it's closed
    create_bo_window.overrideredirect(True)

    # Creating central frame for board
    create_bo_frame = tk.Frame(create_bo_window, bg='white', highlightbackground="black", highlightthickness=3,
                               borderwidth=0)
    create_bo_frame.place(relx=0.025, rely=0.074, relwidth=0.95, relheight=0.8)

    # Create Label to provide user with instructions of what they should do
    instr_lbl = tk.Label(create_bo_window, text="Fill in the 9x9 grid with digits from 1 to 9",
                         font=btn_font, bg='light grey', fg='black')
    instr_lbl.place(rely=0.015, relwidth=1)

    create_blank_board(create_bo_frame)

    entries_board = []  # 2D List that keeps entry objects
    for r in range(len(bo)):
        col_entries = []  # Creates List of 9 widgets, which are then added to total board widgets List
        for c in range(len(bo[r])):
            # Validation such that user can only input a 1-character long number into Entry boxes
            vcmd = (create_bo_frame.register(validate), '%P')

            # Create entry and add to list
            entry = tk.Entry(create_bo_frame, font=tile_font, fg='black', justify='center', selectbackground='white',
                             width=2, cursor='xterm', bd=0, validate='key', validatecommand=vcmd)
            col_entries.append(entry)

            # Place entry onto screen with specified spacing
            adjust_x, adjust_y = determine_spacing(r, c, False)
            entry.place(relx=adjust_x + 0.015, rely=adjust_y + 0.015, relwidth=0.08, relheight=0.08)
        entries_board.append(col_entries)

    # Button to confirm entries; closes window and switches all values to what is listed in each entry
    confirm_btn = tk.Button(create_bo_window, text="Confirm", font=btn_font, bg='black', activebackground='white',
                            fg='white', activeforeground='black', borderwidth=0, cursor='hand2',
                            command=combine_funcs(lambda: transfer_vals(entries_board), create_bo_window.destroy))
    confirm_btn.place(relx=0.375, rely=0.895, relwidth=0.25, relheight=0.08)


# Clears all values from board; all values in 2D array are 0 and GUI board is empty (except for tile lines)
def clear_board(bo):
    global board_frame
    solve_btn['state'] = 'disabled'  # Disable SOLVE since board is empty; can't solve empty board
    reset_board_btn['state'] = 'disabled'
    create_board_btn['state'] = 'normal'  # Enable CREATE button so user can create new board to solve

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
    root.configure(background="light grey")

    # Creating central frame for board
    board_frame = tk.Frame(root, bg='white', highlightbackground="black", highlightthickness=3, borderwidth=0)
    board_frame.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.84444)

    one_tile = 374 / 9  # Each tile is approximately 41.55x41.55
    tile_font = ("Comic Sans", 18)
    btn_font = ("Helvetica", 12, 'bold')

    # Creates board with known values
    create_blank_board(board_frame)
    fill_known_vals(board, board_frame)

    # Each tile stored in 2D List as a widget, so called values can be easily changed instead of reinitialized
    board_widgets = board_of_widgets(board)

    # Button used to solve entire board by prompting user if they would like to see board being solved
    solve_btn = tk.Button(root, text="Solve", font=btn_font, bg='black', activebackground='white', fg='white',
                          activeforeground='black', borderwidth=0, cursor='hand2', state='disabled',
                          command=lambda: popup_ask_to_show(board, board_frame))
    solve_btn.place(relx=0.09, rely=0.9, relwidth=0.2, relheight=0.07)

    # Button only appears IF board is not empty, and used to have board be empty for new input
    reset_board_btn = tk.Button(root, text="Reset", font=btn_font, bg='black', activebackground='white', fg='white',
                                activeforeground='black', borderwidth=0, cursor='hand2', state='disabled',
                                command=lambda: clear_board(board))
    reset_board_btn.place(relx=0.4, rely=0.9, relwidth=0.2, relheight=0.07)

    # Button where use can input values into a board using entries
    create_board_btn = tk.Button(root, text="Create", font=btn_font, bg='black', activebackground='white', fg='white',
                                 activeforeground='black', borderwidth=0, cursor='hand2',
                                 command=lambda: input_board_values(board))
    create_board_btn.place(relx=0.715, rely=0.9, relwidth=0.2, relheight=0.07)

    root.mainloop()
