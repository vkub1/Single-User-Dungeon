import random
import combat
import display
import map
import characters
import doctest


def get_user_choice():
    """
    Return the direction the user inputted
    :return:Return the direction the user inputted
    """
    while True:
        direction = input("Please enter a direction as displayed above(type quit to exit): ").strip().upper()
        possible_directions = ["N", "S", "W", "E", "QUIT"]
        if direction not in possible_directions:
            print("Please enter only directions N, S, W, or E")
        else:
            if direction == "QUIT":
                return "quit"
            return direction


def validate_move(board: list, character: dict, direction: str) -> bool:
    """
    Return a bool representing a valid move.
    :param board: a list of tuples representing a game_board.
    :param character: a list of ints representing character coordinates.
    :param direction: a str representing a direction to move in.
    :precondition board: must be a list of tuples representing a board.
    :precondition character: must be a list of ints representing character coordinates.
    :precondition direction: must be a str representing a direction.
    :postcondition: Return a bool representing a valid move.
    :return: Return a bool representing a valid move.
    >>> validate_move([(0,0),(0,1),(1,0),(1,1)], {"Name":"Vlad", "Health":[10,10], "Position":[0, 0]}, "S")
    True
    >>> validate_move([(0,0),(0,1),(1,0),(1,1)], {"Name":"Vlad", "Health":[10,10], "Position":[0, 0]}, "N")
    False
    """
    if direction.strip().upper() == "N":
        return (character["Position"][0] - 1, character["Position"][1]) in board
    elif direction.strip().upper() == "S":
        return (character["Position"][0] + 1, character["Position"][1]) in board
    elif direction.strip().upper() == "W":
        return (character["Position"][0], character["Position"][1] - 1) in board
    elif direction.strip().upper() == "E":
        return (character["Position"][0], character["Position"][1] + 1) in board
    else:
        print("Please enter only directions shown above")
        return False


def check_if_exit_is_reached(character: dict) -> bool:
    """
    Return a boolean representing whether exit is reached or not.
    :param character: a list of character coordinates.
    :precondition character: must be a list of character coordinates.
    :return: Return a boolean representing whether exit is reached or not.

    >>> check_if_exit_is_reached({"Position": [4,4]})
    True

    >>> check_if_exit_is_reached({"Position": [1,1]})
    False
    """
    if character["Position"][0] == 4 and character["Position"][1] == 4:
        return True
    else:
        return False


def check_for_combat():
    """
    Return a bool representing whether or not combat happened.
    :return: Return a bool representing whether or not combat happened.
    """
    if random.randint(1, 4) == 1:
        return True
    else:
        return False


def movement_handler(character: dict) -> bool:
    """
    Return a bool representing whether your character is still alive after processing possible outcomes after movement.
    :param character: a dictionary with the following key value pairs "Health": [int,int] , "Position": [int, int] ,
    "Name": str.
    :precondition character: a dictionary with the following keys "Health": [int,int] , "Position": [int, int] , "Name":
     str.
    :postcondition: Return a bool representing whether your character is still alive.
    :return: Return a bool representing whether your character is still alive.
    """
    is_there_combat = check_for_combat()
    if is_there_combat:
        return combat.resolve_combat(character, combat.fight_or_flee(), characters.generate_monster())
    else:
        characters.heal_character(character)
        display.display_character_healing(character)
        return True


def game():
    """
    Plays a game for the user using user input.
    """
    display.display_game_scenario()
    board = map.make_board()
    player = characters.create_character()
    found_exit = False
    while not found_exit:
        display.print_current_position(board, player)
        direction = get_user_choice()
        if direction == "quit":
            print("You have either chosen to quit or died either way you failed your quest!")
            return
        valid_move = validate_move(board, player, direction)
        if valid_move:
            characters.move_character(player, direction)
            found_exit = check_if_exit_is_reached(player)
            if not found_exit:
                if not movement_handler(player):
                    print("You have either chosen to quit or died either way you failed your quest!")
                    return
        else:
            print("You can't go in that direction because it is a wall")
    display.display_game_ending()


def main():
    doctest.testmod()
    game()


if __name__ == "__main__":
    main()
