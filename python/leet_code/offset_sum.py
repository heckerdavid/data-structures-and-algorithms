# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

# Follow-up: Can you do this in O(N) time and constant space?

def non_adjacent_sum(nums_list):
    total = 0
    current_idx = 0
    last_idx = len(nums_list)-1

    while current_idx <= last_idx:
        next_idx = current_idx + 1
        option_1 = calculate_gains_losses(nums_list, current_idx)

        if next_idx <= last_idx:
            option_2 = calculate_gains_losses(nums_list, next_idx)
        else:
            option_2 = None

        if option_2 is None or option_1 >= option_2:
            total += nums_list[current_idx]
            current_idx = current_idx + 2
        elif option_2 > option_1:
            total += nums_list[current_idx + 1]
            current_idx = current_idx + 3

    return total

def calculate_gains_losses(list,index):
    net_gain = list[index]

    if index - 1 >= 0:
        net_gain -= list[index -1]
    if index + 1 < len(list):
        net_gain -= list[index + 1]

    return net_gain
