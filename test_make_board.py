from unittest import TestCase
import map


class TestMake_board(TestCase):
    def test_make_board(self):
        expected_return = [(row, column) for row in range(5) for column in range(5)]
        self.assertEqual(expected_return, map.make_board())
