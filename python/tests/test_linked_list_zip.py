from linked_list_zip.linked_list_zip import zip_lists
from linked_list.linked_list import LinkedList, Node


def test_import():
    assert zip_lists

def test_zip_with_short_lists():
    new = LinkedList()
    new2 = LinkedList()
    new.append('a')
    new.append('b')
    new.append('c')

    new2.append(1)
    new2.append(2)
    new2.append(3)

    zip_lists(new, new2)

    actual = new.__str__()
    expected = "{ a } -> { 1 } -> { b } -> { 2 } -> { c } -> { 3 } -> NULL"
    assert actual == expected

def test_zip_with_longer_lists():
    new = LinkedList()
    new2 = LinkedList()
    new.append('a')
    new.append('b')
    new.append('c')
    new.append('d')
    new.append('e')
    new.append('f')

    new2.append(1)
    new2.append(2)
    new2.append(3)
    new2.append(4)
    new2.append(5)
    new2.append(6)

    zip_lists(new, new2)

    actual = new.__str__()
    expected = "{ a } -> { 1 } -> { b } -> { 2 } -> { c } -> { 3 } -> { d } -> { 4 } -> { e } -> { 5 } -> { f } -> { 6 } -> NULL"
    assert actual == expected

def test_zip_with_shorter_lists():
    new = LinkedList()
    new2 = LinkedList()
    new.append('a')
    new2.append(1)

    zip_lists(new, new2)

    actual = new.__str__()
    expected = "{ a } -> { 1 } -> NULL"
    assert actual == expected

def test_zip_with_uneven_lists():
    new = LinkedList()
    new2 = LinkedList()
    new.append('a')
    new.append('b')
    new.append('c')

    new2.append(1)
    new2.append(2)
    new2.append(3)
    new2.append(4)
    new2.append(5)
    new2.append(6)

    zip_lists(new, new2)

    actual = new.__str__()
    expected = "{ a } -> { 1 } -> { b } -> { 2 } -> { c } -> { 3 } -> { 4 } -> { 5 } -> { 6 } -> NULL"
    assert actual == expected

def test_per_the_assignment_1():
    new = LinkedList()
    new2 = LinkedList()
    new.append(1)
    new.append(3)
    new.append(2)

    new2.append(5)
    new2.append(9)
    new2.append(4)

    zip_lists(new, new2)

    actual = new.__str__()
    expected = "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> { 4 } -> NULL"
    assert actual == expected


def test_per_the_assignment_2():
    new = LinkedList()
    new2 = LinkedList()
    new.append(1)
    new.append(3)

    new2.append(5)
    new2.append(9)
    new2.append(4)

    zip_lists(new, new2)

    actual = new.__str__()
    expected = "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 4 } -> NULL"
    assert actual == expected


def test_per_the_assignment_3():
    new = LinkedList()
    new2 = LinkedList()
    new.append(1)
    new.append(3)
    new.append(2)

    new2.append(5)
    new2.append(9)

    zip_lists(new, new2)

    actual = new.__str__()
    expected = "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> NULL"
    assert actual == expected
