from stack_and_queue.stack import Stack
from stack_and_queue.underflow import UnderFlowError

def valid_parens(string):
    stack = Stack()

    pairs = {')':'(', ']':'[', '}':'{',}

    for letter in string:
        if letter in pairs.values():
            stack.push(letter)

        elif letter in pairs.keys():
            try:
                last_opener = stack.pop()
            except UnderFlowError:
                return False
            if pairs[letter] != last_opener:
                return False

    return stack.is_empty()
