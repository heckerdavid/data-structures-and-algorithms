from stack_and_queue.node import Node

class Stack:
    def __init__(self) -> None:
        self.top = None


    def peek(self) -> any:
        if not self.top:
            return None #TODO raise exception
        return self.top.value


    def push(self, value) -> None:
        self.top = Node(value, self.top)

    def pop(self):
        temporary_holder = self.top

        self.top = self.top.next

        return temporary_holder.value
