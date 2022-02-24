from cmath import exp
from leet_code.two_sum import two_sum

def test_import():
    assert two_sum

def test_two_sum():
    nums = [10, 15, 3, 7]
    k = 17
    actual = two_sum(nums, k)
    expected = True
    assert actual == expected


def test_two_sum_negatives():
    nums = [-10, 15, 3, -7]
    k = -17
    actual = two_sum(nums, k)
    expected = True
    assert actual == expected


def test_two_sum_repeat_vals():
    nums = [-10, -10, 15, 3, -7, -10]
    k = -17
    actual = two_sum(nums, k)
    expected = True
    assert actual == expected


def test_two_sum_no_match():
    nums = [-10, -10, 15, 3, -7, -10]
    k = -11
    actual = two_sum(nums, k)
    expected = False
    assert actual == expected


def test_two_sum_same_val():
    nums = [-10, 4, 15, 3, -10, 4]
    k = 8
    actual = two_sum(nums, k)
    expected = True
    assert actual == expected


def test_two_sum_same_val_once():
    nums = [-10, 4, 15, 3, -10]
    k = 8
    actual = two_sum(nums, k)
    expected = False
    assert actual == expected
