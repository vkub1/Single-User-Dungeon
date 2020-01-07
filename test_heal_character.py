import io
from unittest import TestCase
from unittest.mock import patch

import characters


class TestHealCharacter(TestCase):
    def test_heal_character(self):
        player = characters.create_character()
        for numbers in range(1, 8):
            player["Health"] = numbers
            characters.heal_character(player)
            self.assertEqual(numbers + 2, player["Health"])

    def test_heal_character_heal_1_health(self):
        player = characters.create_character()
        player["Health"] = 9
        characters.heal_character(player)
        self.assertEqual(10, player["Health"])

    def test_heal_character_heal_nothing(self):
        player = characters.create_character()
        player["Health"]= 10
        characters.heal_character(player)
        self.assertEqual(10, player["Health"])
