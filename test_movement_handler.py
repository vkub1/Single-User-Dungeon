import io
from unittest import TestCase
from unittest.mock import patch

import sud
import characters
import combat


class TestMovementHandler(TestCase):
    @patch('random.randint', side_effect=[2, 3, 4])
    def test_movement_handler_return_true_character_alive_when_character_heals(self, mock_stdout):
        for number in range(3):
            self.assertEqual(True, sud.movement_handler({"Name": "Vlad", "Health": 10}))

    @patch('random.randint', return_value=1)
    @patch('combat.fight_or_flee', return_value="quit")
    def test_movement_handler_returns_false_when_player_quits(self, mock_input, mock_dice_roll):
        self.assertEqual(False, sud.movement_handler({"Name": "Vlad", "Health": 10}))

    @patch('random.randint', side_effect=[1, 5, 6, 11])
    @patch('combat.fight_or_flee', return_value="fight")
    def test_movement_handler_returns_false_when_player_dies_in_combat(self, mock_input, mock_dice_roll):
        self.assertEqual(False, sud.movement_handler({"Name": "Vlad", "Health": 10}))


