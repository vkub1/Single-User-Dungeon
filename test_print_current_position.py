import io
from unittest import TestCase
from unittest.mock import patch
import display


class TestPrintCurrentPosition(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_current_position_test_move_all_directions(self, mock_stdout):
        expected_output = "x x x x x \n" + "x o x x x \n" + "x x x x x \n" + "x x x x x \n" + "x x x x _ \n"
        expected_output += "You can move south (enter S) north (enter N)  east (enter E) west (enter W) \n"
        display.print_current_position([(row, column) for row in range(5) for column in range(5)], {"Position": [1, 1]})
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_current_position_test_move_north_and_east(self, mock_stdout):
        expected_output = "x x x x x \n" + "x x x x x \n" + "x x x x x \n" + "x x x x x \n" + "o x x x _ \n"
        expected_output += "You can move north (enter N)  east (enter E) \n"
        display.print_current_position([(row, column) for row in range(5) for column in range(5)], {"Position": [4, 0]})
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_current_position_test_move_west_and_south(self, mock_stdout):
        expected_output = "x x x x o \n" + "x x x x x \n" + "x x x x x \n" + "x x x x x \n" + "x x x x _ \n"
        expected_output += "You can move south (enter S) west (enter W) \n"
        display.print_current_position([(row, column) for row in range(5) for column in range(5)], {"Position": [0, 4]})
        self.assertEqual(mock_stdout.getvalue(), expected_output)
