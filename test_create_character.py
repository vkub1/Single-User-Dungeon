from unittest import TestCase
import characters


class TestCreateCharacter(TestCase):
    def test_create_character(self):
        self.assertEqual({"Name": "Honorable Knight", "Health": 10, "Position": [0, 0]}, characters.
                         create_character())
