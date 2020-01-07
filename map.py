import display


def make_board():
    """
    Return a list of tuples representing a game_board.
    :return:Return a list of tuples representing a game_board.
    """
    return [(row, column) for row in range(5) for column in range(5)]


