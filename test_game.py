import io
from unittest import TestCase
from unittest.mock import patch

import sud


class TestGame(TestCase):
    @patch('sud.get_user_choice', return_value='quit')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_quit_when_asked_for_direction(self, mock_stdout, mock_input):
        expected_output = "-------------------------------------------------------------------------------------\n" \
                          "You awaken in some sort of shrine and hear a soft voice taking to you\nHeroic Knight,\n" \
                          "I am the water goddess Aqua and I require your assistance.The orb you picked up during your"\
                          " last adventure is treasure that was stolen from my spring. As a result my shrine has been "\
                          "infested with monsters. Please bring the orb back to my spring.\n" \
                          "---------------------------------------------------------------------------------\n"\
                          "Your character is a knight(indicated by an o) and your goal for this scenario is to return " \
                          "the orb in your possession to the spring marked on your map (indicated by an _ )\n" \
                          "o x x x x \nx x x x x \nx x x x x \nx x x x x \nx x x x _ \nYou can move south (enter S) " \
                          "east (enter E) \nYou have either chosen to quit or died either way you failed your quest!\n"
        sud.game()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['S', "quit"])
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_quit_when_asked_to_fight_or_flee(self, mock_stdout, mock_roll_die, mock_input):
        expected_output = "-------------------------------------------------------------------------------------\n" \
                          "You awaken in some sort of shrine and hear a soft voice taking to you\nHeroic Knight,\n" \
                          "I am the water goddess Aqua and I require your assistance.The orb you picked up during your"\
                          " last adventure is treasure that was stolen from my spring. As a result my shrine has been "\
                          "infested with monsters. Please bring the orb back to my spring.\n" \
                          "---------------------------------------------------------------------------------\n" \
                          "Your character is a knight(indicated by an o) and your goal for this scenario is to return "\
                          "the orb in your possession to the spring marked on your map (indicated by an _ )\n" \
                          "o x x x x \nx x x x x \nx x x x x \nx x x x x \nx x x x _ \nYou can move south (enter S) " \
                          "east (enter E) \nA Spooky Scary Skeleton is attacking you do you flee or fight it. If you " \
                          "choose to flee there is a 10% chance to take 1 to 4 damage \n" \
                          "-------------------------------------------------------------------------------------\n"\
                          "You have either chosen to quit or died either way you failed your quest!\n"
        sud.game()
        self.assertEqual(mock_stdout.getvalue(), expected_output)


