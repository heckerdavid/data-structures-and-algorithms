from k_ary_tree.k_ary_tree import KaryTree
from k_ary_tree.node import Node


def fizz_buzz_tree(tree):
    if tree.root is None:
        return None

    new_tree = KaryTree()

    def walk(root):
        if root is None:
            return
        nonlocal new_tree
        if root.value % 3 == 0 and root.value % 5 == 0:
            new_tree.add('fizzbuzz')
        elif root.value % 5 == 0:
            new_tree.add('buzz')
        elif root.value % 3 == 0:
            new_tree.add('fizz')
        else:
            new_tree.add(str(root.value))
        for child in root.children:
            walk(child)

    walk(tree.root)

    return new_tree
