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
    table.add('bat', 'blac')
    table.add('mat', 'blak')

    actual = table.get('cat')
    expected = 'black'
    assert actual == expected

def test_get_():
    table = HashTable()
    table.add('cat', 'black')
    table.add('bat', 'blac')
    table.add('mat', 'blak')

    actual = table.get('bat')
    expected = 'blac'
    assert actual == expected

def test_get_not_in():
    table = HashTable()
    table.add('cat', 'black')
    table.add('bat', 'blac')
    table.add('mat', 'blak')

    actual = table.get('fat')
    expected = None
    assert actual == expected

def test_get_collision():
    table = HashTable()
    table.add('cat', 'black')
    table.add('act', 'blac')
    table.add('tac', 'blak')

    actual = table.get('tac')
    expected = 'blak'
    assert actual == expected

def test_contains():
    table = HashTable()
    table.add('cat', 'black')

    actual = table.contains('cat')
    expected = True
    assert actual == expected

def test_does_not_contain():
    table = HashTable()
    table.add('dogs', 'golden')
    table.add('cat', 'black')

    actual = table.contains('dog')
    expected = False
    assert actual == expected



def test_contains():
    table = HashTable()
    table.add('cat', 'black')

    actual = table.remove('cat')
    expected = 'black'
    assert actual == expected
