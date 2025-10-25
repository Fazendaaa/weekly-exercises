#                   Find the Nth row in Pascal's Triangle
#
# Given a non-negative integer n, the task is to find the nth row of Pascal's
# Triangle.
#
# Note: The row index starts from 1.
#
# Examples:
#
#   Input: n = 4
#   Output: 1 3 3 1
#
# Explanation: The elements in the 4th row are 1 3 3 1 as shown in Pascal Triangle.
#
# Nth-row-in-Pascals-Triangle
#
#   Input: n = 1
#   Output: 1
#
# Explanation: The elements in the 1th row is 1 as shown in Pascal Triangle.
#
# Reference:
#   - https://www.geeksforgeeks.org/dsa/find-the-nth-row-in-pascals-triangle/
#


def pascalsTriangle(
    rowIndex: int,
) -> list[int]:
    """
    This function calculates the elements of the nth row in Pascal's Triangle.

    Args:
        row (int): The row number for which the elements need to be calculated.

    Returns:
        list: A list containing the elements of the nth row in Pascal's Triangle.
    """
    row = [1]

    for _ in range(1, rowIndex):
        row = (
            [1]
            + [row[column] + row[column + 1] for column in range(len(row) - 1)]
            + [1]
        )

    return row
