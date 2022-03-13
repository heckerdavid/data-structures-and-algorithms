# given a binary tree ROOT, check if it is symmetric around its center (a mirror of itself)


def symmetric_tree_first_attempt(root):
    left = in_order_list(root.left)
    right = in_order_list(root.right)

    if left == list(reversed(right)):
        return True
    return False

def in_order_list(root):
    output = []

    def walk(root):
        nonlocal output
        if not root:
            return
        walk(root.left)
        output.append(root.value)
        walk(root.right)

    walk(root)

    return output

# second attempt
def symmetric_tree(root):
    return is_symmetric(root, root)

def is_symmetric(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is None or root2 is None:
        return False

    return root1.value == root2.value and is_symmetric(root1.left, root2.right) and is_symmetric(root1.right, root2.left)
