from leet_code.buy_sell_max import max_profit

def test_import():
    assert max_profit

def test_max_profit():
    prices = [7,1,5,3,6,4]

    actual = max_profit(prices)
    expected = 5
    assert actual == expected

def test_no_profit():
    prices = [7,6,4,3,1]

    actual = max_profit(prices)
    expected = 0
    assert actual == expected

def test_last_day():
    prices = [7,7,7,7,1,7]

    actual = max_profit(prices)
    expected = 6
    assert actual == expected

def test_first_day():
    prices = [1,7,7,7,7,7]

    actual = max_profit(prices)
    expected = 6
    assert actual == expected

def test_first_day():
    prices = [1,7,7,7,7,7]

    actual = max_profit(prices)
    expected = 6
    assert actual == expected
