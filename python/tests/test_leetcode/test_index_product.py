from leet_code.index_product import product_index

def test_import():
    assert product_index

def test_prod_idx():
    nums = [1, 2, 3, 4, 5]

    actual = product_index(nums)
    expected = [120, 60, 40, 30, 24]
    assert actual == expected

def test_prod_idx_short():
    nums = [3, 2, 1]

    actual = product_index(nums)
    expected = [2, 3, 6]
    assert actual == expected


def test_prod_idx_negatives():
    nums = [-3, -2, -1]

    actual = product_index(nums)
    expected = [2, 3, 6]
    assert actual == expected



def test_prod_idx_mulitple_negatives():
    nums = [-3, -2, -1, -1]

    actual = product_index(nums)
    expected = [-2, -3, -6, -6]
    assert actual == expected

