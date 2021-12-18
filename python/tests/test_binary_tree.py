from binary_tree.binary_tree import BinaryTree
from binary_tree.node import Node

'''
Can successfully instantiate an empty tree
Can successfully instantiate a tree with a single root node
Can successfully add a left child and right child to a single root node

Can successfully return a collection from a preorder traversal
Can successfully return a collection from an inorder traversal
Can successfully return a collection from a postorder traversal'''

def test_import():
    assert BinaryTree
    assert Node

def test_node():
    node = Node(9)
    actual = node.value
    expected = 9
    assert actual == expected

def test_node_left():
    node = Node(9)
    actual = node.left
    expected = None
    assert actual == expected

def test_node_right():
    node = Node(9)
    actual = node.right
    expected = None
    assert actual == expected

def test_empty_tree():
    tree = BinaryTree()
    actual = tree.root.value
    expected = None
    assert actual == expected

def test_empty_tree_children():
    tree = BinaryTree()
    actual = tree.root.left
    expected = None
    assert actual == expected

def test_add_to_tree():
    tree = BinaryTree(1)

    actual = tree.root.value
    expected = 1
    assert actual == expected

def test_add_left_to_tree():
    tree = BinaryTree(3)
    tree.add(2)

    actual = tree.root.left.value
    expected = 2
    assert actual == expected

def test_add_right_to_tree():
    tree = BinaryTree(3)
    tree.add(2)
    tree.add(5)

    actual = tree.root.right.value
    expected = 5
    assert actual == expected

def test_preorder():
    tree = BinaryTree()
    tree.root = Node(3)
    tree.root.left = Node(2)
    tree.root.right = Node(4)

    actual = tree.pre_order()
    expected = [3, 2, 4]
    assert actual == expected

def test_in_order():
    tree = BinaryTree()
    tree.root = Node(3)
    tree.root.left = Node(2)
    tree.root.right = Node(4)

    actual = tree.in_order()
    expected = [2, 3, 4]
    assert actual == expected

def test_post_order():
    tree = BinaryTree()
    tree.root = Node(3)
    tree.root.left = Node(2)
    tree.root.right = Node(4)

    actual = tree.post_order()
    expected = [2, 4, 3]
    assert actual == expected
