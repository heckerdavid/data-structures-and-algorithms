from leet_code.move_zeros import shift_zeros

def test_import():
    assert shift_zeros

def test_shift_zeros():
    nums = [0,1,0,3,12]

    actual = shift_zeros(nums)
    expected = [1,3,12,0,0]
    assert actual == expected

def test_shift_zeros_2():
    nums = [0]

    actual = shift_zeros(nums)
    expected = [0]
    assert actual == expected

def test_shift_zeros_3():
    nums = [0,1,2,3]

    actual = shift_zeros(nums)
    expected = [1,2,3,0]
    assert actual == expected

def test_shift_zeros_4():
    nums = [0,0,0,0,1,2,3]

    actual = shift_zeros(nums)
    expected = [1,2,3,0,0,0,0]
    assert actual == expected

def test_shift_zeros_5():
    nums = [1,0,2,0,3,0,0]

    actual = shift_zeros(nums)
    expected = [1,2,3,0,0,0,0]
    assert actual == expected

def test_shift_zeros_6():
    nums = [1,2,3,4]

    actual = shift_zeros(nums)
    expected = [1,2,3,4]
    assert actual == expected
