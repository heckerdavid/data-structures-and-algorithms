def sort_diag(grid):

# GO ACROSS
    for index, num in enumerate(grid[0]):
        current_row = 0
        current_col = index
        current_nums = []
        index_list = []

        while current_row < len(grid) and current_col >= 0 :
            current_nums.append(grid[current_row][current_col])
            index_list.append((current_row, current_col))
            current_row += 1
            current_col -= 1

        current_nums.sort(reverse=True)

        for i, spot in enumerate(index_list):
            grid[spot[0]][spot[1]] = current_nums[i]




# GO DOWN
    for row_index, num_lst in enumerate(grid):
        current_row = row_index
        current_col = len(grid[0]) - 1
        current_nums = []
        index_list = []

        while current_row <= len(grid)-1 and current_col >= 0:
            current_nums.append(grid[current_row][current_col])
            index_list.append((current_row, current_col))
            current_row += 1
            current_col -= 1

        current_nums.sort(reverse=True)


        for i, spot in enumerate(index_list):
            grid[spot[0]][spot[1]] = current_nums[i]


    return grid
