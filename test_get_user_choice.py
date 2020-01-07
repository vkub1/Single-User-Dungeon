import io
from unittest import TestCase
from unittest.mock import patch

import sud


class TestGetUserChoice(TestCase):
    @patch("builtins.input", side_effect=["N", "S", "W", "E", "quit"])
    def test_get_user_choice_test_possible_direction_entries(self, mock_input):
        direction_entries = ["N", "S", "W", "E", "quit"]
        for direction in direction_entries:
            self.assertEqual(direction, sud.get_user_choice())

    @patch("builtins.input", side_effect=[" n ", "s   ", "w   ", "  e", " QuIt "])
    def test_get_user_choice_test_possible_badly_entered_direction_entries(self, mock_input):
        direction_entries = ["N", "S", "W", "E", "quit"]
        for direction in direction_entries:
            self.assertEqual(direction, sud.get_user_choice())

    @patch("builtins.input", side_effect=["banana", "N"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_test_bad_input_warning(self,mock_stdout, mock_input):
        expected_value = "Please enter only directions N, S, W, or E\n"
        sud.get_user_choice()
        self.assertEqual(mock_stdout.getvalue(), expected_value)
