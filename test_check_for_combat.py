from unittest import TestCase
from unittest.mock import patch
import sud


class TestCheck_for_combat(TestCase):
    @patch('random.randint', return_value=1)
    def test_check_for_combat_value_where_combat_happens(self, mock_roll_die):
        self.assertEqual(True, sud.check_for_combat())

    @patch('random.randint', side_effect=[2, 3, 4])
    def test_check_for_combat_all_values_where_combat_didnt_happen(self, mock_roll_die):
        for number in range(3):
            self.assertEqual(False, sud.check_for_combat())
