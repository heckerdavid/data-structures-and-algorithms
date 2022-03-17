def reverse_linked_list(linked_list):
    current = linked_list.head
    prev_node = None

    while current:
        next_node = current.next
        current.next = prev_node
        prev_node = current
        current = next_node

    linked_list.head = prev_node

    return linked_list

