from leet_code.nth_from_end import Solution
from linked_list.linked_list import LinkedList
import pytest

def test_import():
    assert Solution

def test_empty_list():
    linked = LinkedList()
    head = linked.head

    solution = Solution()

    with pytest.raises(IndexError):
        solution.removeNthFromEnd(head,1)

def test_last_node():
    linked = LinkedList()
    linked.append(1)
    linked.append(2)
    linked.append(3)
    linked.append(4)
    head = linked.head
    solution = Solution()

    solution.removeNthFromEnd(head, 1)
    actual = str(linked)
    expected = '{ 1 } -> { 2 } -> { 3 } -> NULL'
    assert actual == expected


def test_middle_node():
    linked = LinkedList()
    linked.append(1)
    linked.append(2)
    linked.append(3)
    head = linked.head
    solution = Solution()

    solution.removeNthFromEnd(head, 2)
    actual = str(linked)
    expected = '{ 1 } -> { 3 } -> NULL'
    assert actual == expected

@pytest.mark.skip()
def test_first_node():
    linked = LinkedList()
    linked.append(1)
    linked.append(2)
    linked.append(3)
    head = linked.head
    solution = Solution()

    solution.removeNthFromEnd(head, 3)
    actual = str(linked)
    expected = '{ 1 } -> { 3 } -> NULL'
    assert actual == expected
