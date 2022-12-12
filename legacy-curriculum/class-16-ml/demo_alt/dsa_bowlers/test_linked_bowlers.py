from linked_bowlers import find_worst_average_bowler
from bowler import Bowler
from codefellows.dsa.linked_list import LinkedList


def test_linked_bowlers():
    annie = Bowler("Annie", 190, 210)
    benny = Bowler("Benny", 190, 195)
    chance = Bowler("Chance", 185, 225)
    delia = Bowler("Delia", 165, 170)

    bowlers = LinkedList(values=[annie, benny, chance, delia])

    actual = find_worst_average_bowler(bowlers)
    expected = delia

    assert actual is expected
