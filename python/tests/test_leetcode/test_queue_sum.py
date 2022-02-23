from leet_code.queue_sum import queue_sum
from stack_and_queue.queue import Queue
def test_import():
    assert queue_sum

def test_small_queue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)

    actual = queue_sum(q)
    expected = 3
    assert actual == expected

def test_queue_sum():
    q = Queue()
    for i in range(5):
        q.enqueue(i)

    actual = queue_sum(q)
    expected = 10
    assert actual == expected


def test_negative_sum():
    q = Queue()
    for i in range(5):
        q.enqueue(-i)

    actual = queue_sum(q)
    expected = -10
    assert actual == expected

def test_negative_sum():
    q = Queue()
    for i in range(5):
        q.enqueue(-i)
    for i in range(5):
        q.enqueue(i)

    actual = queue_sum(q)
    expected = 0
    assert actual == expected
