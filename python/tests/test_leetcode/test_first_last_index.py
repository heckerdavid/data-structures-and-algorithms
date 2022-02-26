from leet_code.first_last_index import index_range

def test_import():
    assert index_range

def test_index_range():
    arr = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]
    target = 5

    actual = index_range(arr, target)
    expected = [2,6]
    assert actual == expected


def test_no_match():
    arr = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]
    target = 8

    actual = index_range(arr, target)
    expected = [-1, -1]
    assert actual == expected



def test_one_match():
    arr = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]
    target = 7

    actual = index_range(arr, target)
    expected = [7, 7]
    assert actual == expected


def test_start_match():
    arr = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]
    target = 2

    actual = index_range(arr, target)
    expected = [0, 0]
    assert actual == expected
