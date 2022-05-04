def list_zip(list, n):
    left = 0
    right = n
    new_list = []
    for i in range(n):
        new_list.append(list[left+i])
        new_list.append(list[right+i])

    return new_list
