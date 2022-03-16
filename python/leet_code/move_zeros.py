# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.



# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]

def shift_zeros(nums_list):
    left = 0
    right = 1

    while right <= len(nums_list) - 1:

        if nums_list[left] == 0:
            while nums_list[right] == 0 and right <= len(nums_list) - 2:
                right +=1
            nums_list[left], nums_list[right] = nums_list[right], nums_list[left]
            left +=1
            right +=1
        else:
            left += 1
            right += 1


    return nums_list
