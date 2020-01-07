import io
from unittest import TestCase
from unittest.mock import patch
import display


class TestDisplayCharacterHealing(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_character_healing_2_health(self, mock_stdout):
        expected_output = ""
        for number in range(1, 8):
            expected_output += "Vlad set up for the night and no monsters attacked so you recovered 2 health\n" \
                              f"Vlad has {number + 2} health\n\n" \
                              "-------------------------------------------------------------------------------------\n"
            display.display_character_healing({"Name": "Vlad", "Health": number})
            self.assertEqual(expected_output, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_character_healing_1_health(self, mock_stdout):
        expected_output = "Vlad set up for the night and no monsters attacked so you recovered 1 health\n" \
                          "Vlad has 10 health\n\n" \
                          "-------------------------------------------------------------------------------------\n"
        display.display_character_healing({"Name": "Vlad", "Health": 9})
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_character_healing_nothing(self, mock_stdout):
        expected_output = "Vlad has had a peaceful rest because no monster attacked, but is already at max health\n" \
                          "-------------------------------------------------------------------------------------\n"
        display.display_character_healing({"Name": "Vlad", "Health": 10})
        self.assertEqual(mock_stdout.getvalue(), expected_output)
