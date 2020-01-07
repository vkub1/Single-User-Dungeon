import io
from unittest import TestCase
from unittest.mock import patch
import combat


class TestCombatRound(TestCase):
    @patch('random.randint', side_effect=[5, 4, 5])
    def test_combat_round_attacker_kills_defender_exactly(self, mock_roll_die):
        expected_values = [10, 0]  # [player_health, monster_health]
        player = {"Name": "Vlad", "Health": 10}
        monster = {"Name": "Orc", "Health": 5}
        combat.combat_round(player, monster)
        self.assertEqual([player["Health"], monster["Health"]], expected_values)

    @patch('random.randint', side_effect=[5, 4, 5])
    def test_combat_round_attacker_overkills_defender_health_values(self, mock_roll_die):
        expected_values = [10, 0]  # [player_health, monster_health]
        player = {"Name": "Vlad", "Health": 10}
        monster = {"Name": "Orc", "Health": 5}
        combat.combat_round(player, monster)
        self.assertEqual([player["Health"], monster["Health"]], expected_values)

    @patch('random.randint', side_effect=[5, 4, 4, 9])
    def test_combat_round_both_attack_and_dont_kill_health_values(self, mock_roll_die):
        expected_values = [1, 1]  # [player_health, monster_health]
        player = {"Name": "Vlad", "Health": 10}
        monster = {"Name": "Orc", "Health": 5}
        combat.combat_round(player, monster)
        self.assertEqual([player["Health"], monster["Health"]], expected_values)

    @patch('random.randint', side_effect=[5, 4, 4, 10])
    def test_combat_round_player_attacks_doesnt_kill_and_dies_exactly(self, mock_roll_die):
        expected_values = [0, 1]  # [player_health, monster_health]
        player = {"Name": "Vlad", "Health": 10}
        monster = {"Name": "Orc", "Health": 5}
        combat.combat_round(player, monster)
        self.assertEqual([player["Health"], monster["Health"]], expected_values)

    @patch('random.randint', side_effect=[5, 4, 4, 11])
    def test_combat_round_player_attacks_doesnt_kill_and_overkilled(self, mock_roll_die):
        expected_values = [0, 1]  # [player_health, monster_health]
        player = {"Name": "Vlad", "Health": 10}
        monster = {"Name": "Orc", "Health": 5}
        combat.combat_round(player, monster)
        self.assertEqual([player["Health"], monster["Health"]], expected_values)