# given a sorted array of ints ARR and an int TARGET find the index of the first and last position of TARGET in ARR. If target cannot be found return [-1, -1]

def index_range(num_list, target):
    low = -1
    high = -1

    index = find_index(num_list, target)

    while num_list[index] == target:
        low = index
        index -= 1

    index += 1
    while num_list[index] == target:
        high = index
        index += 1


    return [low, high]

def find_index(num_list, target):
    start = 0
    end = len(num_list) - 1

    while start <= end:
        mid = (start + end) // 2
        if num_list[mid] == target:
            return mid
        elif num_list[mid] < target:
            start = mid + 1
            continue
        elif num_list[mid] > target:
            end = mid - 1
            continue

    return -1

