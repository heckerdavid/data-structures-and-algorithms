from os import link
from leet_code.kth_from_end import remove_kth_from_end
from linked_list.linked_list import LinkedList


def test_import():
    assert remove_kth_from_end

def test_remove_kth_1():
    linked = LinkedList()
    for i in range(1,11):
        linked.append(i)

    remove_kth_from_end(linked, 1)

    actual = str(linked)
    expected = '{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 5 } -> { 6 } -> { 7 } -> { 8 } -> { 10 } -> NULL'
    assert actual == expected

def test_remove_kth_2():
    linked = LinkedList()
    for i in range(1,11):
        linked.append(i)

    remove_kth_from_end(linked, 2)

    actual = str(linked)
    expected = '{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 5 } -> { 6 } -> { 7 } -> { 9 } -> { 10 } -> NULL'
    assert actual == expected

def test_remove_kth_last():
    linked = LinkedList()
    for i in range(1,11):
        linked.append(i)

    remove_kth_from_end(linked, 0)

    actual = str(linked)
    expected = '{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 5 } -> { 6 } -> { 7 } -> { 8 } -> { 9 } -> NULL'
    assert actual == expected

def test_remove_kth_first():
    linked = LinkedList()
    for i in range(1,11):
        linked.append(i)

    remove_kth_from_end(linked, 9)

    actual = str(linked)
    expected = '{ 2 } -> { 3 } -> { 4 } -> { 5 } -> { 6 } -> { 7 } -> { 8 } -> { 9 } -> { 10 } -> NULL'
    assert actual == expected
