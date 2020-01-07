from unittest import TestCase
from unittest.mock import patch
import combat


class TestDecideAttackOrder(TestCase):
    @patch('random.randint', side_effect=[5, 4])
    def test_decide_attack_order_player_attacks_first(self, mock_roll_die):
        self.assertEqual(1, combat.decide_attack_order())

    @patch('random.randint', side_effect=[4, 5])
    def test_decide_attack_order_player_monster_attacks_first(self, mock_roll_die):
        self.assertEqual(-1, combat.decide_attack_order())

    @patch('random.randint', side_effect=[4, 4, 5, 4])
    def test_decide_attack_order_roll_again_because_of_draw(self, mock_roll_die):
        self.assertEqual(1, combat.decide_attack_order())
