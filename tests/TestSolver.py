import unittest

from solver import *


# Run tests `python -m unittest discover tests`.

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.word = "crazy"

    def test_empty_board_no_cells(self):
        board = [[]]
        expected = [[]]
        empty_board(board)
        self.assertEqual(board, expected)

    def test_empty_board_multiple_in_row(self):
        board = [[1, 2, 3]]
        expected = [[0, 0, 0]]
        empty_board(board)
        self.assertEqual(board, expected)

    def test_empty_board_only_multiple_in_column(self):
        board = [[1], [2], [3]]
        expected = [[0], [0], [0]]
        empty_board(board)
        self.assertEqual(board, expected)

    def test_empty_board_multiple_in_rows_and_columns(self):
        board = [
            [1, 2, 3],
            [3, 1, 2],
            [2, 3, 1]
        ]
        expected = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        empty_board(board)
        self.assertEqual(board, expected)

    def test_find_empty_tile_no_cells(self):
        board = [[]]
        expected = None
        self.assertEqual(find_empty_tile([[]]), expected)

    def test_find_empty_tile_beginning_of_single_row(self):
        board = [[0, 2, 3]]
        expected = (0, 0)
        self.assertEqual(find_empty_tile(board), expected)

    def test_find_empty_tile_end_of_single_row(self):
        board = [[1, 2, 0]]
        expected = (0, 2)
        self.assertEqual(find_empty_tile(board), expected)

    def test_find_empty_tile_beginning_of_single_column(self):
        board = [[0], [2], [3]]
        expected = (0, 0)
        self.assertEqual(find_empty_tile(board), expected)

    def test_find_empty_tile_end_of_single_column(self):
        board = [[1], [2], [0]]
        expected = (2, 0)
        self.assertEqual(find_empty_tile(board), expected)

    def test_find_empty_tile_filled_board_empty_exists(self):
        board = [
            [1, 2, 3],
            [3, 0, 2],
            [2, 3, 1]
        ]
        expected = (1, 1)
        self.assertEqual(find_empty_tile(board), expected)

    def test_find_empty_tile_filled_board_empty_does_not_exist(self):
        board = [
            [1, 2, 3],
            [3, 1, 2],
            [2, 3, 1]
        ]
        expected = None
        self.assertEqual(find_empty_tile(board), expected)

    def test_is_in_row_invalid_row(self):
        board = [[1]]
        invalid = 4
        self.assertRaises(IndexError, is_in_row(1, invalid, 0, board))

    def test_is_in_row_invalid_column(self):
        board = [[1]]
        invalid = 4
        self.assertRaises(IndexError, is_in_row(1, 0, invalid, board))

    def test_is_in_row_value_not_found(self):
        board = [[1, 2, 3, 0]]
        self.assertRaises(IndexError, is_in_row(9, 0, 3, board))

    def test_is_in_col_invalid_row(self):
        board = [[1]]
        invalid = 4
        self.assertRaises(IndexError, is_in_col(1, invalid, 0, board))

    def test_is_in_col_invalid_column(self):
        board = [[1]]
        invalid = 4
        self.assertRaises(IndexError, is_in_col(1, 0, invalid, board))


if __name__ == '__main__':
    unittest.main()