import numpy as np
import matplotlib.pyplot as plt


# def update_image(ax, grid):
#     ax.imshow(grid, cmap='binary')
#     ax.set_xticks(np.arange(grid.shape[1] + 1) - 0.5, minor=True)
#     ax.set_yticks(np.arange(grid.shape[0] + 1) - 0.5, minor=True)
#     ax.grid(which="minor", color="black", linestyle='-', linewidth=1)


# grid_row = 10
# grid_col = 10
# starting_position = [(4, 4), (5, 5), (6, 5), (6, 4), (6, 3)]
# iterations = 0

# grid = np.zeros((grid_row, grid_col), dtype=int)
# # initialize the grid with the starting position
# for pos in starting_position:
#     grid[pos] = 1


# fig, ax = plt.subplots()
# update_image(ax, grid)
# plt.show()


# grid_new = grid.copy()
# for iter in range(iterations):
#     for row in range(grid.shape[0]):
#         for col in range(grid.shape[1]):
#             neighbour_cells_sum = 0
#             if row == 0 and col == 0:  # left top corner
#                 neighbour_cells_sum = np.sum(
#                     grid[row:row+2, col:col+2]) - grid[row, col]
#             elif row == 0 and col == grid.shape[1] - 1:  # right top corner
#                 neighbour_cells_sum = np.sum(
#                     grid[row:row+2, col-1:col+1]) - grid[row, col]
#             elif row == grid.shape[0] - 1 and col == 0:
#                 neighbour_cells_sum = np.sum(
#                     grid[row-1:row+1, col:col+2]) - grid[row, col]
#             elif row == grid.shape[0] - 1 and col == grid.shape[1] - 1:
#                 neighbour_cells_sum = np.sum(
#                     grid[row-1:row+1, col-1:col+1]) - grid[row, col]
#             elif row == 0:  # top edge no corners
#                 neighbour_cells_sum = np.sum(
#                     grid[row:row+2, col-1:col+2]) - grid[row, col]
#             elif row == grid.shape[0] - 1:
#                 neighbour_cells_sum = np.sum(
#                     grid[row-1:row+1, col-1:col+2]) - grid[row, col]
#             elif col == 0:
#                 neighbour_cells_sum = np.sum(
#                     grid[row-1:row+2, col:col+2]) - grid[row, col]
#             elif col == grid.shape[1] - 1:
#                 neighbour_cells_sum = np.sum(
#                     grid[row-1:row+2, col-1:col+1]) - grid[row, col]
#             else:
#                 neighbour_cells_sum = np.sum(
#                     grid[row-1:row+2, col-1:col+2]) - grid[row, col]

#             if grid[row, col] == 1:
#                 if neighbour_cells_sum < 2 or neighbour_cells_sum > 3:
#                     grid_new[row, col] = 0
#                 elif neighbour_cells_sum == 2 or neighbour_cells_sum == 3:
#                     grid_new[row, col] = 1
#             else:
#                 if neighbour_cells_sum == 3:
#                     grid_new[row, col] = 1
#     grid = grid_new.copy()
#     plt.imshow(grid, cmap='binary')
#     plt.show()
#     grid_new = np.zeros((grid_row, grid_col), dtype=int)


class GameOfLife:
    def __init__(self, grid_row, grid_col, starting_position, iterations):
        self.grid_row = grid_row
        self.grid_col = grid_col
        self.starting_position = starting_position
        self.iterations = iterations
        self.grid = self._init_grid(grid_row, grid_col, starting_position)
        # self.fig, self.ax = plt.subplots()

    def _init_grid(self, grid_row, grid_col, starting_position):
        grid = np.zeros((grid_row, grid_col), dtype=int)
        # initialize the grid with the starting position
        for pos in starting_position:
            grid[pos] = 1
        return grid

    def _update_image(self):
        fig, ax = plt.subplots()
        ax.imshow(self.grid, cmap='binary')
        ax.set_xticks(np.arange(self.grid.shape[1] + 1) - 0.5, minor=True)
        ax.set_yticks(np.arange(self.grid.shape[0] + 1) - 0.5, minor=True)
        ax.grid(which="minor", color="black", linestyle='-', linewidth=1)
        plt.show()

    def _run_iteration(self):
        grid_new = self.grid.copy()
        for row in range(self.grid.shape[0]):
            for col in range(self.grid.shape[1]):
                neighbour_cells_sum = 0
                if row == 0 and col == 0:  # left top corner
                    neighbour_cells_sum = np.sum(
                        self.grid[row:row+2, col:col+2]) - self.grid[row, col]
                elif row == 0 and col == self.grid.shape[1] - 1:  # right top corner
                    neighbour_cells_sum = np.sum(
                        self.grid[row:row+2, col-1:col+1]) - self.grid[row, col]
                elif row == self.grid.shape[0] - 1 and col == 0:
                    neighbour_cells_sum = np.sum(
                        self.grid[row-1:row+1, col:col+2]) - self.grid[row, col]
                elif row == self.grid.shape[0] - 1 and col == self.grid.shape[1] - 1:
                    neighbour_cells_sum = np.sum(
                        self.grid[row-1:row+1, col-1:col+1]) - self.grid[row, col]
                elif row == 0:  # top edge no corners
                    neighbour_cells_sum = np.sum(
                        self.grid[row:row+2, col-1:col+2]) - self.grid[row, col]
                elif row == self.grid.shape[0] - 1:
                    neighbour_cells_sum = np.sum(
                        self.grid[row-1:row+1, col-1:col+2]) - self.grid[row, col]
                elif col == 0:
                    neighbour_cells_sum = np.sum(
                        self.grid[row-1:row+2, col:col+2]) - self.grid[row, col]
                elif col == self.grid.shape[1] - 1:
                    neighbour_cells_sum = np.sum(
                        self.grid[row-1:row+2, col-1:col+1]) - self.grid[row, col]
                else:
                    neighbour_cells_sum = np.sum(
                        self.grid[row-1:row+2, col-1:col+2]) - self.grid[row, col]

                if self.grid[row, col] == 1:
                    if neighbour_cells_sum < 2 or neighbour_cells_sum > 3:
                        grid_new[row, col] = 0
                    elif neighbour_cells_sum == 2 or neighbour_cells_sum == 3:
                        grid_new[row, col] = 1
                else:
                    if neighbour_cells_sum == 3:
                        grid_new[row, col] = 1
        return grid_new
    
    def run(self):
        self._update_image()
        for iter in range(self.iterations):
            self.grid = self._run_iteration()
            self._update_image()



simulation = GameOfLife(10, 10, [(4, 4), (5, 5), (6, 5), (6, 4), (6, 3)], 5)
simulation.run()