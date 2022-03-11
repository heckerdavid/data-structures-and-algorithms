# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

def is_valid_bst(root, min_val=float("-inf"), max_val=float('inf')):
    if root is None:
        return True

    if root.value <= min_val or root.value >= max_val:
        return False

    return is_valid_bst(root.left, min_val, root.value) and is_valid_bst(root.right, root.value, max_val)
