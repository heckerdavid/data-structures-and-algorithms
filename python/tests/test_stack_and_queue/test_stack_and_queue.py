'''Can successfully push onto a stack
Can successfully push multiple values onto a stack
Can successfully pop off the stack
Can successfully empty a stack after multiple pops
Can successfully peek the next item on the stack
Can successfully instantiate an empty stack
Calling pop or peek on empty stack raises exception
Can successfully enqueue into a queue
Can successfully enqueue multiple values into a queue
Can successfully dequeue out of a queue the expected value
Can successfully peek into a queue, seeing the expected value
Can successfully empty a queue after multiple dequeues
Can successfully instantiate an empty queue
Calling dequeue or peek on empty queue raises exception'''

from attr import s
from stack_and_queue.queue import Queue
from stack_and_queue.stack import Stack
from stack_and_queue.underflow import UnderFlowError
import pytest

def test_import():
    assert Stack()
    assert Queue()


def test_make_empty_stack_and_peek():
    stack = Stack()

    with pytest.raises(UnderFlowError):
        stack.peek()

def test_push_to_empty_stack():
    stack = Stack()
    stack.push(9)

    actual = stack.peek()
    expected = 9
    assert actual == expected

def test_pop_from_stack():
    stack = Stack()
    stack.push(9)
    stack.push(8)

    actual = stack.pop()
    expected = 8
    assert actual == expected

def test_pop_from_empty_stack():
    stack = Stack()

    with pytest.raises(UnderFlowError):
        stack.pop()

def test_multiple_pops_from_stack():
    stack = Stack()
    stack.push(9)
    stack.push(8)
    stack.push(7)
    stack.push(6)

    stack.pop()
    stack.pop()
    actual = stack.pop()
    expected = 8
    assert actual == expected


def test_multiple_pops_from_stack_until_empty():
    stack = Stack()
    stack.push(9)
    stack.push(8)
    stack.push(7)

    stack.pop()
    stack.pop()
    stack.pop()
    with pytest.raises(UnderFlowError):
        stack.peek()

def test_exception_on_empty_stack():
    stack = Stack()
    with pytest.raises(UnderFlowError):
        stack.peek()



# Queue tests
def test_make_empty_queue_and_peek():
    queue = Queue()

    with pytest.raises(UnderFlowError):
        queue.peek()

def test_push_to_empty_queue():
    queue = Queue()
    queue.push(9)

    actual = queue.peek()
    expected = 9
    assert actual == expected

def test_push_multiple_pushes_to_queue():
    queue = Queue()
    queue.push(9)
    queue.push(8)
    queue.push(7)
    queue.push(6)
    queue.pop()

    actual = queue.peek()
    expected = 8
    assert actual == expected

def test_pop_from_queue():
    queue = Queue()
    queue.push(9)

    actual = queue.pop()
    expected = 9
    assert actual == expected

def test_pop_from_empty_queue():
    queue = Queue()
    with pytest.raises(UnderFlowError):
        queue.pop()

def test_multiple_pops_from_queue():
    queue = Queue()
    queue.push(9)
    queue.push(8)
    queue.push(7)

    queue.pop()
    queue.pop()
    actual = queue.pop()
    expected = 7
    assert actual == expected
