from unittest import TestCase
from unittest.mock import patch
import combat


class TestCombat_to_the_death(TestCase):
    @patch('random.randint',side_effect=[6, 4, 6])
    def test_combat_to_the_death_return_true_when_monster_dies(self, mock_dice_roll):
        player = {"Name": "Vlad", "Health": 10}
        monster = {"Name": "Orc", "Health": 5}
        self.assertEqual(True, combat.combat_to_the_death(player, monster))

    @patch('random.randint', side_effect=[4, 6, 11])
    def test_combat_to_the_death_return_false_when_character_dies(self, mock_dice_roll):
        player = {"Name": "Vlad", "Health": 10}
        monster = {"Name": "Orc", "Health": 5}
        self.assertEqual(False, combat.combat_to_the_death(player, monster))

    @patch('random.randint', side_effect=[4, 6, 8, 4, 5, 3, 3])
    def test_combat_to_the_death_loops_until_someone_dies(self, mock_dice_roll):
        player = {"Name": "Vlad", "Health": 10}
        monster = {"Name": "Orc", "Health": 5}
        self.assertEqual(True, combat.combat_to_the_death(player, monster))

