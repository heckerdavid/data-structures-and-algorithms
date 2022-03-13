from re import sub
from leet_code.max_in_sub_array import sub_array_max

def test_import():
    assert sub_array_max

def test_max_sub_array():
    array = [10, 5, 2, 7, 8, 7]
    k = 3

    actual = sub_array_max(array, k)
    expected = [10, 7, 8, 8]
    assert actual == expected

def test_max_sub_array_same():
    array = [10, 10, 10, 10, 10, 10]
    k = 2

    actual = sub_array_max(array, k)
    expected = [10, 10, 10, 10, 10]
    assert actual == expected

def test_max_sub_array_alt():
    array = [10, 1, 10, 1, 10, 1]
    k = 2

    actual = sub_array_max(array, k)
    expected = [10, 10, 10, 10, 10]
    assert actual == expected

def test_max_sub_array_des():
    array = [10, 9, 8, 7,6]
    k = 2

    actual = sub_array_max(array, k)
    expected = [10, 9, 8, 7]
    assert actual == expected

def test_max_sub_array_asc():
    array = [6, 7, 8, 9, 10]
    k = 2

    actual = sub_array_max(array, k)
    expected = [7, 8, 9, 10]
    assert actual == expected

def test_max_sub_array_full_len():
    array = [6, 7, 8, 9, 10]
    k = 5

    actual = sub_array_max(array, k)
    expected = [10]
    assert actual == expected

def test_max_sub_array_full_len_1():
    array = [6, 7, 8, 9, 10]
    k = 4

    actual = sub_array_max(array, k)
    expected = [9, 10]
    assert actual == expected
