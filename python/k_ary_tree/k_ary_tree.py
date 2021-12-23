from k_ary_tree.node import Node
from stack_and_queue.queue import Queue

class KaryTree:

    def __init__(self) -> None:
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.children.append(Node(value))
