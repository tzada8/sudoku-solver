class Board:
    EMPTY_VALUE = 0
    VALUES = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    SIZE = len(VALUES)
    BOX_SIZE = int(SIZE / 3)

    def __init__(self, bo):
        self.set_bo(bo)

    # Neatly prints board to console formatted as a Sudoku Board.
    def print(self):
        for r in range(self.SIZE):
            for c in range(self.SIZE):
                print(self.bo[r][c], end=" ")
                is_box_col_border = (c + 1) % self.BOX_SIZE == 0
                is_not_last_col = (c + 1) != self.SIZE
                if is_box_col_border and is_not_last_col:
                    print("|", end=" ")
            print()

            is_box_row_border = (r + 1) % self.BOX_SIZE == 0
            is_not_last_row = (r + 1) != self.SIZE
            if is_box_row_border and is_not_last_row:
                num_dashes = (self.SIZE * 2 - 1) + 2 * 2
                for _ in range(num_dashes):
                    print("-", end="")
                print()

    # Sets all values in board to empty.
    def clear(self):
        for r in range(self.SIZE):
            for c in range(self.SIZE):
                self.bo[r][c] = self.EMPTY_VALUE

    # Finds next empty tile in board.
    def find_empty_tile(self):
        for r in range(self.SIZE):
            for c in range(self.SIZE):
                if self.bo[r][c] == self.EMPTY_VALUE:
                    return r, c  # Empty tile is at that location
        return None  # No more empty tiles

    # Gets entire board.
    def get_bo(self):
        return self.bo

    # Sets entire board.
    def set_bo(self, bo):
        # Confirm board is correct Sudoku Board size (9x9).
        if not Board.is_square(bo) or not len(bo) == self.SIZE:
            raise ValueError(f'board size must be {self.SIZE}x{self.SIZE}')
        self.bo = bo

    # Gets value at specified row and col.
    def get_val(self, row, col):
        return self.bo[row][col]

    # Set value at specified row and col.
    def set_val(self, row, col, val):
        self.__confirm_value(val)
        self.bo[row][col] = val

    # Confirms if "value" satisfies all conditions to insert it.
    def is_valid_placement(self, val, row, col):
        Board.__confirm_value(val)
        return not self.__is_in_row(val, row, col) and not self.__is_in_col(val, row, col) and not self.__is_in_box(val,
                                                                                                                    row,
                                                                                                                    col)

    # Determines if entire board is valid.
    def is_fully_valid(self):
        for r in range(self.SIZE):
            for c in range(self.SIZE):
                curr = self.bo[r][c]
                if curr != self.EMPTY_VALUE and not self.is_valid_placement(curr, r, c):
                    return False
        return True

    # Goes through entire Sudoku board solving it using recursion.
    def solve(self, board_view, is_visual):
        empty_location = self.find_empty_tile()
        if not empty_location:  # If board is full, then exit recursion.
            return True
        else:  # If still some empty tiles, then get current empty tile.
            row, col = empty_location

        for i in Board.VALUES:
            # If value is valid, place in board and move to next empty tile.
            if self.is_valid_placement(i, row, col):
                self.set_val(row, col, i)
                if is_visual:  # Only show solution if chooses to see steps.
                    board_view.insert_value(row, col, self.get_val(row, col))

                if self.solve(board_view, is_visual):
                    return True
                # Tile could not be filled, so empty it, then backtrack to previous step.
                self.set_val(row, col, Board.EMPTY_VALUE)
                if is_visual:  # Only show solution if chooses to see steps.
                    board_view.remove_value(row, col)
        return False

    # Determines if a board is squared.
    @staticmethod
    def is_square(bo):
        return all([len(i) == len(bo) for i in bo])

    # Raise error if "value" is invalid.
    @staticmethod
    def __confirm_value(val):
        if val not in Board.VALUES and val != Board.EMPTY_VALUE:
            raise ValueError(f'value must be between {Board.EMPTY_VALUE} and {max(Board.VALUES)}')

    # Confirms if "value" already exists in given row.
    def __is_in_row(self, val, row, col):
        for c in range(self.SIZE):
            if val == self.bo[row][c] and (c != col):
                return True
        return False

    # Confirms if "value" already exists in given col.
    def __is_in_col(self, val, row, col):
        for r in range(self.SIZE):
            if val == self.bo[r][col] and (r != row):
                return True
        return False

    # Confirms if "value" already exists in given box.
    def __is_in_box(self, val, row, col):
        box_r = row // self.BOX_SIZE  # Rows 0,1,2 = 0, 3,4,5 = 1, 6,7,8 = 2.
        box_c = col // self.BOX_SIZE  # Cols 0,1,2 = 0, 3,4,5 = 1, 6,7,8 = 2.

        # Determines range of box.
        lower_r = box_r * self.BOX_SIZE
        upper_r = box_r * self.BOX_SIZE + self.BOX_SIZE
        lower_c = box_c * self.BOX_SIZE
        upper_c = box_c * self.BOX_SIZE + self.BOX_SIZE

        # Loop exactly 3x3 times (for box) adding values to a list
        for r in range(lower_r, upper_r):
            for c in range(lower_c, upper_c):
                if val == self.bo[r][c] and (r != row and c != col):
                    return True
        return False
