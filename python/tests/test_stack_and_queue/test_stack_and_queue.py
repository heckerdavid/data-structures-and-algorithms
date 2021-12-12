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

from stack_and_queue.queue import Queue
from stack_and_queue.stack import Stack

def test_import():
    assert Stack()
    assert Queue()


def test_make_empty_stack_and_peek():
    stack = Stack()

    actual = stack.peek()
    expected = None
    assert actual == expected

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


def test_exception_on_empty_stack():
    pass
