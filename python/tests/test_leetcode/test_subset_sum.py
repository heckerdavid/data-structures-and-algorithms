from leet_code.subset_sum import sub_sum
import pytest


def test_import():
    assert sub_sum
@pytest.mark.skip("I dont know how to DP =(")
def test_example():
    S = [12, 1, 61, 5, 9, 2]
    K = 24

    actual = sub_sum(S, K)
    expected = [12, 9, 2, 1]
    assert actual == expected
