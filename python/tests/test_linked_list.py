from linked_list.linked_list import LinkedList, Node


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
