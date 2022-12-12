import pytest

from codefellows.dsa.binary_tree import BinaryTree


def test_instantiate_empty():
    tree = BinaryTree()
    actual = tree.root
    expected = None
    assert actual == expected


def test_add_to_empty():
    tree = BinaryTree()
    tree.add("apples")
    actual = tree.root.value
    expected = "apples"
    assert actual == expected


def test_add_some():
    tree = BinaryTree()
    tree.add("apples")
    tree.add("bananas")
    actual = tree.root.left.value
    expected = "bananas"
    assert actual == expected


def test_add_more():
    tree = BinaryTree()
    tree.add("a")
    tree.add("b")
    tree.add("c")
    actual = tree.root.left.value
    expected = "b"
    assert actual == expected


def test_pre_order(tiny):
    actual = []
    tiny.pre_order(actual.append)
    expected = ["root", "left", "right"]
    assert actual == expected


def test_in_order(tiny):
    actual = []
    tiny.in_order(actual.append)
    expected = ["left", "root", "right"]
    assert actual == expected


def test_post_order(tiny):
    actual = []
    tiny.post_order(actual.append)
    expected = ["left", "right", "root"]
    assert actual == expected


def test_breadth_first(tree):
    actual = []
    tree.breadth_first(actual.append)
    expected = ["a", "b", "c", "d", "e", "f", "g", "h"]
    assert actual == expected


def test_binary_add():
    tree = BinaryTree()
    tree.add("apples")
    tree.add("bananas")
    tree.add("cucumbers")

    actual = []
    tree.breadth_first(actual.append)
    expected = ["apples", "bananas", "cucumbers"]

    assert actual == expected


def test_find_maximum_value():
    tree = BinaryTree(values=[1, 5, 3, 6, 5, 2, -7, 6])
    actual = tree.find_maximum_value()
    expected = 6
    assert actual == expected


@pytest.fixture
def tiny():
    tree = BinaryTree()
    tree.add("root")
    tree.add("left")
    tree.add("right")
    return tree


@pytest.fixture
def tree():
    tree = BinaryTree()
    tree.add("a")
    tree.add("b")
    tree.add("c")
    tree.add("d")
    tree.add("e")
    tree.add("f")
    tree.add("g")
    tree.add("h")
    return tree
