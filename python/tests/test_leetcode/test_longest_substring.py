from leet_code.longest_substring import max_substring

def test_import():
    assert max_substring

def test_max_substring():
    string = 'abcba'
    k = 2

    actual = max_substring(string, k)
    expected = 3
    assert actual == expected

def test_max_substring_end():
    string = 'abcbaffff'
    k = 2

    actual = max_substring(string, k)
    expected = 5
    assert actual == expected

def test_max_substring_beginning():
    string = 'ffffabcba'
    k = 2

    actual = max_substring(string, k)
    expected = 5
    assert actual == expected
