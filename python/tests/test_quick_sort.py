from sorts.quick_sort import quick_sort

def test_import():
    assert quick_sort.quick_sort

def test_sorted():
    unsorted_list = [1,2,3,4,5]
    actual = quick_sort.quick_sort(unsorted_list, 0, len(unsorted_list) - 1)
    expected = [1,2,3,4,5]
    assert unsorted_list == expected

def test_almost_sorted():
    unsorted_list = [1,3,2,4,5]
    actual = quick_sort.quick_sort(unsorted_list, 0, len(unsorted_list) - 1)
    expected = [1,2,3,4,5]
    assert unsorted_list == expected

def test_unsorted():
    unsorted_list = [4,3,1,5,2]
    actual = quick_sort.quick_sort(unsorted_list, 0, len(unsorted_list) - 1)
    expected = [1,2,3,4,5]
    assert unsorted_list == expected

def test_reversed():
    unsorted_list = [5,4,3,2,1]
    actual = quick_sort.quick_sort(unsorted_list, 0, len(unsorted_list) - 1)
    expected = [1,2,3,4,5]
    assert unsorted_list == expected

def test_duplicate_nums():
    unsorted_list = [5,4,5,4,3,2,3,2,1,1]
    actual = quick_sort.quick_sort(unsorted_list, 0, len(unsorted_list) - 1)
    expected = [1,1,2,2,3,3,4,4,5,5]
    assert unsorted_list == expected
