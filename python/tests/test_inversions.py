from leet_code.inversions import inversion_count

def test_import():
    assert inversion_count

def test_example():
    arr = [2, 4, 1, 3, 5]

    actual = inversion_count(arr)
    expected = 3
    assert actual == expected

def test_example2():
    arr = [5, 4, 3, 2, 1]

    actual = inversion_count(arr)
    expected = 10
    assert actual == expected

def test_example3():
    arr = [1, 2, 3, 4, 5]

    actual = inversion_count(arr)
    expected = 0
    assert actual == expected

def test_end():
    arr = [2, 3, 4, 5, 1]

    actual = inversion_count(arr)
    expected = 4
    assert actual == expected

def test_start():
    arr = [5, 1, 2, 3, 4]

    actual = inversion_count(arr)
    expected = 4
    assert actual == expected
