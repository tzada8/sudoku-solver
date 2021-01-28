from boards import board


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


# Goes through entire Sudoku board following the rules and solves it using recursion
def solve(bo):
    empty_location = find_empty_tile(bo)
    if not empty_location:  # If board is full, then exit recursion
        return True
    else:  # If still some empty tiles, then assign empty tile to row, and col
        row, col = empty_location

    for i in range(1, 10):  # Try numbers 1-9
        # Value works, so place it in board and try next empty tile
        if valid_placement(i, row, col, bo):
            bo[row][col] = i

            if solve(bo):
                return True
            # Tile could not be replaced so empty it, then backtrack to previous step
            bo[row][col] = 0
    return False

# this is a test comment x2

# Show board before and after solving with a space in between 2 boards
print_board(board)
solve(board)
print()
print_board(board)
