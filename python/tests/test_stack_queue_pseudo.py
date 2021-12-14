from stack_and_queue.underflow import UnderFlowError
from stack_queue_pseudo.stack_queue_pseudo import PseudoQueue
import pytest

def test_import():
    assert PseudoQueue()


def test_single_enqueue():
    psqueue = PseudoQueue()

    psqueue.enqueue(9)

    actual = psqueue.dequeue()
    expected = 9
    assert actual == expected

def test_multiple_enqueue():
    psqueue = PseudoQueue()

    psqueue.enqueue(9)
    psqueue.enqueue(8)
    psqueue.enqueue(7)
    psqueue.enqueue(6)
    psqueue.enqueue(5)
    psqueue.enqueue(4)

    actual = psqueue.dequeue()
    expected = 9
    assert actual == expected

def test_multiple_dequeue():
    psqueue = PseudoQueue()

    psqueue.enqueue(9)
    psqueue.enqueue(8)
    psqueue.enqueue(7)
    psqueue.enqueue(6)
    psqueue.enqueue(5)
    psqueue.enqueue(4)

    psqueue.dequeue()
    psqueue.dequeue()
    psqueue.dequeue()
    psqueue.dequeue()

    actual = psqueue.dequeue()
    expected = 5
    assert actual == expected

def test_dequeue_from_empty():
    psqueue = PseudoQueue()

    with pytest.raises(UnderFlowError):
        psqueue.dequeue()

def test_dequeue_until_past_empty():
    psqueue = PseudoQueue()
    psqueue.enqueue(5)
    psqueue.enqueue(4)
    psqueue.dequeue()
    psqueue.dequeue()


    with pytest.raises(UnderFlowError):
        psqueue.dequeue()

def test_is_empty():
    psqueue = PseudoQueue()

    actual = psqueue.is_empty()
    expected = True
    assert actual == expected
