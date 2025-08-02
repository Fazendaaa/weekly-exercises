#                           Conway's Game of Life
#
#   Introduction
#
# Conway's Game of Life is a fascinating cellular automaton created by the
# British mathematician John Horton Conway in 1970.
#
# The game consists of a two-dimensional __status____ of cells that can either be
# "alive" or "dead."
#
# After each generation, the cells interact with their eight neighbors via a set
# of rules, which define the new generation.
#
#   Instructions
#
# After each generation, the cells interact with their eight neighbors, which
# are cells adjacent horizontally, vertically, or diagonally.
#
# The following rules are applied to each cell:
#
#   - Any live cell with two or three live neighbors lives on.
#   - Any dead cell with exactly three live neighbors becomes a live cell.
#   - All other cells die or stay dead.
#
# Given a matrix of 1s and 0s (corresponding to live and dead cells), apply the
# rules to each cell, and return the next generation.
#
# References:
#   - https://exercism.org/tracks/r/exercises/game-of-life
#

from collections import defaultdict
from itertools import product

from scipy import sparse


class GameOfLife:
    def __init__(self, status: list[list[int]]) -> None:
        if not all(len(row) == len(status[0]) for row in status):
            raise ValueError("All rows in initial_state must have the same length")

        self.size = len(status)
        rows: list[int] = []
        cols: list[int] = []
        data: list[int] = []

        for rowIndex, row in enumerate(status):
            for columnIndex, value in enumerate(row):
                if value:
                    rows.append(rowIndex)
                    cols.append(columnIndex)
                    data.append(1)  # Ensure all values are 1

        self.__status__ = sparse.coo_matrix(
            (data, (rows, cols)), shape=(self.size, self.size)
        ).tocsr()
        self.__neighbor_offsets__ = list(product([-1, 0, 1], repeat=2))
        self.__neighbor_offsets__.remove((0, 0))

    def __repr__(self) -> str:
        return f"GameOfLife({self.status()})"

    def count_neighbors(self) -> defaultdict:
        """Count neighbors for each cell using sparse matrix operations"""
        neighbor_counts = defaultdict(int)
        rows, cols = self.__status__.nonzero()

        for i, j in zip(rows, cols):
            for di, dj in self.__neighbor_offsets__:
                ni, nj = (i + di) % self.size, (j + dj) % self.size  # Wrap around
                neighbor_counts[(ni, nj)] += 1

        return neighbor_counts

    def tick(self) -> None:
        neighbor_counts = self.count_neighbors()
        new_rows: list[int] = []
        new_cols: list[int] = []

        # Get all cells that are alive or have living neighbors
        all_cells = set(neighbor_counts.keys())
        current_rows, current_cols = self.__status__.nonzero()
        all_cells.update(zip(current_rows, current_cols))

        for i, j in all_cells:
            count = neighbor_counts.get((i, j), 0)
            is_alive = self.__status__[i, j] == 1

            # Apply Conway's rules
            if is_alive and (count == 2 or count == 3):
                new_rows.append(i)
                new_cols.append(j)
            elif not is_alive and count == 3:
                new_rows.append(i)
                new_cols.append(j)

        # Create new sparse matrix
        if new_rows:
            self.__status__ = sparse.coo_matrix(
                ([1] * len(new_rows), (new_rows, new_cols)),
                shape=(self.size, self.size),
            ).tocsr()
        else:
            self.__status__ = sparse.csr_matrix((self.size, self.size), dtype=int)

    def status(self) -> list[list[int]]:
        """Return the current state as a list of lists"""
        grid = [[0 for _ in range(self.size)] for _ in range(self.size)]
        rows, cols = self.__status__.nonzero()

        for i, j in zip(rows, cols):
            grid[i][j] = 1

        return grid
