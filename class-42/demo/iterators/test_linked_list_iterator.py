import pytest

from linked_list_iterator import LinkedList

def test_for_in():

    foods = LinkedList(("apple","banana","cucumber"))

    foods_list = []

    for food in foods:
        foods_list.append(food)

    assert foods_list == ["apple","banana","cucumber"]


def test_list_comprehension():

    foods = LinkedList(("apple","banana","cucumber"))

    cap_foods = [food.upper() for food in foods]

    assert cap_foods == ["APPLE","BANANA","CUCUMBER"]

def test_list_cast():

    food_list = ["apple","banana","cucumber"]

    foods = LinkedList(food_list)

    assert list(foods) == food_list

def test_range():

    num_range = range(1,20+1)

    nums = LinkedList(num_range)

    assert len(nums) == 20


def test_filter():

    nums = LinkedList(range(1,21))

    odds = [num for num in nums if num % 2]

    assert odds == [1,3,5,7,9,11,13,15,17,19]

def test_next():

    foods = LinkedList(["apple","banana","cucumber"])

    iterator = iter(foods)

    assert next(iterator) == "apple"
    assert next(iterator) == "banana"
    assert next(iterator) == "cucumber"

def test_stop_iteration():

    foods = LinkedList(["apple","banana","cucumber"])

    iterator = iter(foods)

    with pytest.raises(StopIteration):
        while True:
            food = next(iterator)


def test_str():
    foods = LinkedList(["apple","banana","cucumber"])
    assert str(foods) == "[ apple ] -> [ banana ] -> [ cucumber ] -> None"

# dunder method tests

def test_equals():

    lla = LinkedList(["apple","banana","cucumber"])
    llb = LinkedList(["apple","banana","cucumber"])

    assert lla == llb

def test_get_item():

    foods = LinkedList(["apple","banana","cucumber"])

    assert foods[0] == "apple"

def test_get_item_out_of_range():

    foods = LinkedList(["apple","banana","cucumber"])

    with pytest.raises(IndexError):
        foods[100]
