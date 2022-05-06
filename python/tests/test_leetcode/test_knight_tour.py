from black import assert_equivalent
from leet_code.knight_tour import solution

def test_import():
    assert solution

def test_knight_tour():
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]

    actual = solution(3, 3, grid)
    expected = True
    assert actual == expected

