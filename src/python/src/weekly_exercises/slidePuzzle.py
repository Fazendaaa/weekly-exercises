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

from copy import deepcopy

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
    dimension = (size**2) - 1
    newPuzzle = flatten(puzzle)
    queue: list[tuple[list[int], list[int]]] = [(newPuzzle, [])]
    visited = set()
    moves = {"up": -size, "down": size, "left": -1, "right": 1}

    def checkResult(state: list[int], path: list[int]) -> str:
        """
        Validates the solution path.

        Args:
            state (list[int]): the current state variation to solve the puzzle.
            path (list[int]): The sequence of moves to solve the puzzle.

        Returns:
            str: A string representing the sequence of moves to solve the puzzle.
        """
        directions = {-size: "u", size: "d", -1: "l", 1: "r"}
        ordered = [i for i in range(1, dimension)]
        variationA = ordered + [0]
        variationB = [0] + ordered

        return (
            ""
            if variationA != state or variationB != state
            else "".join([directions[moves[move]] for move in path])
        )

    # Perform a depth-first search to find the solution
    while queue:
        state, path = queue.pop(0)

        # Generate all possible moves from the current state
        for _, offset in moves.items():
            pivot = state.index(0)
            newIndex = pivot + offset

            if newIndex < 0 or newIndex > dimension:
                continue

            newState = deepcopy(state)  # state[:]
            newState[pivot], newState[newIndex] = (
                newState[newIndex],
                newState[pivot],
            )

            movements = tuple(newState)

            if movements in visited:
                continue

            new_path = path + [offset]
            result = checkResult(newState, new_path)

            if result:
                return result

            queue.append((newState, new_path))
            visited.add(movements)

    return ""
