class Board:
    EMPTY_VALUE = 0
    SIZE = 9
    MAX_BOX_SIZE = int(SIZE / 3)

    # Initializes a board from a 2D array.
    def __init__(self, bo):
        # Confirm board is correct Sudoku Board size (9x9).
        if not Board.is_square(bo) or not len(bo) == self.SIZE:
            raise ValueError(f'Board size must be {self.SIZE}x{self.SIZE}.')
        self.bo = bo

    # Neatly prints board to console formatted as a Sudoku Board.
    def print_board(self):
        for r in range(len(self.bo)):
            for c in range(len(self.bo[r])):
                print(self.bo[r][c], end=" ")
                if (c + 1) % 3 == 0 and (c != 8):
                    print("|", end=" ")
            print()
            if (r + 1) % 3 == 0 and r != 8:
                for count in range(len(self.bo) * 2 + 3):
                    print("-", end="")
                print()

    # Sets all values in board to empty.
    def clear(self):
        for r in range(len(self.bo)):
            for c in range(len(self.bo[r])):
                self.bo[r][c] = self.EMPTY_VALUE

    # Finds next empty tile in board.
    def find_empty_tile(self):
        for r in range(len(self.bo)):
            for c in range(len(self.bo[r])):
                if self.bo[r][c] == self.EMPTY_VALUE:
                    return r, c  # Empty tile is at that location
        return None  # No more empty tiles

    # Confirms if "value" already exists in given row.
    def is_in_row(self, val, row):
        # for col_val in self.bo[row]:
        #     if val == col_val:
        #         return True
        # return False
        for c in range(len(self.bo)):
            if val == self.bo[row][c]:
                return True
        return False

    # Confirms if "value" already exists in given col.
    def is_in_col(self, val, col):
        for r in range(len(self.bo)):
            if val == self.bo[r][col]:
                return True
        return False

    # Confirms if "value" already exists in given box.
    def is_in_box(self, val, row, col):
        box_x = row // 3  # Rows 0,1,2 = 0, 3,4,5 = 1, 6,7,8 = 2.
        box_y = col // 3  # Cols 0,1,2 = 0, 3,4,5 = 1, 6,7,8 = 2.

        # Loop exactly 3x3 times (for box) adding values to a list
        for r in range(box_x * 3, box_x * 3 + 3):
            for c in range(box_y * 3, box_y * 3 + 3):
                if val == self.bo[r][c]:
                    return True
        return False

    # Confirms if "value" satisfies all conditions to insert it.
    def is_valid_placement(self, val, row, col):
        return not self.is_in_row(val, row) and not self.is_in_col(val, col) and not self.is_in_box(val, row, col)

    # Determines if entire board is valid.
    def is_customized_valid(self):
        for r in range(len(self.bo)):
            for c in range(len(self.bo[r])):
                curr = self.bo[r][c]
                if curr != 0 and not self.is_valid_placement(curr, r, c):
                    return False
        return True

    # Determines if a board is squared.
    @staticmethod
    def is_square(bo):
        return all([len(i) == len(bo) for i in bo])
