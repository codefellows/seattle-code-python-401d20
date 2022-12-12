import pytest
from ten_thousand.game_logic import GameLogic

pytestmark = [pytest.mark.version_3]


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (tuple(), tuple()),
        ((1,), (1,)),
        ((1, 2), (1,)),
        ((1, 2, 3), (1,)),
        ((1, 2, 3, 5), (1, 5)),
        ((5, 1, 2, 3), (1, 5)),
        ((2, 3, 4), tuple()),
    ],
)
def test_get_scorers(test_input, expected):
    actual = GameLogic.get_scorers(test_input)
    assert sorted(actual) == sorted(expected)
