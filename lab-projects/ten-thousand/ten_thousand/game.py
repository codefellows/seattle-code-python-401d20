from ten_thousand.game_logic import GameLogic

dice_roller = GameLogic.roll_dice


def play(roller=GameLogic.roll_dice, num_rounds=20):
    """
    play Ten Thousand game

    Args:
        roller: optional dice rolling function. Default is GameLogic.roll_dice
        num_rounds: optional number of rounds. Default of 20

    Returns:
        None

    """
    global dice_roller

    dice_roller = roller

    choice = invite_to_play()

    if choice == "y":
        start_game(num_rounds)
    else:
        decline_game()


def invite_to_play():
    """
    Display welcome message and prompt them to play or decline
    Returns:
        string "y" or "n"
    """
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    choice = input("> ")
    return choice


def start_game(num_rounds):
    """
    Start the game and run for given number of rounds
    Args:
        num_rounds:

    Returns:
        None
    """
    round_num = 1
    max_round = num_rounds
    total_points = 0

    while round_num <= max_round:
        round_result = do_round(round_num)
        if round_result == -1:
            break

        print(f"You banked {round_result} points in round {round_num}")

        total_points += round_result

        print(f"Total score is {total_points} points")
        round_num += 1

    print(f"Thanks for playing. You earned {total_points} points")


def do_round(round_num):
    """
    Play a round of the game
    Args:
        round_num:

    Returns:
        integer for number of points scored in the round
        -1 has special meaning for "quit"
    """
    print(f"Starting round {round_num}")

    num_dice = 6
    unbanked_points = 0

    # loop here until a quit, bank or zilch
    while True:
        roll = do_roll(num_dice)

        if GameLogic.calculate_score(roll) == 0:
            zilch()
            return 0

        keepers = confirm_keepers(roll)

        # TODO: I don't like these varying ways to handle a quit
        if len(keepers) == 0:
            return -1

        unbanked_points += GameLogic.calculate_score(keepers)

        num_dice -= len(keepers)

        if num_dice == 0:  # hot dice
            num_dice = 6  # reset to six

        print(f"You have {unbanked_points} unbanked points and {num_dice} dice remaining")

        print("(r)oll again, (b)ank your points or (q)uit:")

        roll_bank_or_quit = input("> ")

        if roll_bank_or_quit == "q":
            return -1
        elif roll_bank_or_quit == "b":
            return unbanked_points


def zilch():
    """
    Display zilch message
    Returns:
        None
    """
    print("****************************************")
    print("**        Zilch!!! Round over         **")
    print("****************************************")


def confirm_keepers(roll):
    """

    Return values that user would like to keep after being validated

    Loops until user quits or follows the rules (aka keeps values that are valid)

    Args:
        roll: tuple of integers

    Returns:
        tuple of values to keep aka "keepers"
        empty tuple signals a "quit"
    """
    while True:
        print("Enter dice to keep, or (q)uit:")
        keep_or_quit = input("> ")

        if keep_or_quit == "q":
            return tuple()  # empty tuple means quit

        keepers = convert_keepers(keep_or_quit)

        if GameLogic.validate_keepers(roll, keepers):
            return keepers
        else:
            print("Cheater!!! Or possibly made a typo...")
            formatted_roll = format_roll(roll)
            print(formatted_roll)


def convert_keepers(keeper_string):
    """
    converts a given string of dice values to keep into a tuple of integers
    Args:
        keeper_string:

    Returns:
        tuple of integers

    """
    values = [int(value) for value in keeper_string if value.isdigit()]
    return tuple(values)


def do_roll(num_dice):
    """
    Display to user a new roll of given number of dice in formatted form
    Args:
        num_dice:

    Returns:
        return the roll (tuple of integers

    """
    print(f"Rolling {num_dice} dice...")

    roll = dice_roller(num_dice)

    formatted_roll = format_roll(roll)

    print(formatted_roll)

    return roll


def format_roll(roll):
    """
    converts given roll into display friendly string

    Args:
        roll: e.g. (5, 1, 1, 4, 5, 5)

    Returns:
        string: e.g. *** 5 1 1 4 5 5 ***
    """
    values_as_strings = [str(value) for value in roll]

    formatted_roll = " ".join(values_as_strings)

    return f"*** {formatted_roll} ***"


def decline_game():
    """
    Displays message to decling player
    Returns:
        None
    """
    print("OK. Maybe another time")


if __name__ == '__main__':
    play()
