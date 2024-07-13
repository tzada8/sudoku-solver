import unittest
from board_interface.Board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        self.board_empty = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.board_full = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [3, 1, 2, 6, 4, 5, 9, 7, 8],
            [9, 7, 8, 3, 1, 2, 6, 4, 5],
            [6, 4, 5, 9, 7, 8, 3, 1, 2],
            [2, 3, 1, 5, 6, 4, 8, 9, 7],
            [8, 9, 7, 2, 3, 1, 5, 6, 4],
            [5, 6, 4, 8, 9, 7, 2, 3, 1]
        ]
        self.board_1x3 = [[1, 2, 3]]
        self.board_3x3 = [
            [1, 2, 3],
            [3, 1, 2],
            [2, 3, 1]
        ]

    def test_init_invalid_board_due_to_not_square(self):
        with self.assertRaises(ValueError) as err:
            Board(self.board_1x3)
        self.assertEqual(str(err.exception), 'board size must be 9x9')

    def test_init_invalid_board_due_to_not_size_9x9(self):
        with self.assertRaises(ValueError) as err:
            Board(self.board_3x3)
        self.assertEqual(str(err.exception), 'board size must be 9x9')

    def test_init_valid_board(self):
        self.assertEqual(Board, type(Board(self.board)))

    def test_clear(self):
        bo = Board(self.board)
        bo.clear()
        self.assertEqual(bo.bo, self.board_empty)

    def test_find_empty_tile_empty_exists(self):
        self.assertEqual(Board(self.board).find_empty_tile(), (0, 2))

    def test_find_empty_tile_no_empty(self):
        self.assertEqual(Board(self.board_full).find_empty_tile(), None)

    def test_get_bo(self):
        self.assertEqual(Board(self.board).get_bo(), self.board)

    def test_set_bo(self):
        board = Board(self.board)
        board.set_bo(self.board_empty)
        self.assertEqual(board.bo, self.board_empty)

    def test_get_val_invalid_row(self):
        with self.assertRaises(IndexError) as err:
            Board(self.board).get_val(999, 0)
        self.assertEqual(str(err.exception), 'list index out of range')

    def test_get_val_invalid_col(self):
        with self.assertRaises(IndexError) as err:
            Board(self.board).get_val(0, 999)
        self.assertEqual(str(err.exception), 'list index out of range')

    def test_get_val_valid(self):
        self.assertEqual(Board(self.board).get_val(0, 0), 5)

    def test_set_val_invalid_row(self):
        with self.assertRaises(IndexError) as err:
            Board(self.board).set_val(999, 0, 1)
        self.assertEqual(str(err.exception), 'list index out of range')

    def test_set_val_invalid_col(self):
        with self.assertRaises(IndexError) as err:
            Board(self.board).set_val(0, 999, 1)
        self.assertEqual(str(err.exception), 'list assignment index out of range')

    def test_set_val_invalid_value(self):
        with self.assertRaises(ValueError) as err:
            Board(self.board).set_val(0, 0, 999)
        self.assertEqual(str(err.exception), 'value must be between 0 and 9')

    def test_set_val_valid(self):
        board = Board(self.board)
        board.set_val(0, 0, 1)
        self.assertEqual(board.bo[0][0], 1)

    def test_is_valid_placement_invalid_value(self):
        value = 999
        row = 0
        col = 0
        with self.assertRaises(ValueError) as err:
            Board(self.board).is_valid_placement(value, row, col)
        self.assertEqual(str(err.exception), 'value must be between 0 and 9')

    def test_is_valid_placement_invalid_row(self):
        value = 1
        row = 999
        col = 0
        with self.assertRaises(IndexError) as err:
            Board(self.board).is_valid_placement(value, row, col)
        self.assertEqual(str(err.exception), 'list index out of range')

    def test_is_valid_placement_invalid_col(self):
        value = 1
        row = 0
        col = 999
        with self.assertRaises(IndexError) as err:
            Board(self.board).is_valid_placement(value, row, col)
        self.assertEqual(str(err.exception), 'list index out of range')

    def test_is_valid_placement_value_exists_in_col_and_box(self):
        value = 8
        row = 0
        col = 2
        self.assertFalse(Board(self.board).is_valid_placement(value, row, col))

    def test_is_valid_placement_value_exists_in_row_and_box(self):
        value = 5
        row = 0
        col = 2
        self.assertFalse(Board(self.board).is_valid_placement(value, row, col))

    def test_is_valid_placement_value_exists_in_row_and_col(self):
        value = 7
        row = 8
        col = 0
        self.assertFalse(Board(self.board).is_valid_placement(value, row, col))

    def test_is_valid_placement_value_does_not_exist_in_any(self):
        value = 1
        row = 0
        col = 2
        self.assertTrue(Board(self.board).is_valid_placement(value, row, col))

    def test_is_fully_valid_with_invalid_board(self):
        bo = self.board_empty
        bo[0][0], bo[0][1], bo[1][0] = 1, 1, 1
        self.assertFalse(Board(bo).is_fully_valid())

    def test_is_fully_valid_with_valid_board(self):
        self.assertTrue(Board(self.board_full).is_fully_valid())

    def test_solve_with_solvable_board(self):
        expected = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]
        board = Board(self.board)
        self.assertTrue(board.solve(None, False))
        self.assertEqual(board.get_bo(), expected)

    def test_solve_with_unsolvable_board(self):
        unsolvable_board = [
            [5, 1, 6, 8, 4, 9, 7, 3, 2],
            [3, 0, 7, 6, 0, 5, 0, 0, 0],
            [8, 0, 9, 7, 0, 0, 0, 6, 5],
            [1, 3, 5, 0, 6, 0, 9, 0, 7],
            [4, 7, 2, 5, 9, 1, 0, 0, 6],
            [9, 6, 8, 3, 7, 0, 0, 5, 0],
            [2, 5, 3, 1, 8, 6, 0, 7, 4],
            [6, 8, 4, 2, 0, 7, 5, 0, 0],
            [7, 9, 1, 0, 5, 0, 6, 0, 8]
        ]
        board = Board(unsolvable_board)
        self.assertFalse(board.solve(None, False))

    def test_is_square_with_not_squared_board(self):
        self.assertFalse(Board.is_square(self.board_1x3))

    def test_is_square_with_squared_board(self):
        self.assertTrue(Board.is_square(self.board_3x3))


if __name__ == '__main__':
    unittest.main()
