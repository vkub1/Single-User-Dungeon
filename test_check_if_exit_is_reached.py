from unittest import TestCase
import sud
import map
import characters


class TestCheckIfExitIsReached(TestCase):
    def test_check_if_exit_is_reached_for_true(self):
        self.assertEqual(True, sud.check_if_exit_is_reached({"Position": [4, 4]}))

    def test_check_if_exit_is_reached_all_not_reached_positions(self):
        board = map.make_board()
        player = characters.create_character()
        for coordinate in board:
            player["Position"] = list([coordinate])
            self.assertEqual(False, sud.check_if_exit_is_reached(player))
