# Given a Stack, Find the sum of all elements ... Iteratively.

def find_stack_sum(stack):
    total = 0

    while not stack.is_empty():
        total += stack.pop()

    return total

