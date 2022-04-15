from re import L
from leet_code.lru_cache import LRU

def test_import():
    assert LRU


def test_lru():
    cache = LRU(2)

    cache.lru_set(1, 'test1')
    cache.lru_set(2, 'test2')
    cache.lru_get(2)

    actual = cache.lru_get(2)
    expected = 'test2'
    assert actual == expected

    cache.lru_set(3, 'test3')

    actual = cache.lru_get(1)
    expected = None
    assert actual == expected

    actual = cache.lru_get(3)
    expected = 'test3'
    assert actual == expected
