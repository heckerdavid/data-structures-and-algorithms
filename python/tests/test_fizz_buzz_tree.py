from CodeFellows401.fizz_buzz_tree.fizz_buzz_tree import fizz_buzz_tree
from k_ary_tree.k_ary_tree import KaryTree
from k_ary_tree.node import Node

def test_import():
    assert fizz_buzz_tree

def test_root():
    tree = KaryTree()
    tree.root = Node(1)

    actual = fizz_buzz_tree(tree).root.value
    expected = '1'
    assert actual == expected

def test_root_children():
    tree = KaryTree()
    tree.root = Node(1)
    tree.add(2)

    actual_tree = fizz_buzz_tree(tree)
    assert isinstance(actual_tree, KaryTree)

def test_root_multiple_children():
    tree = KaryTree()
    tree.root = Node(1)
    tree.root.children.append(Node(2))
    tree.root.children.append(Node(3))

    actual = fizz_buzz_tree(tree)

    assert isinstance(actual, KaryTree)
