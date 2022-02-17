from decimal import Underflow
import pytest
from leet_code.remove_dup_from_q import remove_duplicates
from stack_and_queue.queue import Queue
from stack_and_queue.underflow import UnderFlowError

def test_import():
    assert remove_duplicates


def test_short():
    q = Queue()
    q.enqueue(1)
    for i in range(5):
        q.enqueue(i)

    remove_duplicates(q)
    assert q.dequeue() == 1
    assert q.dequeue() == 0
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() == 4

def test_multi_repeated():
    q = Queue()
    q.enqueue(1)
    for i in range(5):
        q.enqueue(i)
    q.enqueue(4)
    q.enqueue(2)
    q.enqueue(3)

    remove_duplicates(q)

    assert q.dequeue() == 1
    assert q.dequeue() == 0
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() == 4
    with pytest.raises(UnderFlowError):
        q.dequeue()


def test_no_repeated():
    q = Queue()

    for i in range(5):
        q.enqueue(i)

    remove_duplicates(q)

    assert q.dequeue() == 0
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() == 4
    with pytest.raises(UnderFlowError):
        q.dequeue()


def test_no_repeated_strings():
    q = Queue()


    q.enqueue('hello')
    q.enqueue('world')

    remove_duplicates(q)

    assert q.dequeue() == 'hello'
    assert q.dequeue() == 'world'
    with pytest.raises(UnderFlowError):
        q.dequeue()


def test_repeated_strings():
    q = Queue()


    q.enqueue('hello')
    q.enqueue('world')
    q.enqueue('hello')

    remove_duplicates(q)

    assert q.dequeue() == 'hello'
    assert q.dequeue() == 'world'
    with pytest.raises(UnderFlowError):
        q.dequeue()
