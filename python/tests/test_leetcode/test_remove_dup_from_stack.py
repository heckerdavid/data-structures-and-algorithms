from leet_code.remove_dup_from_stack import remove_repeat_vals
from stack_and_queue.stack import Stack
import pytest

from stack_and_queue.underflow import UnderFlowError


def test_import():
    assert remove_repeat_vals

def test_short_repeat():
    stack = Stack()
    stack.push(1)
    stack.push(1)

    stack = remove_repeat_vals(stack)

    assert stack.pop() == 1
    with pytest.raises(UnderFlowError):
        stack.pop()


def test_zeros_repeat():
    stack = Stack()
    stack.push(0)
    stack.push(0)

    stack = remove_repeat_vals(stack)

    assert stack.pop() == 0
    with pytest.raises(UnderFlowError):
        stack.pop()


def test_multiple_repeat():
    stack = Stack()
    stack.push(0)
    stack.push(0)
    stack.push(10)
    stack.push(10)

    stack = remove_repeat_vals(stack)

    assert stack.pop() == 10
    assert stack.pop() == 0
    with pytest.raises(UnderFlowError):
        stack.pop()



def test_multi_repeat():
    stack = Stack()
    stack.push(0)
    stack.push(0)
    stack.push(10)
    stack.push(0)
    stack.push(10)
    stack.push(0)

    stack = remove_repeat_vals(stack)

    assert stack.pop() == 0
    assert stack.pop() == 10
    with pytest.raises(UnderFlowError):
        stack.pop()


def test_multi_data_types():
    stack = Stack()
    stack.push('hello')
    stack.push(0)
    stack.push(10)
    stack.push('hello')
    stack.push(10)
    stack.push(0)

    stack = remove_repeat_vals(stack)

    assert stack.pop() == 0
    assert stack.pop() == 10
    assert stack.pop() == 'hello'
    with pytest.raises(UnderFlowError):
        stack.pop()
