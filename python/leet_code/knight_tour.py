
def solution(x, y, grid):
    '''this requires the grid to be pre-made, and doesnt work for 5x5(not sure why)'''

    if no_available_moves(grid):
        return True

    available_moves = find_available_moves(x, y, grid)
    for move in available_moves:
        grid[move[0]][move[1]] = 1

        if solution(move[0], move[1], grid):
            return True
        grid[move[0]][move[1]] = 0

    return False


def no_available_moves(grid):
    for row in grid:
        for num in row:
            if num == 0:
                return False

    return True


def find_available_moves(x, y, grid):
    max_length = len(grid) - 1
    possible = [(2, 1), (2, -1), (1, 2), (1, -2), (-2, 1), (-2, -1), (-1, 2), (-1, -2)]
    available = []

    for move in possible:
        if (
            0 <= x + move[0] <= max_length
            and 0 <= y + move[1] <= max_length
            and grid[x + move[0]][y + move[1]] == 0
        ):
            available.append((x + move[0], y + move[1]))

    return available
