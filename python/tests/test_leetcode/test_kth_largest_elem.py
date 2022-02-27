from leet_code.kth_largest_elem import kth_largest

def test_import():
    assert kth_largest

def test_kth_largest():
    nums = [4,2,9,7,5,6,7,1,3]
    k = 4

    actual = kth_largest(nums, k)
    expected = 6
    assert actual == expected


def test_kth_larg():
    nums = [7,6,5,4,3,2,1]
    k = 2

    actual = kth_largest(nums, k)
    expected = 6
    assert actual == expected


def test_negatives():
    nums = [-7,6,5,-4,3,-2,1]
    k = 2

    actual = kth_largest(nums, k)
    expected = 5
    assert actual == expected

def test_zeros():
    nums = [0,0,0,0,0]
    k = 2

    actual = kth_largest(nums, k)
    expected = 0
    assert actual == expected
