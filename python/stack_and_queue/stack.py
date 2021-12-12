from stack_and_queue.node import Node
from stack_and_queue.underflow import UnderFlowError

class Stack:
    def __init__(self) -> None:
        self.top = None


    def peek(self) -> any:
        if not self.top:
            raise UnderFlowError
        return self.top.value


    def push(self, value) -> None:
        self.top = Node(value, self.top)


    def pop(self) -> any:
        if not self.top:
            raise UnderFlowError

        temporary_holder = self.top

        self.top = self.top.next

        return temporary_holder.value

    def is_empty(self):
        return not self.top
