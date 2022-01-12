from hash_table.hash_table import HashTable

def test_import():
    assert HashTable

def test_hash():
    table = HashTable()

    actual = table.hash('cat')
    expected = 470
    assert actual == expected

def test_hash_same():
    table = HashTable()

    actual = table.hash('act')
    expected = 470
    assert actual == expected

def test_hash_int():
    table = HashTable()

    actual = table.hash(1)
    expected = 6
    assert actual == expected

def test_add():
    table = HashTable()
    table.add('cat', 'black')

    actual = table.table[470][0]
    expected = ('cat', 'black')
    assert actual == expected

def test_get():
    table = HashTable()
    table.add('cat', 'black')

    actual = table.get('cat')
    expected = 'black'
    assert actual == expected


def test_contains():
    table = HashTable()
    table.add('cat', 'black')

    actual = table.contains('cat')
    expected = True
    assert actual == expected

