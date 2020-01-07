import io
from unittest import TestCase
from unittest.mock import patch
import display


class TestDisplayAttackResults(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_attack_results_overkill_death_message(self, mock_stdout):
        attacker = {"Name": "Vlad"}
        defender = {"Name": "Orc", "Health": 10}
        expected_output = "----------------------------------------------------------------------------------------\n" \
                          "Vlad attacked for 11 damage\nOrc's current health is 10 which is not more than 11 so Orc " \
                          "has died!\n"
        display.display_attack_results(11, attacker, defender)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_attack_results_death_message(self, mock_stdout):
        attacker = {"Name": "Vlad"}
        defender = {"Name": "Orc", "Health": 10}
        expected_output = "----------------------------------------------------------------------------------------\n" \
                          "Vlad attacked for 10 damage\nOrc's current health is 10 which is not more than 10 so Orc " \
                          "has died!\n"
        display.display_attack_results(10, attacker, defender)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_attack_results_survival_message(self, mock_stdout):
        attacker = {"Name": "Vlad"}
        defender = {"Name": "Orc", "Health": 10}
        expected_output = "----------------------------------------------------------------------------------------\n" \
                          "Vlad attacked for 5 damage\nOrc's current health is 10 which is more than 5 so Orc has 5 " \
                          "health left!\n"
        display.display_attack_results(5, attacker, defender)
        self.assertEqual(mock_stdout.getvalue(), expected_output)
