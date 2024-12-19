import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class GameOfLife:
    def __init__(self, grid_row, grid_col, starting_position, iterations):
        self.grid_row = grid_row
        self.grid_col = grid_col
        self.starting_position = starting_position
        self.iterations = iterations
        self.grid = self._init_grid(grid_row, grid_col, starting_position)

    def _init_grid(self, grid_row, grid_col, starting_position):
        """
        Initialize the grid with the starting position
        """
        grid = np.zeros((grid_row, grid_col), dtype=int)
        for pos in starting_position:
            grid[pos] = 1
        return grid

    def _update_image(self, frame):
        """
        Function to update the image for each frame of the animation
        runs iteration and updates the image
        """
        self._run_iteration()
        self.im.set_array(self.grid)
        return [self.im]

    def _run_iteration(self):
        """
        One iteration of the game of life.

        Rules:
        1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
        2. Any live cell with two or three live neighbours lives on to the next generation.
        3. Any live cell with more than three live neighbours dies, as if by overpopulation.
        4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction

        """
        grid_new = self.grid.copy()
        for row in range(self.grid.shape[0]):
            for col in range(self.grid.shape[1]):
                neighbour_cells_sum = 0
                # sum the neighbour cells. The grid is finite, so we check edges
                if row == 0 and col == 0:  # left top corner
                    neighbour_cells_sum = np.sum(
                        self.grid[row:row+2, col:col+2]) - self.grid[row, col]
                # right top corner
                elif row == 0 and col == self.grid.shape[1] - 1:
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

                # apply the rules
                if self.grid[row, col] == 1:
                    if neighbour_cells_sum < 2 or neighbour_cells_sum > 3:
                        grid_new[row, col] = 0
                    elif neighbour_cells_sum == 2 or neighbour_cells_sum == 3:
                        grid_new[row, col] = 1
                else:
                    if neighbour_cells_sum == 3:
                        grid_new[row, col] = 1
        # update the grid for the animation
        self.grid = grid_new

    def animate(self):
        """
        This is our run function. Sets up the image and runs the animation
        _update_image is called to update the image for each frame
        """
        fig, ax = plt.subplots()
        self.im = ax.imshow(self.grid, cmap='binary')
        # sets where the grid lines will be
        ax.set_xticks(np.arange(self.grid.shape[1] + 1) - 0.5, minor=True)
        ax.set_yticks(np.arange(self.grid.shape[0] + 1) - 0.5, minor=True)
        ax.grid(which="minor", color="black", linestyle='-', linewidth=1)
        ax.set_aspect('equal')  # ensures each cell is a square
        ax.set_title("Game of Life")
        ani = animation.FuncAnimation(
            fig, self._update_image, frames=self.iterations, interval=700, blit=False, repeat=False)
        plt.show()


simulation = GameOfLife(18, 18, [(4, 4), (5, 5), (6, 5), (6, 4), (6, 3)], 50)
simulation.animate()
