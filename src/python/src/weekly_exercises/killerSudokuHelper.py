#                             Instructions
#
# A friend of yours is learning how to solve Killer Sudokus (rules below) but
# struggling to figure out which digits can go in a cage. They ask you to help
# them out by writing a small program that lists all valid combinations for a
# given cage, and any constraints that affect the cage.
#
# To make the output of your program easy to read, the combinations it returns
# must be sorted.
#
#   Killer Sudoku Rules
#
#   - Standard Sudoku rules apply --
#     https://masteringsudoku.com/sudoku-rules-beginners/.
#   - The digits in a cage, usually marked by a dotted line, add up to the small
#     number given in the corner of the cage.
#   - A digit may only occur once in a cage.
#   - For a more detailed explanation, check out this --
#     https://masteringsudoku.com/killer-sudoku/ -- guide.
#
#   Example 1: Cage with only 1 possible combination
#
# In a 3-digit cage with a sum of 7, there is only one valid combination: 124.
#
#   - 1 + 2 + 4 = 7
#   - Any other combination that adds up to 7, e.g. 232, would violate the rule
#     of not repeating digits within a cage.
#
#     +-------+-------+-------+
#     | . 1 . | . . . | . . . |
#     | . 2 . | . . . | . . . |
#     | . 5 . | . . 2 | 3 . . |
#     +-------+-------+-------+
#     | . . . | . 1 . | 2 . . |
#     | . . . | . 2 . | . . . |
#     | . . . | . 4 . | . . . |
#     +-------+-------+-------+
#     | . . . | . . . | . . . |
#     | . . . | . . . | . . . |
#     | . . . | . . . | . . . |
#     +-------+-------+-------+
#
#   Example 2: Cage with several combinations
#
# In a 2-digit cage with a sum 10, there are 4 possible combinations:
#
#   - 19
#   - 28
#   - 37
#   - 46
#
#     +-------+-------+-------+
#     | . . . | . 1 . | . . . |
#     | . . . | . 9 . | . . . |
#     | . . . | . 2 . | . . . |
#     +-------+-------+-------+
#     | . . . | . 8 . | . . . |
#     | . . . | . 3 . | . . . |
#     | . . . | . 7 . | . . . |
#     +-------+-------+-------+
#     | . . . | . 4 . | . . . |
#     | . . . | . 6 . | . . . |
#     | . . . | . . . | . . . |
#     +-------+-------+-------+
#
#   Example 3: Cage with several combinations that is restricted
#
# In a 2-digit cage with a sum 10, where the column already contains a 1 and a
# 4, there are 2 possible combinations:
#
#   - 28
#   - 37
#
# 19 and 46 are not possible due to the 1 and 4 in the column according to
# standard Sudoku rules.
#
#     +-------+-------+-------+
#     | . . . | . 4 . | . . . |
#     | . . . | . . . | . . . |
#     | . . . | . 1 . | . . . |
#     +-------+-------+-------+
#     | . . . | . 2 . | . . . |
#     | . . . | . 8 . | . . . |
#     | . . . | . 3 . | . . . |
#     +-------+-------+-------+
#     | . . . | . 7 . | . . . |
#     | . . . | . 1 . | . . . |
#     | . . . | . 9 . | . . . |
#     +-------+-------+-------+
#
#   Trying it yourself
#
# If you want to give an approachable Killer Sudoku a go, you can try out this
# -- https://app.crackingthecryptic.com/sudoku/HqTBn3Pr6R -- puzzle by Clover,
# featured by Mark Goodliffe on Cracking The Cryptic on the 21st of June 2021 --
# https://youtu.be/c_NjEbFEeW0?t=1180.
#
# You can also find Killer Sudokus in varying difficulty in numerous newspapers,
# as well as Sudoku apps, books and websites.
#
# Reference:
#   - https://exercism.org/tracks/r/exercises/killer-sudoku-helper
#   - https://github.com/exercism/julia/pull/413
#

from itertools import combinations


def killerSudokuHelper(
    cage_sum: int, cage_size: int, constraints: set[int] = None
) -> list[tuple[int]]:
    """
    This function takes in a cage, its sum, and the size of the Sudoku grid.
    It returns a list of all valid combinations for the cage, given the sum and size constraints.
    """

    if constraints is None:
        constraints = set()

    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    valid_combinations: list[tuple[int]] = []

    for combo in combinations(digits, cage_size):
        if sum(combo) != cage_sum:
            continue

        if len(set(combo)) != cage_size:
            continue

        if constraints and any(d in constraints for d in combo):
            continue

        valid_combinations.append(combo)

    valid_combinations.sort()

    return valid_combinations
