from copy import deepcopy


expand_size = 0


def rotate(grid):
    grid_copy = deepcopy(grid)
    x_width = len(grid[0])

    # print("x_width: ", x_width)

    y_width = len(grid)
    # print("x_width: ", y_width)

    # start swapping grid points about
    for y in range(y_width):
        for x in range(x_width):
            grid_element = grid[y][x]
            # print(
            #     f"place {grid_element} from ({y}, {x}) => ({x}, {x_width - y - 1})"
            # )
            grid_copy[x][x_width - y - 1] = grid_element
    return grid_copy

def expand(grid):
    x_width = len(grid[0])
    # print("x_width: ", x_width)

    y_width = len(grid)
    # print("x_width: ", y_width)

    global expand_size
    expand_size = x_width - y_width
    print(f"expand_size: {expand_size}")
    # For rectangular grids, need to extend at least one dimension
    if expand_size < 0:
        # horizontal rectangle, so extend in x-direction
        for y in range(y_width):
            for x_add in range(y_width - x_width):
                grid[y].append(".")
    elif expand_size > 0:
        # vertical rectangle, so extend in y-direction
        for x in range(x_width):
            for y_add in range(x_width - y_width):
                grid[x].append(".")
    else:
        # no rotation for squares
        pass
    #print("grid after extension: ", grid)
    return grid

def trim(grid):
    # remove extra rows or columns
    result = []
    if expand_size < 0:
        # trim off bottom
        keep_rows = len(grid) + expand_size - 1
        #print(f"keep_rows: {keep_rows}")
        result = [row[:] for ind, row in enumerate(grid) if ind <= keep_rows]
        #print("result", result)
    elif expand_size > 0:
        # trim off left
        for x in range(x_width):
            for y_add in range(x_width - y_width):
                grid[x].append(".")
    else:
        # no rotation for squares
        pass
    return result


if __name__ == "__main__":

    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]


    print(trim(rotate(expand(grid))))
