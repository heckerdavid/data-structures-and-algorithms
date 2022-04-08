# Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a function rand7() that returns an integer from 1 to 7 (inclusive).
import random

def rand5():
    nums = [1, 2, 3, 4, 5]

    return random.choice(nums)


def rand_7():
    while True:
        randnum = rand5() * (rand5() - 1) + rand5()
        if randnum <= 7:
            return randnum
