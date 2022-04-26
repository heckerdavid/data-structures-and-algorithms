from leet_code.grid_sort import sort_diag

def test_import():
    assert sort_diag

def test_2_x_2():
    grid = [
        [1, 1],
        [2, 2],
    ]

    sort_diag(grid)

    actual = grid
    expected = [
        [1, 2],
        [1, 2],
    ]
    assert actual == expected
