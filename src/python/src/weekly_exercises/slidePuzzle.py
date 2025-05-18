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


def create_vertical_2d(rows: int, cols: int, diff: int) -> list[list[int]]:
    """
    Create a vertically ordered 2D list

    Args:

    Returns:

    """
    return [[i + rows * j + diff for j in range(cols)] for i in range(rows)]


def slidePuzzleNonOptimal(puzzle: list[list[int]], alternativeOrdering: bool) -> str:
    """
    Solves the slide puzzle game and returns the solution in the fewest moves possible.

    Args:
        puzzle (list[list[int]]): A 2D list representing the initial state of the puzzle.

    Returns:
        str: A string representing the sequence of moves to solve the puzzle.
    """
    size = len(puzzle)
    dimension = size**2
    newPuzzle = flatten(puzzle)
    queue: list[tuple[list[int], list[int]]] = [(newPuzzle, [])]
    visited: set[tuple[list[int]]] = set()
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
        horizontalA = ordered + [0]
        horizontalB = [0] + ordered
        verticalA = flatten(create_vertical_2d(size, size, 0))
        vertical = create_vertical_2d(size, size, 1)
        vertical[-1][-1] = 0
        verticalB = flatten(vertical)

        def check():
            if 0 == len(path):
                return "Already sorted"

            return "".join([directions[move] for move in path])

        if horizontalA == state:
            return check()
        if alternativeOrdering:
            if horizontalB == state or verticalA == state or verticalB == state:
                return check()

            horizontalA.reverse()
            horizontalB.reverse()
            verticalA.reverse()
            verticalB.reverse()

            if horizontalB == state or verticalA == state or verticalB == state:
                return check()

        return ""

    def checkHeuristic(
        variations: list[tuple[list[int], list[int]]],
    ) -> list[tuple[list[int], list[int]]]:
        """
        Sorts the variations based on the number of inversions.

        Args:
            variations (list[tuple[list[int], list[int]]]): A list of variations to be sorted.

        Returns:
            list[tuple[list[int], list[int]]]: A sorted list of variations based on the number of inversions.
        """

        def count_inversions(arr: list[tuple[list[int], list[int]]]) -> int:
            inversions = 0

            for i in range(len(arr)):
                for j in range(i + 1, len(arr)):
                    if arr[0][i] > arr[0][j]:
                        inversions += 1

            return inversions

        return sorted(variations, key=count_inversions)

    # Perform a depth-first search to find the solution
    while queue:
        variations: list[tuple[list[int], list[int]]] = []
        state, path = queue.pop(0)

        result = checkResult(state, path)

        if result:
            return result

        # Generate all possible moves from the current state
        for _, offset in moves.items():
            pivot = state.index(0)
            newIndex = pivot + offset

            if newIndex < 0 or newIndex > (dimension - 1):
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

            visited.add(movements)
            variations.append((newState, new_path))

        queue.extend(checkHeuristic(variations))

    return "No Solution Found"


def slidePuzzleOptimal(puzzle: list[list[int]]) -> str:
    """
    Solves the slide puzzle game and returns the solution in the fewest moves possible.

    Args:
        puzzle (list[list[int]]): A 2D list representing the initial state of the puzzle.

    Returns:
        str: A string representing the sequence of moves to solve the puzzle.
    """
    pass
