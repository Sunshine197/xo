import unittest
import XO_board


class TestXOBoard(unittest.TestCase):
    def test_XO_board_move_to_x_outside_board(self):
        message = XO_board.move(6, 0, 'X')
        self.assertEqual(message, False)

    def test_XO_board_move_to_y_outside_board(self):
        message = XO_board.move(0, 6, 'X')
        self.assertEqual(message, False)

    def test_XO_board_move_to_occupied_cell(self):
        XO_board.move(0, 0, 'X')
        message = XO_board.move(0, 0, 'O')
        self.assertEqual(message, False)
