from binary_tree.node import Node

class BinaryTree:
    def __init__(self, root=None) -> None:
        self.root = Node(root)


    def add(self, value) -> None:
        if self.root.left is None:
            self.root.left = Node(value)
            return
        elif self.root.right is None:
            self.root.right = Node(value)

    def find_max_value(self):

        if not self.root.value:
            return None

        current_max = 0

        def walk(root):
            nonlocal current_max
            if root is None:
                return
            if root.value > current_max:
                current_max = root.value

            walk(root.left)
            walk(root.right)

        walk(self.root)
        return current_max

    def pre_order(self) -> list:
        output = []

        def walk(root=self.root):
            if root is None:
                return
            output.append(root.value)
            walk(root.left)
            walk(root.right)
            return

        walk()

        return output

    def in_order(self) -> list:
        output = []

        def walk(root=self.root):
            if root is None:
                return
            walk(root.left)
            output.append(root.value)
            walk(root.right)
            return

        walk()

        return output

    def post_order(self) -> list:
        output = []

        def walk(root=self.root):
            if root is None:
                return
            walk(root.left)
            walk(root.right)
            output.append(root.value)
            return

        walk()

        return output
