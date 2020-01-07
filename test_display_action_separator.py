import io
from unittest import TestCase
from unittest.mock import patch
import display


class TestDisplay_action_separator(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_action_separator(self, mock_stdout):
        expected_output = "-------------------------------------------------------------------------------------\n"
        display.display_action_separator()
        self.assertEqual(mock_stdout.getvalue(), expected_output)
