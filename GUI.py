import tkinter as tk
from boards import board
from solver import solve, combine_funcs


# Creates the boxes / rows / columns to distinguish each individual tile
def create_blank_board():
    # Create canvas to be able to draw lines
    canvas = tk.Canvas(frame, width=one_tile * 9, height=one_tile * 9, bg='white', bd=-10)

    # Create all vertical and horizontal lines
    ver_loc = 0
    hor_loc = 0
    for i in range(1, 9):
        # Entire screen evenly split into 9 sections
        ver_loc += one_tile  # Move in x
        hor_loc += one_tile  # Move in y

        # Draw lines
        if i % 3 == 0:  # Thick lines b/w boxes
            canvas.create_line(0, hor_loc, 450, hor_loc, width=3)
            canvas.create_line(ver_loc, 0, ver_loc, 450, width=3)
        else:  # Thin lines b/w tiles
            canvas.create_line(0, hor_loc, 450, hor_loc)
            canvas.create_line(ver_loc, 0, ver_loc, 450)
    canvas.place(relwidth=1, relheight=1)  # Place canvas in frame for entire size


# Function that inputs the already known values of the Sudoku board
def fill_known_vals(bo):
    # Values that help place the tile in its correct row and column
    adjust_x = 0.03
    adjust_y = 0.01

    for r in range(len(bo)):
        for c in range(len(bo[r])):
            # Place all tiles that aren't empty
            if bo[r][c] != 0:
                tile_val = tk.Label(frame, text=bo[r][c], font=tile_font, bg='white', fg='black')
                tile_val.place(relx=adjust_x, rely=adjust_y)
            adjust_x += 0.112
        adjust_x = 0.03
        adjust_y += 0.112


if __name__ == "__main__":
    # Initializing GUI
    root = tk.Tk()
    root.title("Sudoku Solver")
    root.geometry("400x450+150+75")
    root.resizable(False, False)  # Window doesn't need to resize
    root.iconbitmap('c:/Users/zadat/PycharmProjects/SudokuSolver/images/sudoku_logo2.ico')
    root.configure(background="#F8F8FF")

    # Creating central frame for board
    frame = tk.Frame(root, bg='white', highlightbackground="black", highlightthickness=3)
    frame.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.84444)

    one_tile = 374 / 9  # Each tile is approximately 41.55x41.55
    tile_font = ("comicsans", 18)
    btn_font = ("Helvetica", 12, 'bold')

    # Creates board with known values
    create_blank_board()
    fill_known_vals(board)

    solve_btn = tk.Button(root, text="Solve Board", font=btn_font, bg='black', activebackground='white', fg='white',
                          activeforeground='black', borderwidth=0, cursor='hand2',
                          command=combine_funcs(lambda: solve(board), lambda: fill_known_vals(board)))
    solve_btn.place(relx=0.036, rely=0.89, relwidth=0.3, relheight=0.08)

    #solve(board)
    #fill_known_vals(board)




    # HAVE A BUTTON ON MAIN WNIDOW THAT USER CAN CLICK TO INPUT VALUES INTO BOARD; SHOULD OPEN UP ANOTHER WINDOW
    #     THAT ACCEPTS KEYBOARD INPUT / TAB / ENTER / MOUSE CLICK ON ENTRY AND ALLOWS USER TO CREATE BOARD THEMSELF
    # ANOTHER TO "Solve" BOARD

    root.mainloop()
