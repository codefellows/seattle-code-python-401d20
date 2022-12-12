from codefellows.dsa.binary_tree import BinaryTree
from bowler import Bowler
from tree_bowlers import find_worst_average_bowler


def test_tree_bowlers():
    annie = Bowler("Annie", 190, 210)
    benny = Bowler("Benny", 190, 195)
    chance = Bowler("Chance", 185, 225)
    delia = Bowler("Delia", 165, 170)

    tree = BinaryTree(values=[annie, benny, chance, delia])

    actual = find_worst_average_bowler(tree.root)

    expected = delia

    assert actual is expected
