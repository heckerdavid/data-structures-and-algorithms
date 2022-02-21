from stack_and_queue.stack import Stack

def remove_repeat_vals(input_stack):
    '''Removes repeated values from a stack. Returns a new stack'''
    hold_stack = Stack()
    seen = {}
    return_stack = Stack()

    while not input_stack.is_empty():
        current = input_stack.pop()
        if not seen.get(current):
            seen[current] = True
            hold_stack.push(current)

    while not hold_stack.is_empty():
        return_stack.push(hold_stack.pop())

    return return_stack


