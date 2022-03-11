from leet_code.valid_bst import is_valid_bst
from binary_tree.binary_search_tree import BinarySearchTree
def test_import():
    assert is_valid_bst

def test_valid_bst():
    tree = BinarySearchTree()
    tree.add(8)
    tree.add(5)
    tree.add(9)
    #      8
    #   5     9

    actual = is_valid_bst(tree.root)
    expected = True
    assert actual == expected


def test_invalid_bst():
    tree = BinarySearchTree()
    tree.add(8)
    tree.add(5)
    tree.add(9)
    tree.root.right.value = 1
    #      8
    #   5     1

    actual = is_valid_bst(tree.root)
    expected = False
    assert actual == expected

def test_depth():
    tree = BinarySearchTree()
    tree.add(8)
    tree.add(5)
    tree.add(11)
    tree.add(3)
    tree.add(7)
    tree.add(9)
    tree.add(12)

    #        8
    #     5      11
    #   3   7   9   12

    actual = is_valid_bst(tree.root)
    expected = True
    assert actual == expected


def test_invalid_depth():
    tree = BinarySearchTree()
    tree.add(8)
    tree.add(5)
    tree.add(11)
    tree.add(3)
    tree.add(7)
    tree.add(9)
    tree.add(12)
    tree.root.right.left.value = 3

    #        8
    #     5      11
    #   3   7   3   12

    actual = is_valid_bst(tree.root)
    expected = False
    assert tree.in_order() == [3,5,7,8,3,11,12]
    assert actual == expected
