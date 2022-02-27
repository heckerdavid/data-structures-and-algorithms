from leet_code.pair_construct import car, cdr, cons


def test_import():
    assert car
    assert cdr
    assert cons

def test_car():
    actual = car(cons(3, 4))
    expected = 3
    assert actual == expected


def test_cdr():
    actual = cdr(cons(3, 4))
    expected = 4
    assert actual == expected
