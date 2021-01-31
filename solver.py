# Reads through sudoku board and prints it to console
def print_board(bo):
    for r in range(len(bo)):  # Go through each row
        for c in range(len(bo[r])):  # Go through each column of that row
            print(bo[r][c], end=" ")
            if (c + 1) % 3 == 0 and (c != 8):
                print("|", end=" ")
        print()
        if (r + 1) % 3 == 0 and r != 8:
            for count in range(len(bo) * 2 + 3):
                print("-", end="")
            print()


# Empties board by making every value in 2D array 0
def empty_board(bo):
    for r in range(len(bo)):
        for c in range(len(bo[r])):
            bo[r][c] = 0


# Finds next empty tile of board
def find_empty_tile(bo):
    for r in range(len(bo)):
        for c in range(len(bo[r])):
            if bo[r][c] == 0:
                return r, c  # Empty tile is at that location
    return None  # No more empty tiles


# Checks if "value" already exists in given row
def is_in_row(val, row, bo):
    return val in bo[row]


# Checks if "value" already exists in given column
def is_in_col(val, col, bo):
    for r in range(len(bo)):
        if val == bo[r][col]:
            return True
    return False


# Checks if "value" already exists in given box
def is_in_box(val, row, col, bo):
    box_x = row // 3  # rows 0,1,2=0, 3,4,5=1, 6,7,8=2
    box_y = col // 3  # cols 0,1,2=0, 3,4,5=1, 6,7,8=2

    # Loop exactly 3x3 times (for box) adding values to a list
    for r in range(box_x * 3, box_x * 3 + 3):
        for c in range(box_y * 3, box_y * 3 + 3):
            if val == bo[r][c] and (r != row and c != col):
                return True
    return False


# Determines if number added to given tile satisfies all conditions
def valid_placement(val, row, col, bo):
    return not is_in_row(val, row, bo) and not is_in_col(val, col, bo) and not is_in_box(val, row, col, bo)
