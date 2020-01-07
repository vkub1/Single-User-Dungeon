from unittest import TestCase
from unittest.mock import patch
import combat


class TestMonster_hits_you_in_a_rush(TestCase):
    @patch('random.randint', side_effect=[2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_monster_hits_you_in_a_rush_monster_doesnt_attack_returns_true(self, mock_die_roll):
        player = {"Name": "Vlad", "Health": 10}
        monster = {"Name": "Orc", "Health": 5}
        for number in range(9):
            self.assertEqual(True, combat.monster_hits_you_in_a_rush(player, monster))

    @patch('random.randint', side_effect=[1, 9])
    def test_monster_hits_you_in_a_rush_surviving_attack_returns_true(self, mock_dice_roll):
        player = {"Name": "Vlad", "Health": 10}
        monster = {"Name": "Orc", "Health": 5}
        self.assertEqual(True, combat.monster_hits_you_in_a_rush(player, monster))

    @patch('random.randint', side_effect=[1, 10])
    def test_monster_hits_you_in_a_rush_dieing_to_attack_returns_false(self, mock_dice_roll):
        player = {"Name": "Vlad", "Health": 10}
        monster = {"Name": "Orc", "Health": 5}
        self.assertEqual(False, combat.monster_hits_you_in_a_rush(player, monster))

    @patch('random.randint', side_effect=[1, 11])
    def test_monster_hits_you_in_a_rush_being_overkilled_returns_false(self, mock_dice_roll):
        player = {"Name": "Vlad", "Health": 10}
        monster = {"Name": "Orc", "Health": 5}
        self.assertEqual(False, combat.monster_hits_you_in_a_rush(player, monster))