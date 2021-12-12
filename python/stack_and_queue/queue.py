from _pytest.python_api import raises
from stack_and_queue.node import Node
from stack_and_queue.underflow import UnderFlowError

class Queue:
    def __init__(self) -> None:
        self.front = None
        self.back = None

    def peek(self):
        if not self.front:
            raise UnderFlowError

        return self.front.value

    def push(self, value):

        if not self.front:
            self.front = Node(value)
            self.back = self.front
            return

        self.back.next = Node(value)
        self.back = self.back.next

    def pop(self):
        if not self.front:
            raise UnderFlowError

        temp_value_holder = self.front.value
        if self.front.next:
            self.front = self.front.next
        else:
            self.front = None

        return temp_value_holder
