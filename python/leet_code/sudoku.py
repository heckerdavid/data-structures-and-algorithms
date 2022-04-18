def check_horizontal(x, y, grid, value):
  for i in range(9):
    if grid[x][i] == value:
      return False
  return True

def check_vertical(x, y, grid, value):
  for i in range(9):
    if grid[i][y] == value:
      return False
  return True

def check_box(x, y, grid, value):
  x_offset = 0
  y_offset = 0
  if x >= 3 and x < 6:
    x_offset = 3
  elif x >= 6:
    x_offset = 6

  if y >= 3 and y < 6:
    y_offset = 3
  elif y >= 6:
   y_offset = 6

  for i in range(3):
    for j in range(3):
      if grid[i + x_offset][j + y_offset] == value:
        return False

  return True

def find_next_empty(grid):
  for i in range(9):
    for j in range(9):
      if grid[i][j] == 0:
        return [i, j]

  return False

def solve_sudoku(grid):
  if not find_next_empty(grid):
    return True

  next_empty_x, next_empty_y = find_next_empty(grid)


  for i in range(1,10):
    if check_horizontal(next_empty_x, next_empty_y, grid, i) and check_vertical(next_empty_x, next_empty_y, grid,i) and check_box(next_empty_x, next_empty_y, grid,i):
      grid[next_empty_x][next_empty_y] = i
      if solve_sudoku(grid):
        return True

  grid[next_empty_x][next_empty_y] = 0
  return False
