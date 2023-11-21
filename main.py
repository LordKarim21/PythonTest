import random
import numpy as np
import matplotlib.pyplot as plt


class CityGrid:
    def __init__(self, n, m, randomly_coverage=0.3):
        self.randomly_coverage = randomly_coverage
        self.grid = np.zeros((n, m), dtype=int)
        self.path_array = None

    def calculate(self):
        random_replace = np.vectorize(lambda x: 1 if random.random() <= self.randomly_coverage else 0)
        self.grid = random_replace(self.grid)

    def place_tower(self, radius):
        self.grid = self._place_tower(self.grid, radius)

    def placement_towers(self, radius):
        self.grid = _placement_towers(self.grid, radius)

    def find_most_reliable_paths(self):
        self.path_array = self._find_most_reliable_paths(self.grid, )

    def visualize_path(self):
        if self.path_array is not None:
            plt.imshow(self.grid, cmap='Blues', interpolation='nearest', alpha=0.5)
            plt.imshow(self.path_array, cmap='Reds', interpolation='nearest', alpha=0.7)
            plt.show()
        else:
            self.visualize(self.grid)

    @staticmethod
    def visualize(grid):
        plt.imshow(grid, cmap='gray', interpolation='nearest')
        plt.show()

    @staticmethod
    def _place_tower(grid, radius):
        row, col = grid.shape
        row_min = max(0, row - radius)
        row_max = min(self.n, row + radius+1)
        col_min = max(0, col - radius)
        col_max = min(self.m, col + radius+1)
        grid[row_min:row_max, col_min:col_max] = 2
        return grid

    @staticmethod
    def _placement_towers(grid, radius):
        row, col = grid.shape
        max_coverage = 0
        optimal_row, optimal_col = 0, 0
        for i in range(1, row):
            for j in range(1, col):
                coverage = self._place_tower(grid, radius)
                coverage = np.sum(coverage)
                if current_coverage > max_coverage:
                    max_coverage = coverage
                    optimal_row, optimal_col = i, j
        return optimal_row, optimal_col

    @staticmethod
    def _find_most_reliable_paths_recursive(self, current_node, path, paths):
        rows, cols = self.grid.shape

        if current_node == rows * cols - 1:
            paths.append(path + [current_node])
            return

        row, col = divmod(current_node, cols)

        for i in range(cols):
            if self.grid[row][i] > 0:
                neighbor = i + row * cols
                if neighbor not in path:
                    self.find_most_reliable_paths_recursive(neighbor, path + [current_node], paths)

    @staticmethod
    def _find_most_reliable_paths(grid):
        paths = []
        for start_node in range(grid.size):
            self._find_most_reliable_paths_recursive(start_node, [], paths)
        return paths
