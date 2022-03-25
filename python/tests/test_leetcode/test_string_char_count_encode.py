from leet_code.string_char_count_encode import encode_string
import pytest


def test_import():
    assert encode_string

@pytest.mark.skip()
def test_encoded_string():
    decoded = "AAAABBBCCDAA"

    actual = encode_string(decoded)
    expected = "4A3B2C1D2A"
    assert actual == expected

@pytest.mark.skip()
def test_encoded_string_2():
    decoded = "AAAABBBCCDAAA"

    actual = encode_string(decoded)
    expected = "4A3B2C1D3A"
    assert actual == expected

@pytest.mark.skip()
def test_encoded_string_3():
    decoded = "AAAAABBBBCCCDDAAA"

    actual = encode_string(decoded)
    expected = "5A4B3C2D3A"
    assert actual == expected
