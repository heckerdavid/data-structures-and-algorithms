from this import d
from leet_code.num_sum_range import sum_digits

def test_import():
    assert sum_digits

def test_num_sum():
    num = 20
    target = 5

    actual = sum_digits(num, target)
    expected = 2
    assert actual == expected

def test_num_sum_30():
    num = 30
    target = 6

    actual = sum_digits(num, target)
    expected = 3
    assert actual == expected

def test_num_sum_42():
    num = 42
    target = 6

    actual = sum_digits(num, target)
    expected = 5
    assert actual == expected
