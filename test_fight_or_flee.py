import io
from unittest import TestCase
from unittest.mock import patch
import combat


class TestFightOrFlee(TestCase):
    @patch('builtins.input', return_value="quit")
    def test_fight_or_flee_inputting_quit_returns_quit(self, mock_input):
        self.assertEqual("quit", combat.fight_or_flee())

    @patch('builtins.input', return_value="1")
    def test_fight_or_flee_entering_1_returns_fight(self, mock_input):
        self.assertEqual("fight", combat.fight_or_flee())

    @patch('builtins.input', return_value="2")
    def test_fight_or_flee_entering_2_returns_flee(self, mock_input):
        self.assertEqual("flee", combat.fight_or_flee())

    @patch('builtins.input', side_effect=["banana", "2"])
    def test_fight_or_flee_wrong_entry_requires_looping_until_correct_input(self, mock_input):
        self.assertEqual("flee", combat.fight_or_flee())

    @patch('builtins.input', side_effect=["banana", "2"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_fight_or_flee_wrong_entry_warning_message(self, mock_stdout, mock_input):
        expected_output = "A Spooky Scary Skeleton is attacking you do you flee or fight it. If you choose to flee " \
                          "there is a 10% chance to take 1 to 4 damage " \
                          "\n-------------------------------------------------------------------------------------" \
                          "\nPlease enter only the responses above\n"
        combat.fight_or_flee()
        self.assertEqual(mock_stdout.getvalue(), expected_output)
