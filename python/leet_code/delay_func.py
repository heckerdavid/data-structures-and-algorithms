# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

import time

def delay(f, wait_period):
    time1 = time.time_ns()
    time2 = time.time_ns()

    while (time2 - time1) * 1000000 < wait_period: #ms
        time2 = time.time_ns()

    f()
    return None
