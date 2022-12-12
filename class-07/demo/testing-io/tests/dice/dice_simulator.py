import builtins
import difflib
import sys


def diff(game_play_func, path="", sample=""):
    """runs a given game play function and compares output with contents of given simulation

    Args:
        game_play_func (function): function that plays game.
            MUST have key word argument 'roller'
        path (str, optional): File path to a simulation text tile. Defaults to "".
        sample (str, optional): Simulation text to use if no path provided.
            Defaults to "".

    Returns:
        list: Reports for any lines that differ
    """

    text = ""

    expected_lines = _parse_expected_lines(path, sample)

    responses = _extract_responses(expected_lines)

    rolls = _extract_rolls(expected_lines)

    # inner function to mock print functionality
    def mock_print(*args):

        nonlocal text

        text += "".join(args) + "\n"

    # inner function to mock input functionality
    def mock_input(*args):

        nonlocal text

        response = responses.pop(0)

        text += "".join(args) + response + "\n"

        return response

    # inner function to mock rolling of dice
    def mock_roller():
        if not rolls:
            sys.exit(1)

        return rolls.pop(0)

    # store the "real" print & input so we can restore them later
    real_print = builtins.print
    real_input = builtins.input

    # mock the built in print & input
    builtins.print = mock_print
    builtins.input = mock_input

    try:
        game_play_func(roller=mock_roller)
    except SystemExit:
        real_print("No problem. System exits are allowed in this app.")

    # restore the "real" print and output functions
    builtins.print = real_print
    builtins.input = real_input

    return _find_differences(text, expected_lines)


# functions "private" to the module use leading underscore convention
# WARNING: they are not TRULY private, which is truly pythonic
def _parse_expected_lines(path, sample):
    if path:
        with open(path) as f:
            expected_lines = f.read().splitlines()
    else:
        expected_lines = sample.splitlines()

    return expected_lines


def _extract_responses(lines):
    responses = []
    for line in lines:
        if line.startswith(">"):
            response = line.replace("> ", "").strip()
            responses.append(response)

    return responses


def _extract_rolls(lines):
    rolls = []
    for line in lines:
        # WARNING: dice rolls MUST start with expected characters
        if line.startswith("*** "):
            roll = [int(char) for char in line if char.isdigit()]
            rolls.append(roll)

    return rolls


def _find_differences(text, expected_lines):

    actual_lines = text.splitlines()

    diffed = difflib.unified_diff(actual_lines, expected_lines, lineterm="")

    return "\n".join(diffed)
