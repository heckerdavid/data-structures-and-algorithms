import pytest
from leet_code.iter_max_in_ll import find_max
from linked_list.linked_list import LinkedList

def test_import():
    assert find_max

def test_short_list():
    linked = LinkedList()
    for i in range(8 + 1):
        linked.append(i)

    actual = find_max(linked)
    expected = 8
    assert actual == expected


def test_long_list():
    linked = LinkedList()
    for i in range(80 + 1):
        linked.append(i)

    actual = find_max(linked)
    expected = 80
    assert actual == expected

def test_negatives():
    linked = LinkedList()
    for i in range(-10, 80 + 1):
        linked.append(i)

    actual = find_max(linked)
    expected = 80
    assert actual == expected

def test_repeated():
    linked = LinkedList()
    for i in range(8 + 1):
        linked.append(i)
    linked.append(4)
    linked.append(5)
    linked.append(6)

    actual = find_max(linked)
    expected = 8
    assert actual == expected

def test_empty_list():
    linked = LinkedList()

    with pytest.raises(ValueError):
        find_max(linked)
