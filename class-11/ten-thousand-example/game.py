from ten_thousand.game_logic import GameLogic


def play(roller=GameLogic.roll_dice, num_rounds=20):
    """
    Play Ten Thousand game

    Args:
        roller: dice rolling function
        num_rounds: number of rounds to play

    Returns:

    """
    accepted = invite_to_play()
    if accepted:
        start_game(num_rounds, roller)
    else:
        decline_game()


def invite_to_play():
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    choice = input("> ")
    return choice == "y"


def decline_game():
    print("OK. Maybe another time")


def start_game(number_of_rounds, roll_dice):
    """
    Start the game

    Returns:
    """
    total_score = 0
    for round_num in range(1, number_of_rounds + 1):
        round_score = do_round(round_num, roll_dice)

        if round_score == -1:
            break

        total_score += round_score

        complete_round(round_num, total_score, round_score)

    end_game(total_score)


def do_round(round_num, roll_dice):
    """

    Args:
        round_num: int
        roll_dice: function

    Returns: number of points score in round or -1 if user quit

    """
    print(f"Starting round {round_num}")
    round_score = 0
    num_dice = 6

    while True:
        print(f"Rolling {num_dice} dice...")
        roll = roll_dice(num_dice)
        display_formatted_roll(roll)
        if GameLogic.calculate_score(roll) == 0:
            zilch()
            return 0
        else:
            keepers = validate_keepers(roll)
            if not keepers:
                return -1  # user quit

            roll_score = GameLogic.calculate_score(keepers)
            round_score += roll_score
            num_dice -= len(keepers)
            if num_dice == 0:
                num_dice = 6

            r_b_q = roll_bank_or_quit(round_score, num_dice)

            if r_b_q == "q":
                return -1
            elif r_b_q == "b":
                return round_score

            # if no return presume user wants to roll again


def display_formatted_roll(roll):
    """
    Display roll with formatting
    Args:
        roll:

    Returns:

    """
    roll_string = " ".join([str(value) for value in roll])
    print("*** " + roll_string + " ***")


def zilch():
    """
    Display to user that Zilch has occurred
    Returns:

    """
    print("****************************************")
    print("**        Zilch!!! Round over         **")
    print("****************************************")


def validate_keepers(roll):
    """
    Collect and validate user's selected dice
    Args:
        roll:

    Returns:
        validated tuple of "keepers" aka user selected dice
        None if user quits

    """
    while True:
        print("Enter dice to keep, or (q)uit:")
        keepers_string = input("> ")
        converted_keepers = convert_keepers(keepers_string)
        valid = GameLogic.validate_keepers(roll, converted_keepers)
        if not valid:
            print("Cheater!!! Or possibly made a typo...")
            display_formatted_roll(roll)
        else:
            return converted_keepers


def convert_keepers(keepers_string):
    """
    Converts string of dice values into tuple
    Args:
        keepers_string:

    Returns:

    """
    keepers = [int(char) for char in keepers_string if char.isdigit()]
    return keepers


def roll_bank_or_quit(unbanked_points, num_dice):
    print(f"You have {unbanked_points} unbanked points and {num_dice} dice remaining")
    print("(r)oll again, (b)ank your points or (q)uit:")
    choice = input("> ")
    # TODO: Ask client if they want to constrain to just r,b or q
    return choice


def end_game(score):
    print(f"Thanks for playing. You earned {score} points")


def complete_round(round_num, total_score, round_score):
    """

    Args:
        round_num:
        total_score:
        round_score:

    Returns:

    """
    print(f"You banked {round_score} points in round {round_num}")
    print(f"Total score is {total_score} points")


if __name__ == '__main__':
    play()
