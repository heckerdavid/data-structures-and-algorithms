# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.
# You can assume that you can always reach the last index.

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

def min_jumps(nums):
    jump_count = 0
    current_idx= 0
    goal_idx = len(nums) - 1

    while current_idx < goal_idx:
        current_val = nums[current_idx]
        if current_idx + current_val >= goal_idx:
            jump_count += 1
            return jump_count

        highest_idx = 0
        highest_worth = 0
        for idx,val in enumerate(nums[current_idx+1:current_idx + current_val+1]):
            attempt = idx + val
            if attempt >= highest_worth:
                highest_idx = idx
                highest_worth = attempt
        current_idx = highest_idx + current_idx + 1
        jump_count += 1

    return jump_count
