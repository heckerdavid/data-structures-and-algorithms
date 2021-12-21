from binary_tree.breadth_first import breadth_first
from binary_tree.binary_tree import BinaryTree
from binary_tree.node import Node

def test_import():
    assert breadth_first

def test_empty_tree():
    tree = BinaryTree()

    actual = breadth_first(tree)
    expected = []
    assert actual == expected

