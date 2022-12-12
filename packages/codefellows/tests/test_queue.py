import pytest
from codefellows.dsa.queue import Queue

def test_is_empty():
    q = Queue()
    assert q.is_empty()

def test_is_not_empty():
    q = Queue()
    q.enqueue("apple")
    assert not q.is_empty()

def test_becomes_empty():
    q = Queue()
    q.enqueue("apple")
    q.dequeue()
    assert q.is_empty()

def test_enqueue():
    q = Queue()
    q.enqueue("apple")
    assert q.peek() == "apple"
