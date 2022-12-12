"""Place in root of Project,
at same level as pyproject.toml
"""

from abc import ABC, abstractmethod
import builtins
import re
from ten_thousand.game import play
from ten_thousand.game_logic import GameLogic


class BaseBot(ABC):
    """Base class for Game bots"""

    def __init__(self, print_all=False):
        self.last_print = ""
        self.last_roll = []
        self.print_all = print_all
        self.dice_remaining = 0
        self.unbanked_points = 0

        self.real_print = print
        self.real_input = input
        builtins.print = self._mock_print
        builtins.input = self._mock_input
        self.total_score = 0

    def reset(self):
        """restores the real print and input builtin functions"""

        builtins.print = self.real_print
        builtins.input = self.real_input

    def report(self, text):
        """Prints out final score, and all other lines optionally"""

        if self.print_all:
            self.real_print(text)
        elif text.startswith("Thanks for playing."):
            score = re.sub("\D", "", text)
            self.total_score += int(score)

    def _mock_print(self, *args, **kwargs):
        """steps in front of the real builtin print function"""

        line = " ".join(args)

        if "unbanked points" in line:

            # parse the proper string
            # E.g. "You have 700 unbanked points and 2 dice remaining"
            unbanked_points_part, dice_remaining_part = line.split("unbanked points")

            # Hold on to unbanked points and dice remaining for determining rolling vs. banking
            self.unbanked_points = int(re.sub("\D", "", unbanked_points_part))

            self.dice_remaining = int(re.sub("\D", "", dice_remaining_part))

        elif line.startswith("*** "):

            self.last_roll = [int(ch) for ch in line if ch.isdigit()]

        else:
            self.last_print = line

        self.report(*args, **kwargs)

    def _mock_input(self, *args, **kwargs):
        """steps in front of the real builtin print function"""

        if self.last_print == "(y)es to play or (n)o to decline":

            return "y"

        elif self.last_print == "Enter dice to keep, or (q)uit:":

            return self._enter_dice()

        elif self.last_print == "(r)oll again, (b)ank your points or (q)uit:":

            return self._roll_bank_or_quit()

        raise ValueError(f"Unrecognized last print {self.last_print}")

    def _enter_dice(self):
        """simulate user entering which dice to keep.
        Defaults to all scoring dice"""

        roll = GameLogic.get_scorers(self.last_roll)

        roll_string = ""

        for value in roll:
            roll_string += str(value)

        self.report("> " + roll_string)

        return roll_string

    @abstractmethod
    def _roll_bank_or_quit(self):
        """decide whether to roll the dice, bank the points, or quit"""

        # subclass MUST implement this method
        pass

    @classmethod
    def play(cls, num_games=1):
        """Tell Bot play game a given number of times.
        Will report average score"""

        mega_total = 0

        for _ in range(num_games):
            player = cls()

            try:
                play()
            except SystemExit:
                # in game system exit is fine
                # because that's how they quit.
                pass

            mega_total += player.total_score
            player.reset()

        print(
            f"{cls.__name__}: {num_games} games played with average score of {mega_total // num_games}"
        )


class NervousNellie(BaseBot):
    """NervousNellie banks the first roll always"""

    def _roll_bank_or_quit(self):
        return "b"


class MiddlingMargaret(BaseBot):
    """MiddlingMargaret has a moderate playing style"""

    def _roll_bank_or_quit(self):

        if self.unbanked_points >= 500 or self.dice_remaining < 3:
            return "b"

        return "r"


class DaringDarla(BaseBot):
    """DaringDarla rolls whenever more than 1 dice remaining """

    def _roll_bank_or_quit(self):
        if self.dice_remaining == 1:
            return "b"

        return "r"


class YourBot(BaseBot):
    def _roll_bank_or_quit(self):
        """your logic here"""
        return "b"

    def _enter_dice(self):
        """simulate user entering which dice to keep.
        Defaults to all scoring dice"""

        return super()._enter_dice()


class MarkBot(BaseBot):
    """
    self.dice_remaining
    self.unbanked_points
    self.total_score
    """

    def __init__(self):
        from collections import Counter

        self.Counter = Counter
        super().__init__()
        self.rounds_remaining = None

    # this is a pretty close approximation of chance to fail, could be improved
    @staticmethod
    def chance_to_fail(num_of_dice):
        return {
            1: 2 / 3,
            2: 4 / 9,
            3: 8 / 27 - 1 / 36,
            4: 16 / 81 - 1 / 36,
            5: 32 / 243 - 1 / 36,
            6: 64 / 729 - 1 / 36 - 1 / 6 ** 6,
        }[num_of_dice]

    def _roll_bank_or_quit(self):
        # always roll when you have 6 dice to roll
        if not self.dice_remaining or self.dice_remaining == 6:
            return "r"
        # bank if we think we have a high chance of failure
        if MarkBot.chance_to_fail(self.dice_remaining) > 95 / (
            self.unbanked_points + 1
        ):
            return "b"
        return "r"

    def _enter_dice(self):
        """simulate user entering which dice to keep.
        Defaults to all scoring dice"""
        roll = GameLogic.get_scorers(self.last_roll)
        roll_string = ""
        # if we all dice score, please keep them all
        # if we are intending on banking, lets keep all scoring dice
        if len(roll) == len(self.last_roll) or self._roll_bank_or_quit() == "b":
            # self.real_print("\nINTENDING TO BANK:",self.dice_remaining)
            for value in roll:
                roll_string += str(value)
            self.report("> " + roll_string)
            return roll_string
        # lets go for highest average of points per die
        highest_score_per_die = 0
        highest_scoring_dice = 0
        highest_scoring_len = 0
        # check each combination of dice, to determine the 'best' value per die, and keep that set
        roll = list(roll)
        roll.sort()
        for i in range(len(roll)):
            for j in range(len(roll)):
                if len(roll[i : j + 1]):
                    test_dice = roll[i : j + 1]
                    test_score = GameLogic.calculate_score(roll[i : j + 1]) / len(
                        test_dice
                    )
                    if test_score > highest_score_per_die:
                        highest_score_per_die = test_score
                        highest_scoring_dice = test_dice
                        highest_scoring_len = len(test_dice)
                    elif test_score == highest_score_per_die:
                        if highest_score_per_die >= 175:
                            if len(test_dice) > highest_scoring_len:
                                highest_score_per_die = test_score
                                highest_scoring_dice = test_dice
                                highest_scoring_len = len(test_dice)
        for value in highest_scoring_dice:
            roll_string += str(value)
        self.report("> " + roll_string)
        return roll_string


class YoniBot(BaseBot):
    def _roll_bank_or_quit(self):
        if self.unbanked_points >= 550 or self.dice_remaining < 2:
            return "b"
        if self.unbanked_points >= 450 and self.dice_remaining <= 3:
            return "b"
        elif self.unbanked_points >= 350 and self.dice_remaining == 2:
            return "b"
        if self.unbanked_points + self.total_score >= 10000:
            return "b"
        return "r"


class EvilBrendan(BaseBot):
    """VERY aggressive playstyle : all or nothing baby"""

    def _roll_bank_or_quit(self):
        if self.dice_remaining >= 3:
            return "r"
        if self.unbanked_points >= 800 or self.dice_remaining < 3:
            return "b"
        if self.unbanked_points > 350:
            if self.dice_remaining >= 3:
                return "r"
            else:
                return "b"
        if self.unbanked_points <= 400:
            return "r"


class EvilIncarnateBot(BaseBot):
    def _zilch_chance(self):
        return {1: 2 / 3, 2: 4 / 9, 3: 5 / 18, 4: 17 / 108, 5: 25 / 324, 6: 5 / 216,}[
            self.dice_remaining
        ]

    def _roll_bank_or_quit(self):
        # if self.unbanked_points >= 500 or self.dice_remaining < 3:
        if not self.dice_remaining:
            return "r"
        if self._zilch_chance() > (95 / (self.unbanked_points)):
            return "b"
        return "r"

    def _enter_dice(self):
        """simulate user entering which dice to keep.
        Defaults to all scoring dice"""
        roll = GameLogic.get_scorers(self.last_roll)
        roll_string = ""
        for value in roll:
            roll_string += str(value)
        if GameLogic.calculate_score(roll) < 200:
            self.report("> " + roll_string[0])
            return roll_string[0]
        five_count = 0
        two_count = 0
        three_count = 0
        for value in roll_string:
            if value == "5":
                five_count += 1
            elif value == "2":
                two_count += 1
            elif value == "3":
                three_count += 1
        if two_count <= 4 and two_count != len(roll):
            roll_string.replace("2", "", two_count)
        if three_count <= 3 and three_count != len(roll):
            roll_string.replace("3", "", three_count)
        if five_count <= 2:
            if five_count == len(roll_string):
                roll_string.replace("5", "", 1)
            else:
                roll_string.replace("5", "", five_count)
        if roll_string == "":
            roll_string += str(roll[0])
        self.report("> " + roll_string)
        return roll_string


if __name__ == "__main__":
    num_games = 100
    NervousNellie.play(num_games)
    # MiddlingMargaret.play(num_games)
    # DaringDarla.play(num_games)
    # YourBot.play(num_games)
    # MarkBot.play(num_games)
