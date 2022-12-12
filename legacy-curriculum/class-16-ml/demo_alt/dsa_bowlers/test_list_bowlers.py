from bowler import Bowler
from list_bowlers import find_worst_average_bowler


def test_list_bowlers():
    annie = Bowler("Annie", 190, 210)
    benny = Bowler("Benny", 190, 195)
    chance = Bowler("Chance", 185, 225)
    delia = Bowler("Delia", 165, 170)

    bowlers = [annie, benny, chance, delia]

    actual = find_worst_average_bowler(bowlers)

    expected = delia

    assert actual == expected
