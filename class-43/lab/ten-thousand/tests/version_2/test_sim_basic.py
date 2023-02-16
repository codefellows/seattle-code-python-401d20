import pytest
from tests.flo import diff
from ten_thousand.game import play

pytestmark = [pytest.mark.version_2]


def test_quitter():
    diffs = diff(play, path="tests/version_2/quitter.sim.txt")
    assert not diffs, diffs


def test_one_and_done():
    diffs = diff(play, path="tests/version_2/one_and_done.sim.txt")
    assert not diffs, diffs


def test_single_bank():
    diffs = diff(
        play, path="tests/version_2/bank_one_roll_then_quit.sim.txt"
    )
    assert not diffs, diffs


def test_bank_first_for_two_rounds():
    diffs = diff(
        play, path="tests/version_2/bank_first_for_two_rounds.sim.txt"
    )
    assert not diffs, diffs
