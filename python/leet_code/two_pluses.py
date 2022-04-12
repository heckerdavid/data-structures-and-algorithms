def two_pluses_area(grid):
    valid_pairs = [{'area': 1, "indexs": []}]
    for row_index, string in enumerate(grid):
        for col_index, letter in enumerate(string):
            if letter == "G" and valid_center(row_index, col_index, grid):
                list_all_possible_crosses = calc_max_area(row_index, col_index, grid)
                for item in list_all_possible_crosses:
                    valid_pairs.append({'area': item[0], "indexs":item[1]})

    valid_pairs.sort(key=lambda x : x["area"], reverse= True)

    return calculate_biggest(valid_pairs)


def calculate_biggest(list_of_crosses):
  if len(list_of_crosses)== 1:
      return list_of_crosses[0]['area']

  hightest_area = 0
  current_left = 0
  current_right = current_left + 1
  while current_left <= len(list_of_crosses)-1:
    if no_index_conflicts(list_of_crosses[current_left]['indexs'], list_of_crosses[current_right]['indexs']):
      hightest_area = max(list_of_crosses[current_left]['area'] * list_of_crosses[current_right]['area'], hightest_area)
    if current_right < len(list_of_crosses) - 1:
      current_right += 1
    elif current_left + 2 == len(list_of_crosses):
          break
    else:
        current_left += 1
        current_right = current_left + 1

  return hightest_area


def calc_max_area(row, col, grid):
    left = max_run(row, col, grid, "left")
    right = max_run(row, col, grid, "right")
    bottom = max_run(row, col, grid, "bottom")
    top = max_run(row, col, grid, "top")
    run_length = min(left, right, top, bottom)
    list_of_all_possible_crosses = []
    for i in range(0, run_length + 1):
        area = 1 + i * 4
        indexs = build_index_list(row, col, i)
        list_of_all_possible_crosses.append((area,indexs))

    return list_of_all_possible_crosses

def max_run(row, col, grid, direction):
    current_row = row
    current_col = col
    count = 0
    while current_col - 1 >= 0 and current_col + 1 < len(grid[0]) and current_row + 1 < len(grid) and current_row -1 >= 0 and grid[current_row][current_col] == 'G':
        if direction == 'left':
            current_col -= 1
        elif direction == 'right':
            current_col += 1
        elif direction == 'top':
            current_row += 1
        elif direction == 'bottom':
            current_row -= 1
        if grid[current_row][current_col] == 'G':
            count += 1

    return count

def build_index_list(row, col, run_length):
    index_list = []
    for i in range(1, run_length + 1):
        index_list.append((row, col + i))
        index_list.append((row, col - i))
        index_list.append((row + i, col))
        index_list.append((row - i, col))

    index_list.append((row, col))

    return index_list

def valid_center(row, col, grid):
    if row + 1 > len(grid)-1 or grid[row+1][col] != 'G':
        return False
    if row - 1 <0 or grid[row-1][col] != 'G':
        return False
    if col + 1 > len(grid[0])-1 or grid[row][col + 1] != 'G':
        return False
    if col - 1 < 0 or grid[row][col - 1] != 'G':
        return False

    return True

def no_index_conflicts(index_list1, index_list2):
    list1_as_dict = {}
    for point in index_list1:
        list1_as_dict[point] = True

    for point in index_list2:
        if list1_as_dict.get(point):
            return False

    return True
