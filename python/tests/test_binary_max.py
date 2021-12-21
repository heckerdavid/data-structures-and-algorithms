from binary_tree.binary_tree import BinaryTree
from binary_tree.node import Node

def test_import():
    assert BinaryTree()

def test_find_max_in_empty():
    tree = BinaryTree()
    actual = tree.find_max_value()
    expected = None
    assert actual == expected

def test_max_is_root():
    tree = BinaryTree()
    tree.root.value = 10

    actual = tree.find_max_value()
    expected = 10
    assert actual == expected

def test_max_is_left():
    tree = BinaryTree()
    tree.root.value = 10
    tree.root.left = Node(11)

    actual = tree.find_max_value()
    expected = 11
    assert actual == expected

def test_max_is_right():
    tree = BinaryTree()
    tree.root.value = 10
    tree.root.left = Node(11)
    tree.root.right = Node(12)

    actual = tree.find_max_value()
    expected = 12
    assert actual == expected

def test_max():
    tree = BinaryTree()
    tree.root.value = 10
    tree.root.left = Node(11)
    tree.root.left.right = Node(11)
    tree.root.left.left = Node(11)
    tree.root.right = Node(12)
    tree.root.right.left = Node(15)
    tree.root.right.right = Node(12)

    actual = tree.find_max_value()
    expected = 15
    assert actual == expected
