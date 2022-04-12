from leet_code.two_pluses import two_pluses_area

def test_import():
    assert two_pluses_area

def test_two_pluses_1():
    grid = [
        'GGGGGG',
        'GBBBGB',
        'GGGGGG',
        'GGBBGB',
        'GGGGGG',
    ]

    actual = two_pluses_area(grid)
    expected = 5
    assert actual == expected

def test_two_pluses_2():
    grid = [
        'BGBBGB',
        'GGGGGG',
        'BGBBGB',
        'GGGGGG',
        'BGBBGB',
        'BGBBGB',
    ]

    actual = two_pluses_area(grid)
    expected = 25
    assert actual == expected
