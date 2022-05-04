from leet_code.zip_list import list_zip

def test_import():
    assert list_zip

def test_middle_zip():
    unzipped = [1, 2, 3, 4, 5, 6]

    actual = list_zip(unzipped, 3)
    expected = [1, 4, 2, 5, 3, 6]
    assert actual == expected

def test_middle_zip():
    unzipped = [1, 2, 3, 4, 5, 6]

    actual = list_zip(unzipped, 3)
    expected = [1, 4, 2, 5, 3, 6]
    assert actual == expected

def test_middle_zip_long():
    unzipped = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    actual = list_zip(unzipped, 5)
    expected = [1, 6, 2, 7, 3, 8, 4, 9, 5, 10]
    assert actual == expected
