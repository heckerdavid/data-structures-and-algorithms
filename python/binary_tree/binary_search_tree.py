from binary_tree.binary_tree import BinaryTree
from binary_tree.node import Node


class BinarySearchTree(BinaryTree):

    def add(self, value=None):
        if self.root.value is None:
            self.root = Node(value)

        def walk(root, value):

            if root.value > value:
                if root.left is None:
                    root.left = Node(value)
                else:
                    walk(root.left, value)

            elif root.value < value:
                if root.right is None:
                    root.right = Node(value)
                else:
                    walk(root.right, value)


        walk(self.root, value)

    def contains(self, value):

        if self.root is None:
            return False

        def walk(root, value):
            if root.value == value:
                return True
            elif value > root.value:
                if root.right:
                    return walk(root.right, value)
            elif value < root.value:
                if root.left:
                    return walk(root.left, value)
            return False

        return walk(self.root, value)
