from leet_code.stack_sum import find_stack_sum
from stack_and_queue.stack import Stack

def test_import():
    assert find_stack_sum

def test_sum():
    stack = Stack()
    for i in range(5):
        stack.push(i)

    actual = find_stack_sum(stack)
    expected = 10
    assert actual == expected

def test_negatives():
    stack = Stack()
    for i in range(5):
        stack.push(-i)

    actual = find_stack_sum(stack)
    expected = -10
    assert actual == expected

def test_repeat_vals():
    stack = Stack()
    for i in range(5):
        stack.push(-i)
    for i in range(5):
        stack.push(-i)


    actual = find_stack_sum(stack)
    expected = -20
    assert actual == expected

def test_mix_vals():
    stack = Stack()
    for i in range(5):
        stack.push(-i)

    for i in range(5):
        stack.push(i)


    actual = find_stack_sum(stack)
    expected = 0
    assert actual == expected
