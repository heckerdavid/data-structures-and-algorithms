from leet_code.min_rooms import minimum_rooms

def test_import():
    assert minimum_rooms


def test_minimum_rooms_example():
    times = [(30, 75), (0, 50), (60, 150)]

    actual = minimum_rooms(times)
    expected = 2
    assert actual == expected


def test_minimum_rooms_fill_gap():
    times = [(51, 58), (60, 150), (30, 75), (0, 50)]

    actual = minimum_rooms(times)
    expected = 2
    assert actual == expected


def test_minimum_rooms_empty():
    times = []

    actual = minimum_rooms(times)
    expected = 0
    assert actual == expected


def test_minimum_rooms_one():
    times = [(7, 9)]

    actual = minimum_rooms(times)
    expected = 1
    assert actual == expected


def test_minimum_rooms_same():
    times = [(7, 9), (7, 9)]

    actual = minimum_rooms(times)
    expected = 2
    assert actual == expected
