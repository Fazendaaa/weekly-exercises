#         Did you really manage to win? Row Winner Checker (retired)
#
# You need to implement a function that checks if there is a winning line
# (horizontal) in the Tic-Tac-Toe (3x3) field.
#
# The field is represented as a one-dimensional array of 9 elements, where:
#
#   'X' -- cross
#   'O' -- zero (letter 'O') '.' -- empty cell.
#
# Your task is to determine if there is at least one filled line (3 identical
# characters in a row in one of the three horizontal lines).
#
#   Examples:
#
#   Field:
#
#   X | X | X
#   O | O | .
#   . | . | .
#
#   isRowWinner({'X', 'X', 'X', 'O', 'O', '.', '.', '.', '.'}) → true
#
#   Field:
#
#   X | O | X
#   O | O | O
#   X | . | X
#
#   isRowWinner({'X', 'O', 'X', 'O', 'O', 'O', 'X', '.', 'X'}) → true
#
#   Field:
#
#   X | O | .
#   . | X | O
#   . | . | X
#
#   isRowWinner({'X', 'O', '.', '.', 'X', 'O', '.', '.', 'X'}) → false // There is no filled line
#
# Note:
#
# If the field has both 'X' and' O ' in the winning rows — this is an invalid
# field, the function should return false.
#
# If there are no winning lines at all, return false.
#
# Reference:
#   - https://www.codewars.com/kata/67fbd1c105b5721c8011d44b
#

from concurrent.futures import ThreadPoolExecutor, as_completed


def checkRow(row: list[str]) -> bool:
    """
    Checks if there is a winning line (horizontal) in the Tic-Tac-Toe field.

    Returns:
        bool: Whether or not there is at least one filled line.
    """

    pivot = row[0]

    return all(["." != cell and pivot == cell for cell in row[1:]])


def isRowWinner(board: list[list[str]]) -> bool:
    """
    Checks if there is a winning line (horizontal) in the Tic-Tac-Toe field.

    Args:
        board (list[list[str]]): A one-dimensional array of n elements representing the Tic-Tac-Toe field.

    Returns:
        bool: Whether or not there is at least one filled line.
    """
    nRows = len(board)

    if any([nRows != len(row) for row in board]):
        raise ValueError("The board is invalid with current input.")

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(checkRow, row) for row in board]
        result = [future.result() for future in as_completed(futures)]

        return result.count(True) == 1

    return False
