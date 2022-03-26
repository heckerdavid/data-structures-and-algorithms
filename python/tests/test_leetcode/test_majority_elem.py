from leet_code.majority_elem import find_majority

def test_import():
    assert find_majority

def test_example_1():
    nums = [3, 2, 3]

    actual = find_majority(nums)
    expected = 3
    assert actual == expected

def test_example_2():
    nums = [2, 2, 1, 1, 1, 2, 2]

    actual = find_majority(nums)
    expected = 2
    assert actual == expected

def test_end_point():
    nums = [1, 2, 1, 2, 1, 2, 2]

    actual = find_majority(nums)
    expected = 2
    assert actual == expected

def test_start():
    nums = [1, 1, 2, 1, 2, 1, 2]

    actual = find_majority(nums)
    expected = 1
    assert actual == expected
