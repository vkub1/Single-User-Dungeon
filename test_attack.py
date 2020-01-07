from unittest import TestCase
import combat


class TestAttack(TestCase):
    def test_attack_subtracts_properly_with_health_remaining(self):
        player = {"Name": "Vlad", "Health": 10}
        monster = {"Name": "Orc", "Health": 5}
        combat.attack(6, monster, player)
        self.assertEqual(4, player["Health"])

    def test_attack_that_kills_exactly(self):
        player = {"Name": "Vlad", "Health": 10}
        monster = {"Name": "Orc", "Health": 5}
        combat.attack(10, monster, player)
        self.assertEqual(0, player["Health"])

    def test_attack_that_overkills(self):
        player = {"Name": "Vlad", "Health": 10}
        monster = {"Name": "Orc", "Health": 5}
        combat.attack(11, monster, player)
        self.assertEqual(0, player["Health"])
