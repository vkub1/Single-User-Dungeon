from unittest import TestCase
import map
import sud
import characters

class TestValidateMove(TestCase):
    def test_validate_move_for_all_invalid_moves_north(self):
        board = map.make_board()
        for number in range(5):
            player = characters.create_character()
            player["Position"] = [0, number]
            if board[number][0] == 0:
                self.assertEqual(False, sud.validate_move(board, player, "N"))

    def test_validate_move_for_all_invalid_moves_south(self):
        board = map.make_board()
        for index, coordinate in enumerate(board):
            player = characters.create_character()
            player["Position"] = list(board[index])
            if board[index][0] == 4:
                self.assertEqual(False, sud.validate_move(board, player, "S"))

    def test_validate_move_for_all_invalid_moves_west(self):
        board = map.make_board()
        for index, coordinate in enumerate(board):
            player = characters.create_character()
            player["Position"] = list(board[index])
            if board[index][1] == 0:
                self.assertEqual(False, sud.validate_move(board, player, "W"))

    def test_validate_move_for_all_invalid_moves_east(self):
        board = map.make_board()
        for index, coordinate in enumerate(board):
            player = characters.create_character()
            player["Position"] = list(board[index])
            if board[index][1] == 4:
                self.assertEqual(False, sud.validate_move(board, player, "E"))

    def test_validate_move_for_all_valid_moves_north(self):
        board = map.make_board()
        for index, coordinate in enumerate(board):
            player = characters.create_character()
            player["Position"] = list(board[index])
            if board[index][0] != 0:
                self.assertEqual(True, sud.validate_move(board, player, "N"))

    def test_validate_move_for_all_valid_moves_south(self):
        board = map.make_board()
        for index, coordinate in enumerate(board):
            player = characters.create_character()
            player["Position"] = list(board[index])
            if board[index][0] != 4:
                self.assertEqual(True, sud.validate_move(board, player, "S"))

    def test_validate_move_for_all_valid_moves_west(self):
        board = map.make_board()
        for index, coordinate in enumerate(board):
            player = characters.create_character()
            player["Position"] = list(board[index])
            if board[index][1] != 0:
                self.assertEqual(True, sud.validate_move(board, player, "W"))

    def test_validate_move_for_all_valid_moves_east(self):
        board = map.make_board()
        for index, coordinate in enumerate(board):
            player = characters.create_character()
            player["Position"] = list(board[index])
            if board[index][1] != 4:
                self.assertEqual(True, sud.validate_move(board, player, "E"))

