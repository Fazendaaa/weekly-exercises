#                               Introduction
#
# You plan to build a tree house in the woods near your house so that you can
# watch the sun rise and set.
#
# You've obtained data from a local survey company that show the height of every
# tree in each rectangular section of the map. You need to analyze each grid on
# the map to find good trees for your tree house.
#
# A good tree is both:
#
#   - taller than every tree to the east and west, so that you have the best
#     possible view of the sunrises and sunsets.
#   - shorter than every tree to the north and south, to minimize the amount of
#     tree climbing.
#
#   Instructions
#
# Your task is to find the potential trees where you could build your tree
# house.
#
# The data company provides the data as grids that show the heights of the
# trees. The rows of the grid represent the east-west direction, and the columns
# represent the north-south direction.
#
# An acceptable tree will be the largest in its row, while being the smallest in
# its column.
#
# A grid might not have any good trees at all. Or it might have one, or even
# several.
#
# Here is a grid that has exactly one candidate tree.
#
#                   ↓
#                   1  2  3  4
#                 |-----------
#               1 | 9  8  7  8
#             → 2 |[5] 3  2  4
#               3 | 6  6  7  1
#
#   - Row 2 has values 5, 3, 2, and 4. The largest value is 5.
#   - Column 1 has values 9, 5, and 6. The smallest value is 5.
#   - So the point at [2, 1] (row: 2, column: 1) is a great spot for a tree
#     house.
#
#   Exception messages
#
# Sometimes it is necessary to raise an exception. When you do this, you should
# always include a meaningful error message to indicate what the source of the
# error is. This makes your code more readable and helps significantly with
# debugging. For situations where you know that the error source will be a
# certain type, you can choose to raise one of the built in error types, but
# should still include a meaningful message.
#
# This particular exercise requires that you use the raise statement to "throw"
# a ValueError if the matrix is irregular. The tests will only pass if you both
# raise the exception and include a message with it.
#
# To raise a ValueError with a message, write the message as an argument to the
# exception type:
#
# # if the matrix is irregular
# raise ValueError("irregular matrix")
#
# Reference:
#   - https://exercism.org/tracks/python/exercises/saddle-points
#   - https://users.csc.calpoly.edu/~jdalbey/103/Projects/ProgrammingPractice.html
#


def saddlePoints(points: list[list[int]]) -> list[list[int]]:
    """
    Finds the saddle points in a given matrix.

    Args:
        points (list[list[int]]): A 2D list representing the matrix.

    Returns:
        list[list[int]]: A list of lists containing the coordinates of the saddle points.

    Raises:
        ValueError: If the input matrix is irregular (i.e., not rectangular).
    """

    if not points or len(set([len(row) for row in points])) > 1:
        raise ValueError("irregular matrix")

    rowMax = [max(row) for row in points]
    colMin = [min(col) for col in zip(*points)]

    return [
        [i + 1, j + 1]
        for i, row in enumerate(points)
        for j, val in enumerate(row)
        if val == rowMax[i] == colMin[j]
    ]
