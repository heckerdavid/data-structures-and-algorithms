from leet_code.set_pairs import subsets
import pytest

def test_import():
    assert subsets

def test_example():
    nums = [1, 2, 3]

    actual = subsets(nums)
    expected = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    assert sorted(actual) == sorted(expected)

def test_empty():
    nums = []

    actual = subsets(nums)
    expected = [[]]
    assert sorted(actual) == sorted(expected)

def test_single():
    nums = [1]

    actual = subsets(nums)
    expected = [[], [1]]
    assert sorted(actual) == sorted(expected)

def test_double():
    nums = [1, 2]

    actual = subsets(nums)
    expected = [[], [1], [2], [1, 2]]
    assert sorted(actual) == sorted(expected)
# @pytest.mark.skip("how to handle four?")
def test_four():
    nums = [1, 2, 3, 4]

    actual = subsets(nums)
    expected = [[], [1], [2], [3], [4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4], [1, 2, 3], [2, 3, 4], [1, 2, 3, 4]]
    assert sorted(actual) == sorted(expected)

def test_five():
    nums = [1, 2, 3, 4, 5]

    actual = subsets(nums)
    expected = [[], [1], [2], [3], [4], [5], [1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5], [1, 2, 3], [2, 3, 4], [3, 4, 5], [1, 2, 3, 4], [2, 3, 4, 5], [1, 2, 3, 4, 5]]
    assert sorted(actual) == sorted(expected)
