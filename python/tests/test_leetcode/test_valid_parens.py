from leet_code.valid_parenthesis import valid_parens

def test_import():
    assert valid_parens

def test_one_valid():
    s = '()'

    actual = valid_parens(s)
    expected = True
    assert actual == expected

def test_three_valid():
    s = '()[]{}'

    actual = valid_parens(s)
    expected = True
    assert actual == expected

def test_three_invalid():
    s = '()[}]{}'

    actual = valid_parens(s)
    expected = False
    assert actual == expected

def test_openers():
    s = '(([[{{'

    actual = valid_parens(s)
    expected = False
    assert actual == expected

def test_closers():
    s = '}}))]]'

    actual = valid_parens(s)
    expected = False
    assert actual == expected

def test_imbedded():
    s = '()[({})]{}'

    actual = valid_parens(s)
    expected = True
    assert actual == expected

def test_invalid_imbedded():
    s = '()[({[})]{}]'

    actual = valid_parens(s)
    expected = False
    assert actual == expected
