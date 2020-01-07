from unittest import TestCase
import characters


class TestGenerateMonster(TestCase):
    def test_generate_monster(self):
        self.assertEqual({'Name': 'Spooky Scary Skeleton', 'Health': 5}, characters.generate_monster())
