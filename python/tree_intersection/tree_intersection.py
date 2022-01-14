from hash_table.hash_table import HashTable


def tree_intersection(first_binary_tree, second_binary_tree) -> list:

    seen_table = convert_tree_to_hashtable(first_binary_tree)

    return find_common_values(second_binary_tree, seen_table)


def find_common_values(binary_tree, hashtable) -> list:
    root = binary_tree.root
    return_list = []

    def walk(root, hashtable):
        if root is None:
            return

        nonlocal return_list

        if hashtable.get(root.value):
            return_list.append(root.value)

        walk(root.left, hashtable)
        walk(root.right, hashtable)

    walk(binary_tree.root, hashtable)

    return return_list

def convert_tree_to_hashtable(binary_tree):
    root = binary_tree.root
    hashtable = HashTable()

    def walk(root):
        if root is None:
            return

        nonlocal hashtable
        hashtable.add(root.value, True)
        walk(root.left)
        walk(root.right)

    walk(root)
    return hashtable
