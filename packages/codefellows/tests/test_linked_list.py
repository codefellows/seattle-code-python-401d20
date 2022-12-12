import pytest
from codefellows.dsa.linked_list import LinkedList, TargetError


def test_insert():
    linked_list = LinkedList()

    assert str(linked_list) == "NULL"

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> NULL"

    linked_list.insert("banana")

    assert str(linked_list) == "{ banana } -> { apple } -> NULL"


def test_includes():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert linked_list.includes("apple")

    assert not linked_list.includes("cucumber")


def test_append():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.append("cucumber")

    assert (
        str(linked_list) == "{ banana } -> { apple } -> { cucumber } -> NULL"
    )


def test_insert_before():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.insert_before("apple", "cucumber")

    assert (
        str(linked_list) == "{ banana } -> { cucumber } -> { apple } -> NULL"
    )


def test_insert_after():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.insert_after("banana", "cucumber")

    assert (
        str(linked_list) == "{ banana } -> { cucumber } -> { apple } -> NULL"
    )


def test_insert_before_empty():
    linked_list = LinkedList()

    with pytest.raises(TargetError):
        linked_list.insert_before("radish", "zucchinni")


def test_insert_before_missing():
    linked_list = LinkedList()

    linked_list.insert("banana")

    with pytest.raises(TargetError):
        linked_list.insert_before("radish", "zucchinni")


def test_insert_after_empty():
    linked_list = LinkedList()

    with pytest.raises(TargetError):
        linked_list.insert_after("radish", "zucchinni")


def test_insert_after_missing():
    linked_list = LinkedList()

    linked_list.insert("banana")

    with pytest.raises(TargetError):
        linked_list.insert_after("radish", "zucchinni")


# Where k is greater than the length of the linked list
# Where k and the length of the list are the same
# Where k is not a positive integer
# Where the linked list is of a size 1
# "Happy Path" where k is not at the end, but somewhere in the middle of the linked list


def test_kth_from_end_zero():
    linked_list = LinkedList(values=["apples", "bananas", "cucumbers"])
    actual = linked_list.kth_from_end(0)
    expected = "cucumbers"
    assert actual == expected


def test_kth_from_end_one():
    linked_list = LinkedList(values=["apples", "bananas", "cucumbers"])
    actual = linked_list.kth_from_end(1)
    expected = "bananas"
    assert actual == expected


def test_kth_from_end_two():
    linked_list = LinkedList(values=["apples", "bananas", "cucumbers"])
    actual = linked_list.kth_from_end(2)
    expected = "apples"
    assert actual == expected


def test_kth_from_end_out_of_range():
    linked_list = LinkedList(values=["apples", "bananas", "cucumbers"])

    with pytest.raises(TargetError):
        linked_list.kth_from_end(3)


def test_kth_from_end_under_range():
    linked_list = LinkedList(values=["apples", "bananas", "cucumbers"])

    with pytest.raises(TargetError):
        linked_list.kth_from_end(-1)


def test_kth_from_end_size_one():
    linked_list = LinkedList(values=["apples"])
    actual = linked_list.kth_from_end(0)
    expected = "apples"
    assert actual == expected


#############################
# reverse
#############################


def test_reverse_1234():
    linked_list = LinkedList(values=[1, 2, 3, 4])
    actual = str(linked_list.reverse())
    expected = "{ 4 } -> { 3 } -> { 2 } -> { 1 } -> NULL"
    assert actual == expected


#############################
# equals
#############################


def test_equals_empty():
    list_a = LinkedList()
    list_b = LinkedList()
    assert list_a == list_b


def test_equals_same_length():
    list_a = LinkedList(values="abc")
    list_b = LinkedList(values="abc")
    assert list_a == list_b


def test_not_equals__same_length():
    list_a = LinkedList(values="abc")
    list_b = LinkedList(values="def")
    assert list_a != list_b


def test_not_equals_first_longer():
    list_a = LinkedList(values="ab")
    list_b = LinkedList(values="a")
    assert list_a != list_b


def test_not_equals_second_longer():
    list_a = LinkedList(values="a")
    list_b = LinkedList(values="ab")
    assert list_a != list_b

#############################
# get item at index
#############################

def test_index_zero():
    letters = LinkedList(values="abcd")
    actual = letters[0]
    expected = "a"
    assert actual == expected

def test_index_one():
    letters = LinkedList(values="abcd")
    actual = letters[1]
    expected = "b"
    assert actual == expected

def test_index_too_large():
    letters = LinkedList(values="abcd")
    with pytest.raises(IndexError):
        letters[4]

def test_negative_index_one():
    letters = LinkedList(values="abcd")
    actual = letters[-1]
    expected = "d"
    assert actual == expected

#############################
# set item at index
#############################

def test_set_item_zero():
    letters = LinkedList(values="abc")
    letters[0] = "b"
    assert letters[0] == "b"

def test_set_item_one():
    letters = LinkedList(values="abc")
    letters[1] = "a"
    assert letters[1] == "a"

