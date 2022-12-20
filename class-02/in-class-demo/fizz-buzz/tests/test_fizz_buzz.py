import pytest
# from package_name.module_name import function_name
from fizz_buzz.fizz_buzz import fizz_buzz


# pytest tests must start with "test_"
def test_fizz_buzz_exists():
    assert fizz_buzz


# @pytest.mark.skip()
def test_fizz_buzz_3():
    actual = fizz_buzz(3)
    expected = "Fizz"
    assert actual == expected


def test_fizz_buzz_6():
    actual = fizz_buzz(6)
    expected = "Fizz"
    assert actual == expected


def test_fizz_buzz_5():
    actual = fizz_buzz(5)
    expected = "Buzz"
    assert actual == expected


def test_fizz_buzz_10():
    actual = fizz_buzz(10)
    expected = "Buzz"
    assert actual == expected


def test_fizz_buzz_15():
    actual = fizz_buzz(15)
    expected = "FizzBuzz"
    assert actual == expected


def test_fizz_buzz_30():
    actual = fizz_buzz(30)
    expected = "FizzBuzz"
    assert actual == expected


def test_fizz_buzz_7():
    actual = fizz_buzz(7)
    expected = "7"
    assert actual == expected


def test_fizz_buzz_11():
    actual = fizz_buzz(11)
    expected = "11"
    assert actual == expected


