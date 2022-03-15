from leet_code.linkedlist_intersection import linked_intersection
from linked_list.linked_list import Node

def test_import():
    assert linked_intersection

def test_linked_intersection():
    three = Node(3)
    seven = Node(7)
    eight = Node(8)
    ten = Node(10)

    three.next = seven
    seven.next = eight
    eight.next = ten

    nintynine = Node(99)
    one = Node(1)

    nintynine.next = one
    one.next = eight

    actual = linked_intersection(three, nintynine)
    expected = eight
    assert actual == expected

def test_linked_intersection_overlap():
    three = Node(3)
    seven = Node(7)
    eight = Node(8)
    ten = Node(10)
    one = Node(1)

    three.next = seven
    seven.next = eight
    eight.next = ten
    ten.next = one

    actual = linked_intersection(three, eight)
    expected = eight
    assert actual == expected
