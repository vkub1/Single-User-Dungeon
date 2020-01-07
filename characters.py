import display
import doctest


def create_character() -> dict:
    """
    Return a dictionary of character details.
    :postcondition: Return a dictionary of character details.
    :return:Return a dictionary of character details.

    >>> create_character()
    {'Name': 'Honorable Knight', 'Health': 10, 'Position': [0, 0]}
    """
    return {"Name": "Honorable Knight", "Health": 10, "Position": [0, 0]}


def generate_monster() -> dict:
    """
    Return a dictionary of monster details.
    :postcondition: Return a dictionary of monster details.
    :return:Return a dictionary of monster details.

    >>> generate_monster()
    {'Name': 'Spooky Scary Skeleton', 'Health': 5}
    """
    return {"Name": "Spooky Scary Skeleton", "Health": 5}


def heal_character(character: dict):
    """
    Increases character current Health based on the current amount.
    :param character: A dictionary of character details.
    :precondition character: must be a dictionary of character details.
    :postcondition: Increases character current Health based on the current amount.

    >>> heal_character({"Name":"Honorable Knight", "Health": [10,6]})
    Honorable Knight set up for the night and no monsters attacked so you recovered 2 health
    Honorable Knight has 8 health
    <BLANKLINE>
    -------------------------------------------------------------------------------------

    """
    if character["Health"] < 9:
        character["Health"] += 2
    elif character["Health"] == 9:
        character["Health"] += 1


def move_character(character: dict, direction: str):
    """
    Modifies character coordinates in character dictionary based on the direction.
    :param character: a dictionary representing a character.
    :param direction: a str representing a direction to move in.
    :precondition direction: must be a str representing a direction.
    :postcondition: Modifies character coordinates in character dictionary based on the direction.
    """
    if direction == "N":
        character["Position"][0] -= 1
    elif direction == "S":
        character["Position"][0] += 1
    elif direction == "W":
        character["Position"][1] -= 1
    else:
        character["Position"][1] += 1

