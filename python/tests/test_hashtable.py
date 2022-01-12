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
