def display_game_scenario():
    """
    Print the game scenario.
    """
    display_action_separator()
    game_scenario = "You awaken in some sort of shrine and hear a soft voice taking to you\n" \
                    "Heroic Knight,\n" \
                    "I am the water goddess Aqua and I require your assistance.The orb you picked" \
                    " up during your last adventure is treasure that was stolen from my spring. As a result my shrine" \
                    " has been infested with monsters. Please bring the orb back to my spring."
    game_scenario += "\n---------------------------------------------------------------------------------\n" \
                     "Your character is a knight(indicated by an o) and your goal for this scenario is to return the " \
                     "orb in your possession to the spring marked on your map (indicated by an _ )"
    print(game_scenario)


def print_current_position(board: list, character: dict):
    """
    Print the board and character location.
    :param board: must be a list of tuples representing a game_board.
    :param character: must be a dict with "Position":[int,int] representing characters coordinates.
    :precondition board: must be a list of tuples representing a game_board.
    :precondition character: must be a dict with "Position":list(int,int) representing characters coordinates.
    :postcondition: Print the board and character location.
    """
    for i, location in enumerate(board):
        if board[i][0] == character["Position"][0] and board[i][1] == character["Position"][1]:
            print("o", end=" ")
            if board[i][1] == 4 and i != 0:
                print("")
        elif board[i][0] == 4 and board[i][1] == 4:
            print("_", end=" ")
            if board[i][1] == 4 and i != 0:
                print("")
        else:
            print("x", end=" ")
            if board[i][1] == 4 and i != 0:
                print("")
    print_possible_directions(board, character)


def display_monster_attack():
    """
    Print details about monster attacking you.
    """
    print("A Spooky Scary Skeleton is attacking you do you flee or fight it. If you choose to flee there is a 10% "
          "chance to take 1 to 4 damage ")
    display_action_separator()


def print_possible_directions(board: list, character: dict):
    """
    Print possible directions to move in based on character location in board.
    :param board: must be a list of tuples representing a game_board.
    :param character: must be a list with the characters coordinates.
    :precondition board: must be a list of tuples representing a game_board.
    :precondition character: must be a dictionary with a key called "Position" and a list characters coordinates as the
    value.
    :postcondition: Print possible directions to move in based on character location in board.
    """
    print("You can move", end=" ")
    if (character["Position"][0] + 1, character["Position"][1]) in board:
        print("south (enter S)", end=" ")
    if (character["Position"][0] - 1, character["Position"][1]) in board:
        print("north (enter N) ", end=" ")
    if (character["Position"][0], character["Position"][1] + 1) in board:
        print("east (enter E)", end=" ")
    if (character["Position"][0], character["Position"][1] - 1) in board:
        print("west (enter W)", end=" ")
    print("")


def display_action_separator():
    """
    Print a separator to separate text to make the game more readable.
    """
    print("-------------------------------------------------------------------------------------")


def display_character_healing(character: dict):
    """
    Print character healing details.
    :param character: a dictionary with a key "Name":str and "Health":[int,int].
    :precondition: character: must be a dictionary with a key "Name":str and "Health":[int,int].
    :postcondition: Print character healing details.
    """
    if character["Health"] == 9:
        print(character["Name"] + " set up for the night and no monsters attacked so you recovered 1 health")
        print(character["Name"] + " has 10 health\n")
    elif character["Health"] < 9:
        print(character["Name"] + " set up for the night and no monsters attacked so you recovered 2 health")
        print(character["Name"] + " has", character["Health"] + 2, "health\n")
    else:
        print(character["Name"] + " has had a peaceful rest because no monster attacked, but is already at max health")
    display_action_separator()


def display_game_ending():
    """
    Print the game ending.
    """
    game_end = "Thanks for bringing my orb to me as thanks I will bestow upon you with a bunch of my finest" \
               " treasures. I will now send you back home now.\nThanks for playing!"
    print(game_end)


def display_attack_results(damage: int, attacker: dict, defender: dict):
    """
    Print details of an attack such as who attacked who defended and how much damage was done.
    :param attacker: a dictionary containing the following key: value pairs "Name": str
    :param defender: a dictionary containing the following key: value pairs "Health": int, "Name": str
    :param damage: a positive int representing damage done.
    :precondition attacker: must be dictionary containing the following key: value pairs "Name": str
    :precondition defender: must be a dictionary containing the following key: value pairs "Health": int, "Name": str
    :precondition damage: must be a positive int representing damage done.
    :postcondition: Print details of an attack such as who attacked who defended and how much damage was done.
    """
    print("----------------------------------------------------------------------------------------")
    print(attacker["Name"], "attacked for", damage, "damage")
    defender_health = defender["Health"] - damage
    if defender_health <= 0:
        print(defender["Name"] + "'s current health is", defender["Health"], "which is not more than", damage,
              "so", defender["Name"], "has died!")
    else:
        print(defender["Name"] + "'s current health is", defender["Health"], "which is more than", damage,
              "so", defender["Name"], "has", defender_health, "health left!")