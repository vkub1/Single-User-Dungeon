import random
import display
import characters


def combat_to_the_death(player: dict, monster: dict) -> bool:
    """
    Return a bool representing whether character survived combat
    :param player:
    :param monster:
    :return:
    """
    combat_unfinished = True
    while combat_unfinished:
        combat_round(player, monster)
        if player["Health"] <= 0:
            return False
        elif monster["Health"] <= 0:
            return True


def decide_attack_order() -> int:
    """
    Return an int that represents who attacks first.
    :return: Return an int that represents who attacks first.
    """
    keep_rolling = True
    while keep_rolling:
        first_die = random.randint(1, 20)
        second_die = random.randint(1, 20)
        if first_die > second_die:
            return 1  # player attacks first
        elif first_die < second_die:
            return -1  # monster attacks first
        else:
            keep_rolling = True


def resolve_combat(character: dict, your_action: str, monster: dict) -> bool:
    """
    Return a bool representing whether character is still alive or not after resolving combat.
    :param monster: a dict containing the following key:value pairs "Name": str, "Health": int.
    :param your_action: a string representing your action, "fight", "flee" or "quit".
    :param character: a dict containing the following key:value pairs "Name": str, "Health": int.
    :precondition monster: must be a containing the following key:value pairs "Name": str, "Health": int.
    :precondition your_action: must be a string representing your action, "fight", "flee" or "quit".
    :precondition character: must be a dict containing the following key:value pairs "Name": str, "Health": int.
    :postcondition: Return a bool representing whether character is still alive or not after resolving combat.
    :return:Return a bool representing whether character is still alive or not after resolving combat.
    """
    if your_action == "quit":
        return False
    elif your_action == "fight":
        return combat_to_the_death(character, monster)
    elif your_action == "flee":
        return monster_hits_you_in_a_rush(character, monster)


def monster_hits_you_in_a_rush(character: dict, monster: dict) -> bool:
    """
    Return a bool representing whether or not character survived monster attack while fleeing.
    :param monster: a dict containing the following key:value pairs "Name": str, "Health": int.
    :param character: a dict containing the following key:value pairs "Name": str, "Health": int.
    :precondition monster: must be a containing the following key:value pairs "Name": str, "Health": int.
    :precondition character: must be a dict containing the following key:value pairs "Name": str, "Health": int.
    :postcondition:Return a bool representing whether or not character survived monster attack while fleeing.
    :return: Return a bool representing whether or not character survived monster attack while fleeing.
    """
    if random.randint(1, 10) == 1:
        damage = random.randint(1, 4)
        attack(damage, monster, character)
        if character["Health"] <= 0:
            return False
        else:
            return True
    else:
        print("The monster decided to let you flee.")
        display.display_action_separator()
        return True


def fight_or_flee() -> str:
    """
    Return a str as a response based on user input.
    :return: Return a str as a response based on user input.
    """
    display.display_monster_attack()
    keep_asking = True
    while keep_asking:
        response = input("Enter 1 to fight and 2 to flee or (quit to exit the game): ")
        if response == "1":
            return "fight"
        elif response == "2":
            return "flee"
        elif response == "quit":
            return "quit"
        else:
            print("Please enter only the responses above")


def attack(damage: int, attacker: dict, defender: dict):
    """
    Subtracts damage from value stored in defender "Health" in defender dictionary.
    :param defender: a dict containing the following key:value pairs "Name": str, "Health": int.
    :param attacker: a dict containing the following key:value pairs "Name": str.
    :param damage: an int that represents damage done by the attacker.
    :precondition attacker: must be a dictionary containing the following key:value pairs "Name": str.
    :precondition defender: must be a dictionary containing the following key:value pairs "Name": str, "Health": int.
    :precondition damage: must be a positive int.
    """
    display.display_attack_results(damage, attacker, defender)
    defender["Health"] = defender["Health"] - damage
    if defender["Health"] < 0:
        defender["Health"] = 0


def combat_round(player: dict, monster: dict):
    """
    Subtracts health from player and monster based on the results of a combat round.
    :precondition player: must be a dictionary containing the following key:value pairs "Name": str, "Health": int.
    :precondition monster: must be a dictionary containing the following key:value pairs "Name": str, "Health": int.
    :postcondition: Subtracts health from player and monster based on the results of a combat round.
    """
    combatant_list = ["None", player, monster]
    combat_order = decide_attack_order()
    attack(random.randint(1, 6), combatant_list[combat_order], combatant_list[-combat_order])
    if combatant_list[-combat_order]["Health"] > 0:
        attack(random.randint(1, 6), combatant_list[-combat_order], combatant_list[combat_order])


def main():
    pass


if __name__ == "__main__":
    main()
