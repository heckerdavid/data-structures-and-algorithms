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

def test_root():
    tree = BinaryTree(Node(5))

    actual = breadth_first(tree)
    expected = [5]
    assert actual == expected

def test_left():
    tree = BinaryTree(Node(5))
    tree.root.left = Node(4)

    actual = breadth_first(tree)
    expected = [5, 4]
    assert actual == expected


def test_right():
    tree = BinaryTree(Node(5))
    tree.root.left = Node(4)
    tree.root.right = Node(6)

    actual = breadth_first(tree)
    expected = [5, 4, 6]
    assert actual == expected


def test_level_3():
    tree = BinaryTree(Node(5))
    tree.root.left = Node(4)
    tree.root.right = Node(6)
    tree.root.left.left = Node(2)

    actual = breadth_first(tree)
    expected = [5, 4, 6, 2]
    assert actual == expected

def test_level_4():
    tree = BinaryTree(Node(1))
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    actual = breadth_first(tree)
    expected = [1, 2, 3, 4, 5, 6, 7]
    assert actual == expected
