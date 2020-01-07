import io
from unittest import TestCase
from unittest.mock import patch
import display


class TestDisplayMonsterAttack(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_monster_attack(self, mock_stdout):
        expected_output = "A Spooky Scary Skeleton is attacking you do you flee or fight it. If you choose to flee " \
                          "there is a 10% chance to take 1 to 4 damage \n" \
                          "-------------------------------------------------------------------------------------\n"
        display.display_monster_attack()
        self.assertEqual(mock_stdout.getvalue(), expected_output)
