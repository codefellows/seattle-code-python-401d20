import pytest
from ten_thousand.game_logic import GameLogic

# Testing - Roll Dice
# When rolling 1 to 6 dice ensure...
# A sequence of correct length is returned
# Each item in sequence is an integer with value between 1 and 6


def test_roll_six():
    roll = GameLogic.roll_dice(6)
    assert len(roll) == 6
    for value in roll:
        assert 1 <= value <= 6


def test_roll_five():
    roll = GameLogic.roll_dice(5)
    assert len(roll) == 5
    for value in roll:
        assert 1 <= value <= 6


# Hey! test_roll_six and test_roll_five are REALLY similar
# There's got to be a better way...


@pytest.mark.parametrize(
    "num_dice,expected_length",
    [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
    ],
)
def test_all_valid_dice_rolls(num_dice, expected_length):
    roll = GameLogic.roll_dice(num_dice)
    assert len(roll) == expected_length
    for value in roll:
        assert 1 <= value <= 6
