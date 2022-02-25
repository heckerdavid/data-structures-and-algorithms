from leet_code.anagram import is_anagram


def test_import():
    assert is_anagram

def test_anagram():
    s1 = 'danger'
    s2 = 'garden'

    actual = is_anagram(s1, s2)
    expected = True
    assert actual == expected

def test_repeat_letters():
    s1 = 'three'
    s2 = 'there'

    actual = is_anagram(s1, s2)
    expected = True
    assert actual == expected

def test_repeat_letters_order():
    s1 = 'there'
    s2 = 'three'

    actual = is_anagram(s1, s2)
    expected = True
    assert actual == expected

def test_false():
    s1 = 'greed'
    s2 = 'gred'

    actual = is_anagram(s1, s2)
    expected = False
    assert actual == expected

def test_false_order():
    s1 = 'gred'
    s2 = 'greed'

    actual = is_anagram(s1, s2)
    expected = False
    assert actual == expected
