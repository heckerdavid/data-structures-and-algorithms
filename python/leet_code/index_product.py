# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

def product_index(num_list):
    product_list = []

    for idx, num in enumerate(num_list):
        exclusive_list = num_list[:idx] + num_list[idx+1:]
        new_num = multiply_all(exclusive_list)
        product_list.append(new_num)

    return product_list

def multiply_all(num_list):
    total = 1
    for number in num_list:
        total *= number
    return total
