from leet_code.symmetric_binary_tree import symmetric_tree
from binary_tree.binary_tree import BinaryTree
from binary_tree.node import Node

def test_import():
    assert symmetric_tree

def test_small_tree():
    tree = BinaryTree()
    tree.root = Node(4)
    tree.root.left = Node(5)
    tree.root.right = Node(5)

    actual = symmetric_tree(tree.root)
    expected = True
    assert actual == expected


def test_non_symmetrical():
    tree = BinaryTree()
    tree.root = Node(4)
    tree.root.left = Node(5)
    tree.root.right = Node(5)
    tree.root.left.left = Node(5)

    actual = symmetric_tree(tree.root)
    expected = False
    assert actual == expected
