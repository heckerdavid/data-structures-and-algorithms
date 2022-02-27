# given a binary tree ROOT, check if it is symmetric around its center (a mirror of itself)


def symmetric_tree(root):
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

