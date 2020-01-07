import io
from unittest import TestCase
from unittest.mock import patch
import display


class TestDisplayGameEnding(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_game_ending(self, mock_stdout):
        expected_output = "Thanks for bringing my orb to me as thanks I will bestow upon you with a bunch of my finest"\
                          " treasures. I will now send you back home now.\nThanks for playing!\n"
        display.display_game_ending()
        self.assertEqual(mock_stdout.getvalue(), expected_output)
