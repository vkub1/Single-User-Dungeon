from unittest import TestCase
import characters
import map


class TestMove_character(TestCase):
    def test_move_character_north(self):
        board = map.make_board()
        player = characters.create_character()
        for index, coordinate in enumerate(board):
            player["Position"] = list(board[index])
            if board[index][0] != 0:
                expected_position = [player["Position"][0] - 1, player["Position"][1]]
                characters.move_character(player, "N")
                self.assertEqual(expected_position, player["Position"])

    def test_move_character_south(self):
        board = map.make_board()
        player = characters.create_character()
        for index, coordinate in enumerate(board):
            player["Position"] = list(board[index])
            if board[index][0] != 4:
                expected_position = [player["Position"][0] + 1, player["Position"][1]]
                characters.move_character(player, "S")
                self.assertEqual(expected_position, player["Position"])

    def test_move_character_east(self):
        board = map.make_board()
        player = characters.create_character()
        for index, coordinate in enumerate(board):
            player["Position"] = list(board[index])
            if board[index][1] != 4:
                expected_position = [player["Position"][0], player["Position"][1] + 1]
                characters.move_character(player, "E")
                self.assertEqual(expected_position, player["Position"])

    def test_move_character_west(self):
        board = map.make_board()
        player = characters.create_character()
        for index, coordinate in enumerate(board):
            player["Position"] = list(board[index])
            if board[index][1] != 0:
                expected_position = [player["Position"][0], player["Position"][1] - 1]
                characters.move_character(player, "W")
                self.assertEqual(expected_position, player["Position"])
