from re import A
from leet_code.rand7 import rand_7

def test_import():
    assert rand_7

def test_example():
    options = [1, 2, 3, 4, 5, 6, 7]

    for _ in range(1000):
        num = rand_7()
        assert num in options
