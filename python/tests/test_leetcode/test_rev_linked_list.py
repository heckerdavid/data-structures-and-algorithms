from leet_code. rev_linkedlist import reverse_linked_list
from linked_list.linked_list import LinkedList

def test_import():
    assert reverse_linked_list

def test_ll_reverse():
    ll = LinkedList()
    for i in range(1, 11):
        ll.append(i)

    reverse_linked_list(ll)
    actual = str(ll)
    expected = '{ 10 } -> { 9 } -> { 8 } -> { 7 } -> { 6 } -> { 5 } -> { 4 } -> { 3 } -> { 2 } -> { 1 } -> NULL'
    assert actual == expected
