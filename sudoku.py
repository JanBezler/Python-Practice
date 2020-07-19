
grid = [[5, 1, 0, 0, 0, 2, 0, 0, 9],
        [0, 6, 2, 0, 5, 0, 3, 0, 0],
        [9, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 4],
        [0, 4, 3, 0, 0, 0, 1, 6, 0],
        [8, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 9, 0, 7, 0, 6, 1, 0],
        [4, 0, 0, 9, 0, 0, 0, 7, 3], ]


def check(grid, x, y, n):
    length = len(grid)

    for i in range(length):

        if grid[i][x] == n or grid[y][i] == n:
            return False

    lensq = (length // 3)
    xsq = (x // lensq) * lensq
    ysq = (y // lensq) * lensq

    for i in range(lensq):
        for j in range(lensq):
            if grid[ysq+i][xsq+j] == n:
                return False

    return True


def solve(grid):
    for y in range(len(grid)):
        for x in range(len(grid)):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if check(grid, x, y, n):
                        grid[y][x] = n
                        solve(grid)
                        grid[y][x] = 0
                return grid
    for row in (grid):
        print(row)
    input("more?")


solve(grid)
