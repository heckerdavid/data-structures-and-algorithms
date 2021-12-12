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
