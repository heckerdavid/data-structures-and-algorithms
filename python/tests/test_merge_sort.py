from sorts.merge_sort import merge_sort

def test_import():
    assert merge_sort.merge_sort

def test_sorted():
    actual = merge_sort.merge_sort([1,2,3,4,5])
    expected = [1,2,3,4,5]
    assert actual == expected

def test_almost_sorted():
    actual = merge_sort.merge_sort([1,3,2,4,5])
    expected = [1,2,3,4,5]
    assert actual == expected

def test_unsorted():
    actual = merge_sort.merge_sort([4,3,1,5,2])
    expected = [1,2,3,4,5]
    assert actual == expected

def test_reversed():
    actual = merge_sort.merge_sort([5,4,3,2,1])
    expected = [1,2,3,4,5]
    assert actual == expected

def test_duplicate_nums():
    actual = merge_sort.merge_sort([5,4,5,4,3,2,3,2,1,1])
    expected = [1,1,2,2,3,3,4,4,5,5]
    assert actual == expected
