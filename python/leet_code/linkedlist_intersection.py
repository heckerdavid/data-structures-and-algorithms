# Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

# Example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

# In this example, assume nodes with the same value are the exact same node objects.
# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.



def linked_intersection(linked_list1, linked_list2):

    stopping_point = None
    prev_a = None
    prev_b = None


    while prev_a == prev_b:
        stopping_point = prev_a
        prev_a = traverse_to_stopping_point(linked_list1, stopping_point)
        prev_b = traverse_to_stopping_point(linked_list2, stopping_point)

    return stopping_point

def traverse_to_stopping_point(linked_list_node, stopping_point):
    current = linked_list_node
    prev = current

    while current != stopping_point:
        prev = current
        current = current.next

    return prev
