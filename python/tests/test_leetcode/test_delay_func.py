from leet_code.delay_func import delay
import time
import pytest

def test_import():
    assert delay

@pytest.mark.skip()
def test_delay():
    def func():
        pass

    t1 = time.time_ns()
    func()
    t2 = time.time_ns()
    no_delay_runtime = (t2 - t1) * 1000000

    artificial_delay = 100000 #ms
    t3 = time.time_ns() #ns
    delay(func, artificial_delay)
    t4 = time.time_ns() #ns
    delay_runtime = (t4 - t3) * 1000000 #ms

    assert delay_runtime > no_delay_runtime
    assert delay_runtime >= artificial_delay

