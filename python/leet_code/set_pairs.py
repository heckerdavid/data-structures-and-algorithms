# This problem was asked by Google.

# The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

# For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

# You may also use a list or array to represent a set.


def subsets(nums, new_set=None):
    if new_set is None:
        new_set = [[]]

    for idx, num in enumerate(nums):
        new_set.append([num])

        pair_idx = idx + 1
        while pair_idx <= len(nums) - 1:
            new_set.append([num, nums[pair_idx]])
            pair_idx += 1

    if len(nums) > 2:
        new_set.append(nums)
    if len(nums) > 3:
        for i in range(3, len(nums)):
            left = 0
            right = i
            while right <= len(nums):
                new_set.append(nums[left:right])
                left +=1
                right +=1
    return new_set
