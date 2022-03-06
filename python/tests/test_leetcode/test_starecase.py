from leet_code.staircase import staircase_options

def test_import():
    assert staircase_options

def test_staircase_options():
    actual = staircase_options(4)
    expected = 5
    assert actual == expected

def test_staircase_options_3():
    actual = staircase_options(3)
    expected = 3
    assert actual == expected

def test_staircase_options_5():
    actual = staircase_options(5)
    expected = 8
    assert actual == expected
