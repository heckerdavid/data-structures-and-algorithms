# Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

# The list is very long, so making more than one pass is prohibitively expensive.

# Do this in constant space and in one pass.

def remove_kth_from_end(linked_list, k):
    prev = linked_list.head
    current = linked_list.head
    leader = linked_list.head

    for _ in range(k + 1):
        leader = leader.next

    while leader:
        leader = leader.next
        prev = current
        current = current.next


    if prev is current:
        linked_list.head = current.next
        return
    next_node = current.next
    prev.next = next_node
