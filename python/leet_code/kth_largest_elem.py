# Given an array of integers ARR and an int K, find the Kth largest element in the array
#  1 <= K <= |arr|



def kth_largest(num_list, k):
    sorted_nums = sorted(num_list)
    return sorted_nums[-k]
