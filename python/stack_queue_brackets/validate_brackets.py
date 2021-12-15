from stack_and_queue.stack import Stack

def validate_brackets(string):
    left = Stack()
    right = Stack()
    acceptable_values = {
        '[':']',
        '{':'}',
        '(':')',
    }

    for char in string:
        if char in acceptable_values.keys():
            left.push(char)
        elif char in acceptable_values.values():
            right.push(char)

    while not left.is_empty() and not right.is_empty():
        if acceptable_values[left.pop()] != right.pop():
            return False

    if left.is_empty() != right.is_empty():
        return False

    return True
