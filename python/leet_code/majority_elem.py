# given an array of size n, find the majority element. The majoirty element is the element that appears more than n/2 times

# you may assume that the array is non-empty and the majority element always exist in the array
# ex.
# input: [3,2,3]
# outout: 3

# [2, 2, 1, 1, 1, 2, 2]
# 2

def find_majority(nums):
    seen_values = {}
    n = len(nums) // 2

    for num in nums:
        if seen_values.get(num):
            seen_values[num] += 1
            if seen_values[num] > n:
                return num
        else:
            seen_values[num] = 1

