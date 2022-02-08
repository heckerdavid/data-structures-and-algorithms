from stack_and_queue.stack import Stack

def validate_brackets(string):
    stack = Stack()

    acceptable_values = {
        '[':']',
        '{':'}',
        '(':')',
    }

    for char in string:
        if char in acceptable_values.keys():
            stack.push(char)
        elif char in acceptable_values.values():
            if stack.is_empty():
                return False
            elif char == acceptable_values[stack.pop()]:
                continue


    return stack.is_empty()
