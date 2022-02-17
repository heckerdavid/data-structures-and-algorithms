# Given a linked list, find the maximum value iteratively

def find_max(linked_list):
    current = linked_list.head
    if not current:
        raise ValueError

    max_value = -1000000000
    while current:
        if current.value > max_value:
            max_value = current.value
        current = current.next

    return max_value
