from binary_tree.node import Node

class BinaryTree:
    def __init__(self, root=None) -> None:
        self.root = Node(root)


    def add(self, value) -> None:
        if self.root.left is None:
            self.root.left = Node(value)
            return
        self.root.right = Node(value)
