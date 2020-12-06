from functools import reduce

grid = []
for _ in range(20):
    grid_row = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_row)

horiz_prod = diag_prod = verti_prod = maximum = 0
for row_i in range(20):
    for col_i in range(20):
        if col_i < 17:
            horiz_prod = reduce(lambda x,y: x*y, grid[row_i][col_i:col_i+4])
        if row_i < 17:
            verti_prod = grid[row_i][col_i] * grid[row_i+1][col_i] * grid[row_i+2][col_i] * grid[row_i+3][col_i]
        if row_i < 17 and col_i < 17:
            l_r_diag_prod = grid[row_i][col_i] * grid[row_i+1][col_i+1] * grid[row_i+2][col_i+2] * grid[row_i+3][col_i+3]
            r_l_diag_prod = grid[row_i][19-col_i] * grid[row_i+1][18-col_i] * grid[row_i+2][17-col_i] * grid[row_i+3][16-col_i]
        maximum = max([verti_prod, horiz_prod, l_r_diag_prod, r_l_diag_prod, maximum])

print(maximum)


