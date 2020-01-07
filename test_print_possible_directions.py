import io
from unittest import TestCase
from unittest.mock import patch
import display


class TestPrintPossibleDirections(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_possible_directions(self, mock_stdout):
        expected_output = "You can move south (enter S) north (enter N)  east (enter E) west (enter W) \n"
        display.print_possible_directions([(row, column) for row in range(5) for column in range(5)],
                                          {"Position": [1, 1]})
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_possible_direction_test_north_and_east(self, mock_stdout):
        expected_output = "You can move north (enter N)  east (enter E) \n"
        display.print_possible_directions([(row, column) for row in range(5) for column in range(5)],
                                          {"Position": [4, 0]})
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_possible_directions_test_west_and_south(self, mock_stdout):
        expected_output = "You can move south (enter S) west (enter W) \n"
        display.print_possible_directions([(row, column) for row in range(5) for column in range(5)],
                                          {"Position": [0, 4]})
        self.assertEqual(mock_stdout.getvalue(), expected_output)
