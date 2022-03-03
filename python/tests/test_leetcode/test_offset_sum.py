from leet_code.offset_sum import non_adjacent_sum

def test_import():
    assert non_adjacent_sum

def test_offset_sum():
    nums_list = [2, 4, 6, 2, 5]

    actual = non_adjacent_sum(nums_list)
    expected = 13
    assert actual == expected

def test_offset_sum_2():
    nums_list = [5, 1, 1, 5]

    actual = non_adjacent_sum(nums_list)
    expected = 10
    assert actual == expected

def test_non_highest_option():
    nums_list = [9, 10, 9, 1, 1, 5]

    actual = non_adjacent_sum(nums_list)
    expected = 23
    assert actual == expected

def test_some_negatives():
    nums_list = [-9, 10, -9, 1, 1, 5]

    actual = non_adjacent_sum(nums_list)
    expected = 16
    assert actual == expected

def test_inverse_negatives():
    nums_list = [9, -10, 9, -1, -1, -5]

    actual = non_adjacent_sum(nums_list)
    expected = 17
    assert actual == expected

def test_first_val():
    nums_list = [9, 1, 1, 1, 1, 1]

    actual = non_adjacent_sum(nums_list)
    expected = 11
    assert actual == expected

def test_last_val():
    nums_list = [1, 1, 1, 1, 1, 9]

    actual = non_adjacent_sum(nums_list)
    expected = 11
    assert actual == expected

def test_zeros():
    nums_list = [1, 0, 1, 0, 1, 0]

    actual = non_adjacent_sum(nums_list)
    expected = 3
    assert actual == expected

def test_all_zeros():
    nums_list = [0, 0, 0, 0, 0, 0]

    actual = non_adjacent_sum(nums_list)
    expected = 0
    assert actual == expected
