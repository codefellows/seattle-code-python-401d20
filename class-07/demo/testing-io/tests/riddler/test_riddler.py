from tests.riddler.riddler_simulator import diff
from testing_io.riddler import Riddler


def test_first_try():
    riddler = Riddler()
    diffs = diff(riddler.play, path="tests/riddler/first_try.sim.txt")
    assert not diffs, diffs


def test_one_and_done():
    riddler = Riddler()
    diffs = diff(riddler.play, path="tests/riddler/one_and_done.sim.txt")
    assert not diffs, diffs


def test_italiano():
    riddler = Riddler(riddle="my favorite coffee drink", answer="Italiano")
    diffs = diff(riddler.play, path="tests/riddler/italiano.sim.txt")
    assert not diffs, diffs


def test_red():
    riddler = Riddler(answer="red")
    diffs = diff(riddler.play, path="tests/riddler/red.sim.txt")
    assert not diffs, diffs

def test_two_for_you():
    riddler = Riddler()
    diffs = diff(riddler.play, path="tests/riddler/two_for_you.sim.txt")
    assert not diffs, diffs
