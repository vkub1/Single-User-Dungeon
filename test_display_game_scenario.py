import io
from unittest import TestCase
from unittest.mock import patch

import display


class TestDisplayGameScenario(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_game_scenario(self, mock_stdout):
        expected_output = "-------------------------------------------------------------------------------------\n"\
                          "You awaken in some sort of shrine and hear a soft voice taking to you\nHeroic Knight,\n"\
                          "I am the water goddess Aqua and I require your assistance.The orb you picked up during " \
                          "your last adventure is treasure that was stolen from my spring. As a result my shrine has " \
                          "been infested with monsters. Please bring the orb back to my spring.\n" \
                          "---------------------------------------------------------------------------------\n"\
                          "Your character is a knight(indicated by an o) and your goal for this scenario is to return "\
                          "the orb in your possession to the spring marked on your map (indicated by an _ )\n"
        display.display_game_scenario()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

