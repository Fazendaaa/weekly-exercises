#                               15 puzzle solver
#
# Your task is to write a program that finds a solution in the fewest moves
# possible single moves to a random Fifteen Puzzle Game.
#
# For this task you will be using the following puzzle:
#
#   15 14  1  6
#    9 11  4 12
#    0 10  7  3
#   13  8  5  2
#
# Solution:
#
#    1  2  3  4
#    5  6  7  8
#    9 10 11 12
#   13 14 15  0
#
# The output must show the moves' directions, like so: left, left, left, down,
# right... and so on.
#
# There are two solutions, of fifty-two moves:
#
# rrrulddluuuldrurdddrullulurrrddldluurddlulurruldrdrd
# rrruldluuldrurdddluulurrrdlddruldluurddlulurruldrrdd
#
# see: Pretty Print of Optimal Solution
#
# Finding either one, or both is an acceptable result.
#
# Extra credit.
# Solve the following problem:
#
#   0 12  9 13
#  15 11 10 14
#   3  7  2  5
#   4  8  6  1
#
# Reference:
#   - https://rosettacode.org/wiki/15_puzzle_solver
#

from .utils import flatten


def slidePuzzle(puzzle: list[list[int]]) -> str:
    """
    Solves the slide puzzle game and returns the solution in the fewest moves possible.

    Args:
        puzzle (list[list[int]]): A 2D list representing the initial state of the puzzle.

    Returns:
        str: A string representing the sequence of moves to solve the puzzle.
    """
    size = len(puzzle)
    new_puzzle = flatten(puzzle)
    goal = [i for i in range(1, size**2)] + [0]

    # Define the possible moves and their corresponding directions
    moves = {"up": -4, "down": 4, "left": -1, "right": 1}

    # Define the directions for printing the solution
    directions = {-4: "up", 4: "down", -1: "left", 1: "right"}

    # Initialize the queue with the starting puzzle state and an empty list for the solution
    queue = [(new_puzzle, [])]

    # Initialize a set to keep track of visited states
    visited = set()

    # Perform a breadth-first search to find the solution
    while queue:
        state, path = queue.pop(0)

        if state == goal:
            return "".join([directions[moves[move]] for move in path])

        # Generate all possible moves from the current state
        for _, offset in moves.items():
            new_state = state[:]
            index = state.index(0)
            new_index = index + offset

            if new_index < 0 or new_index > 15:
                continue

            new_state[index], new_state[new_index] = (
                new_state[new_index],
                new_state[index],
            )

            if tuple(new_state) in visited:
                continue

            queue.append((new_state, path + [offset]))
            visited.add(tuple(new_state))
