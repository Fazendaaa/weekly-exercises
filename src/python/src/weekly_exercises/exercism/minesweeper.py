#                                 Introduction
#
# Minesweeper is a popular game where the user has to find the mines using
# numeric hints that indicate how many mines are directly adjacent
# (horizontally, vertically, diagonally) to a square.
#
#   Instructions
#
# Your task is to add the mine counts to empty squares in a completed
# Minesweeper board. The board itself is a rectangle composed of squares that
# are either empty (' ') or a mine ('*').
#
# For each empty square, count the number of mines adjacent to it (horizontally,
# vertically, diagonally). If the empty square has no adjacent mines, leave it
# empty. Otherwise replace it with the adjacent mines count.
#
# For example, you may receive a 5 x 4 board like this (empty spaces are
# represented here with the '·' character for display on screen):
#
#   ·*·*·
#   ··*··
#   ··*··
#   ·····
#
# Which your code should transform into this:
#
#   1*3*1
#   13*31
#   ·2*2·
#   ·111·
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
# a ValueError when the board() function receives malformed input. The tests
# will only pass if you both raise the exception and include a message with it.
#
# To raise a ValueError with a message, write the message as an argument to the
# exception type:
#
#   # when the board receives malformed input
#   raise ValueError("The board is invalid with current input.")
#
# Reference:
#   - https://exercism.org/tracks/python/exercises/minesweeper
#


from concurrent.futures import ThreadPoolExecutor, as_completed
from copy import deepcopy


def minesweeperRow(result: list[list[str]], nRows: int, outerIndex: int) -> None:
    """
    Checks given minesweeper row going cell by cell and then gives it value.

    Args:
        result (list[list[str]]): A two-dimensional array of n x m elements representing the Minesweeper board.
        nRows (int): the row size
        outerIndex (int): the row size

    Returns:
        None: replaces in-place the needed information at result
    """

    nCols = len(result[0])
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for innerIndex in range(nCols):
        if "*" != result[outerIndex][innerIndex]:
            count = 0

            for di, dj in directions:
                ni, nj = outerIndex + di, innerIndex + dj

                if 0 <= ni < nRows and 0 <= nj < nCols and result[ni][nj] == "*":
                    count += 1

            if count > 0:
                result[outerIndex][innerIndex] = str(count)


def minesweeper(board: list[list[str]]) -> list[list[str]]:
    """
    Adds the mine counts to empty squares in a completed Minesweeper board.

    Args:
        board (list[list[str]]): A two-dimensional array of n x m elements representing the Minesweeper board.

    Returns:
        list[list[str]]: The Minesweeper board with mine counts added to empty squares.

    Raises:
        ValueError: If the board is invalid with current input.
    """

    if not board or not all(
        [all([cell in ["·", "*"] for cell in row]) for row in board]
    ):
        raise ValueError("The board is invalid with current input.")

    result = deepcopy(board)
    nRows = len(result)

    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(minesweeperRow, result, nRows, outerIndex)
            for outerIndex in range(nRows)
        ]

        for future in as_completed(futures):
            future.result()

    return result
