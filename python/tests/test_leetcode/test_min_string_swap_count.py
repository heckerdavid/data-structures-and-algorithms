from itertools import count
from leet_code.min_string_swap_count import count_swaps

def test_import():
    assert count_swaps


def test_min_count_example():
    s1 = 'kitten'
    s2 = 'sitting'

    actual = count_swaps(s1, s2)
    expected = 3
    assert actual == expected


def test_repeat():
    s1 = 'kitten'
    s2 = 'kitten'

    actual = count_swaps(s1, s2)
    expected = 0
    assert actual == expected

# TODO: Should this return two or zero?
def test_anagram():
    s1 = 'there'
    s2 = 'three'

    actual = count_swaps(s1, s2)
    expected = 0
    assert actual == expected


def test_length():
    s1 = 'k'
    s2 = 'kitten'

    actual = count_swaps(s1, s2)
    expected = 5
    assert actual == expected
