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

    def enqueue(self, value):

        if not self.front:
            self.front = Node(value)
            self.back = self.front
            return

        self.back.next = Node(value)
        self.back = self.back.next

    def dequeue(self):

        if not self.front:
            raise UnderFlowError

        temp_value_holder = self.front.value

        self.front = self.front.next

        return temp_value_holder

    def is_empty(self):
        return not self.front
