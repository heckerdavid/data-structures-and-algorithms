import pytest
from linked_list.linked_list import LinkedList, Node


def test_get_length():
    new = LinkedList()
    new.insert(9)
    new.insert(8)
    new.insert(7)
    new.insert(9)
    new.insert(8)
    new.insert(7)
    actual = new.get_length(new.head)
    expected = 6
    assert actual == expected

def test_get_length():
    new = LinkedList()
    new.insert(9)
    new.insert(8)
    new.insert(7)
    new.insert(9)
    new.insert(8)
    new.insert(7)
    new.insert(9)
    new.insert(8)
    new.insert(7)
    actual = new.get_length(new.head)
    expected = 9
    assert actual == expected

def test_get_length_empty():
    new = LinkedList()

    actual = new.get_length(new.head)
    expected = 0
    assert actual == expected

def test_import():
    assert LinkedList

def test_node():
    assert Node()

def test_node_props():
    node = Node(1)
    actual = node.value
    expected = 1
    assert actual == expected

def test_linked_list():
    linked_list = LinkedList()
    actual = linked_list.head
    expected = None
    assert actual == expected


def test_insert():
    new = LinkedList()
    new.insert('9')
    actual = new.head.value
    expected = '9'
    assert actual == expected

def test_insert_many():
    new = LinkedList()
    new.insert(9)
    new.insert(8)
    new.insert(7)
    actual = new.head.value
    expected = 7
    assert actual == expected

def test_includes():
    new = LinkedList()
    new.insert(9)
    new.insert(8)
    new.insert(7)
    actual = new.includes(9)
    expected = True
    assert actual == expected

def test_includes_():
    new = LinkedList()
    new.insert(9)
    new.insert(8)
    new.insert(7)
    actual = new.includes(10)
    expected = False
    assert actual == expected

def test_str():
    new = LinkedList()
    new.insert(9)
    new.insert(8)
    new.insert(7)
    actual = new.__str__()
    expected = "{ 7 } -> { 8 } -> { 9 } -> NULL"
    assert actual == expected

def test_empty_str():
    new = LinkedList()
    actual = new.__str__()
    expected = "NULL"
    assert actual == expected

def test_delete():
    new = LinkedList()
    new.insert(9)
    new.insert(8)
    new.insert(7)
    new.delete(8)
    actual = new.__str__()
    expected = "{ 7 } -> { 9 } -> NULL"
    assert actual == expected

def test_delete_longer_list():
    new = LinkedList()
    new.insert(9)
    new.insert(8)
    new.insert(7)
    new.insert(9)
    new.insert(8)
    new.insert(9)
    new.insert(8)
    new.insert('this one')
    new.insert(7)
    actual = new.delete('this one')
    expected = "this one deleted from list."
    assert actual == expected


def test_append():
    new = LinkedList()
    new.insert(9)
    new.insert(8)
    new.insert(7)

    new.append(1)

    actual = new.__str__()
    expected = "{ 7 } -> { 8 } -> { 9 } -> { 1 } -> NULL"
    assert actual == expected

def test_append_many():
    new = LinkedList()
    new.insert(9)
    new.insert(8)
    new.insert(7)

    new.append(1)
    new.append(2)
    new.append(3)

    actual = new.__str__()
    expected = "{ 7 } -> { 8 } -> { 9 } -> { 1 } -> { 2 } -> { 3 } -> NULL"
    assert actual == expected



def test_append_empty():
    new = LinkedList()

    new.append(1)

    actual = new.head.value
    expected = 1
    assert actual == expected

def test_insert_before():
    new = LinkedList()
    new.insert(9)
    new.insert(8)
    new.insert(7)

    new.insert_before(8, 1)

    actual = new.__str__()
    expected = "{ 7 } -> { 1 } -> { 8 } -> { 9 } -> NULL"
    assert actual == expected

# @pytest.mark.skip('how do I test exceptions?')
def test_insert_before():
    new = LinkedList()
    new.insert(9)
    new.insert(8)
    new.insert(7)

    new.insert_before(7, 1)

    actual = new.__str__()
    expected = "{ 1 } -> { 7 } -> { 8 } -> { 9 } -> NULL"
    assert actual == expected


def test_insert_before_fail():
    new = LinkedList()
    new.insert(9)
    new.insert(8)
    new.insert(7)

    with pytest.raises(Exception):
        new.insert_before(6, 1)


def test_insert_after():
    new = LinkedList()
    new.insert(9)
    new.insert(8)
    new.insert(7)

    new.insert_after(8, 1)

    actual = new.__str__()
    expected = "{ 7 } -> { 8 } -> { 1 } -> { 9 } -> NULL"
    assert actual == expected

def test_insert_after_last():
    new = LinkedList()
    new.insert(9)
    new.insert(8)
    new.insert(7)

    new.insert_after(9, 1)

    actual = new.__str__()
    expected = "{ 7 } -> { 8 } -> { 9 } -> { 1 } -> NULL"
    assert actual == expected

def test_kth():
    new = LinkedList()
    assert new.kth_from_the_end

def test_kth_1():
    new = LinkedList()
    new.insert(9)
    new.insert(8)
    new.insert(7)


    actual = new.kth_from_the_end(0)
    expected = 9
    assert actual == expected



def test_kth_3():
    new = LinkedList()
    new.insert(9)
    new.insert(8)
    new.insert(7)
    new.insert(6)
    new.insert(5)
    new.insert(4)
    new.insert(3)
    new.insert(2)

    actual = new.kth_from_the_end(3)
    expected = 6
    assert actual == expected

def test_kth_long_list():
    new = LinkedList()
    new.insert(9)
    new.insert(8)
    new.insert(7)
    new.insert(6)
    new.insert(5)
    new.insert(4)
    new.insert(3)
    new.insert(2)
    new.insert(9)
    new.insert(8)
    new.insert(7)
    new.insert(6)
    new.insert(5)
    new.insert(4)
    new.insert(3)
    new.insert(2)

    actual = new.kth_from_the_end(7)
    expected = 2
    assert actual == expected

def test_kth_greater_than_list():
    new = LinkedList()
    new.insert(9)
    new.insert(8)
    new.insert(7)


    actual = new.kth_from_the_end(4)
    expected = '4 is larger than the length of this list'
    assert actual == expected

def test_kth_negative():
    new = LinkedList()
    new.insert(9)
    new.insert(8)
    new.insert(7)

    actual = new.kth_from_the_end(-4)
    expected = None
    assert actual == expected

def test_kth_short():
    new = LinkedList()
    new.insert(9)

    actual = new.kth_from_the_end(0)
    expected = 9
    assert actual == expected
