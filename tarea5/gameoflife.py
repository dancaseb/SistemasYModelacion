import numpy as np

grid_row = 10
grid_col = 10
starting_position = [(4, 4), (5,5), (6,5), (6,4), (6,3)]
iterations = 4

grid = np.zeros((grid_row, grid_col), dtype=int)
# initialize the grid with the starting position
for pos in starting_position:
    grid[pos] = 1

print(grid)
grid_new = grid.copy()
for iter in range(iterations):
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            neighbour_cells_sum = 0
            if row == 0 and col == 0:  # left top corner
                neighbour_cells_sum = np.sum(
                    grid[row:row+2, col:col+2]) - grid[row, col]
            elif row == 0 and col == grid.shape[1] - 1:  # right top corner
                neighbour_cells_sum = np.sum(
                    grid[row:row+2, col-1:col+1]) - grid[row, col]
            elif row == grid.shape[0] - 1 and col == 0:
                neighbour_cells_sum = np.sum(
                    grid[row-1:row+1, col:col+2]) - grid[row, col]
            elif row == grid.shape[0] - 1 and col == grid.shape[1] - 1:
                neighbour_cells_sum = np.sum(
                    grid[row-1:row+1, col-1:col+1]) - grid[row, col]
            elif row == 0:  # top edge no corners
                neighbour_cells_sum = np.sum(
                    grid[row:row+2, col-1:col+2]) - grid[row, col]
            elif row == grid.shape[0] - 1:
                neighbour_cells_sum = np.sum(
                    grid[row-1:row+1, col-1:col+2]) - grid[row, col]
            elif col == 0:
                neighbour_cells_sum = np.sum(
                    grid[row-1:row+2, col:col+2]) - grid[row, col]
            elif col == grid.shape[1] - 1:
                neighbour_cells_sum = np.sum(
                    grid[row-1:row+2, col-1:col+1]) - grid[row, col]
            else:
                neighbour_cells_sum = np.sum(
                    grid[row-1:row+2, col-1:col+2]) - grid[row, col]

            if grid[row, col] == 1:
                if neighbour_cells_sum < 2 or neighbour_cells_sum > 3:
                    grid_new[row, col] = 0
                elif neighbour_cells_sum == 2 or neighbour_cells_sum == 3:
                    grid_new[row, col] = 1
            else:
                if neighbour_cells_sum == 3:
                    grid_new[row, col] = 1
    print(grid_new)
    grid = grid_new.copy()
    grid_new = np.zeros((grid_row, grid_col), dtype=int)
    
