from hash_table.hash_table import HashTable
from tree_intersection.tree_intersection import find_common_values, convert_tree_to_hashtable, tree_intersection
from binary_tree.binary_search_tree import BinarySearchTree

def test_import():
    assert find_common_values
    assert convert_tree_to_hashtable
    assert tree_intersection

def test_convert_tree_to_hashtable():
    tree = BinarySearchTree()
    for i in range(10, 20):
        tree.add(i)

    actual = convert_tree_to_hashtable(tree)

    for i in range(10, 20):
        assert actual.get(i)

def test_convert_tree_to_hashtable():
    tree = BinarySearchTree()
    for i in range(10, 20):
        tree.add(i)

    actual = convert_tree_to_hashtable(tree)

    for i in range(10):
        assert not actual.get(i)

def test_common_values():
    tree = BinarySearchTree()
    for i in range(10, 20):
        tree.add(i)

    table = HashTable()

    for i in range(10, 20):
        table.add(i, True)

    actual = find_common_values(tree, table)
    expected = [i for i in range(10, 20)]
    assert actual == expected

def test_common_values_offset():
    tree = BinarySearchTree()
    for i in range(10, 20):
        tree.add(i)

    table = HashTable()

    for i in range(15, 25):
        table.add(i, True)

    actual = find_common_values(tree, table)
    expected = [15, 16, 17, 18, 19]
    assert actual == expected

def test_common_values_none():
    tree = BinarySearchTree()
    for i in range(10, 20):
        tree.add(i)

    table = HashTable()

    for i in range(10):
        table.add(i, True)

    actual = find_common_values(tree, table)
    expected = []
    assert actual == expected

def test_find_intersection():
    tree1 = BinarySearchTree()
    for i in range(10, 20):
        tree1.add(i)

    tree2 = BinarySearchTree()
    for i in range(10, 20):
        tree2.add(i)

    actual = tree_intersection(tree1, tree2)
    expected = [i for i in range(10,20)]
    assert actual == expected

def test_find_intersection_offset():
    tree1 = BinarySearchTree()
    for i in range(10, 20):
        tree1.add(i)

    tree2 = BinarySearchTree()
    for i in range(15, 25):
        tree2.add(i)

    actual = tree_intersection(tree1, tree2)
    expected = [15, 16, 17, 18, 19]
    assert actual == expected

def test_find_intersection_offset():
    tree1 = BinarySearchTree()
    for i in range(10, 20):
        tree1.add(i)

    tree2 = BinarySearchTree()
    for i in range(20, 30):
        tree2.add(i)

    actual = tree_intersection(tree1, tree2)
    expected = []
    assert actual == expected
