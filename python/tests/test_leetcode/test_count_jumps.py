from leet_code.count_jumps import min_jumps

def test_import():
    assert min_jumps

def test_min_jumps():
    nums = [2,3,1,1,4]

    actual = min_jumps(nums)
    expected = 2
    assert actual == expected

def test_min_jumps_2():
    nums = [2,3,0,1,4]

    actual = min_jumps(nums)
    expected = 2
    assert actual == expected

def test_min_jumps_in_order():
    nums = [1,2,3]

    actual = min_jumps(nums)
    expected = 2
    assert actual == expected

def test_min_jumps_rev_order():
    nums = [3,2,1]

    actual = min_jumps(nums)
    expected = 1
    assert actual == expected

def test_min_jumps_ones():
    nums = [1,1,1,1,1]

    actual = min_jumps(nums)
    expected = 4
    assert actual == expected
