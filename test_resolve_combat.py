from unittest import TestCase
from unittest.mock import patch

import combat


class TestResolveCombat(TestCase):
    def test_resolve_combat_quit_returns_false(self):
        player = {"Name": "Vlad", "Health": 10}
        monster = {"Name": "Orc", "Health": 5}
        self.assertEqual(False, combat.resolve_combat(player, "quit", monster))

    @patch('random.randint', side_effect=[2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_resolve_combat_flee_no_monster_attack_returns_true(self, mock_dice_roll):
        player = {"Name": "Vlad", "Health": 10}
        monster = {"Name": "Orc", "Health": 5}
        for number in range(9):
            self.assertEqual(True, combat.resolve_combat(player, "flee", monster))

    @patch('random.randint', side_effect=[1, 9])
    def test_resolve_combat_flee_surviving_monster_attack_returns_true(self, mock_dice_roll):
        player = {"Name": "Vlad", "Health": 10}
        monster = {"Name": "Orc", "Health": 5}
        self.assertEqual(True, combat.resolve_combat(player, "flee", monster))

    @patch('random.randint', side_effect=[1, 10])
    def test_resolve_combat_flee_dieing_to_monster_attack_returns_false(self, mock_dice_roll):
        player = {"Name": "Vlad", "Health": 10}
        monster = {"Name": "Orc", "Health": 5}
        self.assertEqual(False, combat.resolve_combat(player, "flee", monster))

    @patch('random.randint', side_effect=[3, 2, 5])
    def test_resolve_combat_fighting_and_killing_monster_returns_true(self, mock_dice_roll):
        player = {"Name": "Vlad", "Health": 10}
        monster = {"Name": "Orc", "Health": 5}
        self.assertEqual(True, combat.resolve_combat(player, "fight", monster))

    @patch('random.randint', side_effect=[2, 3, 10])
    def test_resolve_combat_fighting_and_dieing_to_monster_returns_false(self, mock_dice_roll):
        player = {"Name": "Vlad", "Health": 10}
        monster = {"Name": "Orc", "Health": 5}
        self.assertEqual(False, combat.resolve_combat(player, "fight", monster))

