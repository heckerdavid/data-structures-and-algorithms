# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

def two_sum(num_list, target):
    seen = set()

    for num in num_list:
        needed = target - num
        if needed in seen:
            return True
        seen.add(num)

    return False
