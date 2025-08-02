import random
from collections import defaultdict
from itertools import product

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class PurePythonGameOfLife:
    def __init__(self, initial_state=None, size=50, density=0.2):
        """
        Initialize the Game of Life with either:
        - A 2D list (list of lists) as initial_state, or
        - Random state with given size and density

        Args:
            initial_state: 2D list of 0s and 1s representing the initial grid
            size: Used if initial_state is None (creates size x size grid)
            density: Used if initial_state is None (probability of cell being alive)
        """
        if initial_state is not None:
            # Validate and store the initial state
            if not all(len(row) == len(initial_state[0]) for row in initial_state):
                raise ValueError("All rows in initial_state must have the same length")

            self.size = len(initial_state)
            self.live_cells = set()

            for i, row in enumerate(initial_state):
                for j, val in enumerate(row):
                    if val:
                        self.live_cells.add((i, j))
        else:
            # Create random initial state
            self.size = size
            self.live_cells = set()

            for i in range(size):
                for j in range(size):
                    if random.random() < density:
                        self.live_cells.add((i, j))

        # All 8 possible neighbor offsets
        self.neighbor_offsets = list(product([-1, 0, 1], repeat=2))
        self.neighbor_offsets.remove((0, 0))  # Remove center cell

    def count_neighbors(self):
        """Count neighbors for each cell using a dictionary"""
        neighbor_counts = defaultdict(int)

        for i, j in self.live_cells:
            for di, dj in self.neighbor_offsets:
                ni, nj = (i + di) % self.size, (j + dj) % self.size  # Wrap around
                neighbor_counts[(ni, nj)] += 1

        return neighbor_counts

    def update(self):
        """Update the grid according to Game of Life rules"""
        neighbor_counts = self.count_neighbors()
        new_live_cells = set()

        # Check all cells that are alive or have living neighbors
        all_cells = self.live_cells.union(neighbor_counts.keys())

        for i, j in all_cells:
            count = neighbor_counts.get((i, j), 0)
            is_alive = (i, j) in self.live_cells

            # Apply Conway's rules
            if is_alive and (count == 2 or count == 3):
                new_live_cells.add((i, j))
            elif not is_alive and count == 3:
                new_live_cells.add((i, j))

        self.live_cells = new_live_cells

    def get_list_grid(self):
        """Return the current state as a Python list of lists"""
        grid = [[0 for _ in range(self.size)] for _ in range(self.size)]

        for i, j in self.live_cells:
            grid[i][j] = 1

        return grid

    def visualize(self, frames=100):
        """Visualize the game with animation"""
        fig, ax = plt.subplots(figsize=(8, 8))
        img = ax.imshow(self.get_list_grid(), cmap="binary", interpolation="nearest")

        def animate(i):
            self.update()
            img.set_array(self.get_list_grid())
            ax.set_title(f"Generation {i+1} | Alive: {len(self.live_cells)}")
            return (img,)

        ani = FuncAnimation(fig, animate, frames=frames, interval=200, blit=True)
        plt.show()
        return ani


# Example usage:

# Option 1: Initialize with a 2D list
glider = [[0, 1, 0], [0, 0, 1], [1, 1, 1]]

game = PurePythonGameOfLife(initial_state=glider)
print("Initial state:")
for row in game.get_list_grid():
    print(row)

# Run some generations
game.update()
print("\nAfter 1 generation:")
for row in game.get_list_grid():
    print(row)

# Option 2: Visualize a random game
random_game = PurePythonGameOfLife(size=30, density=0.2)
random_game.visualize(frames=50)
