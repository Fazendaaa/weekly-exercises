#                           Instructions
#
# Given an alphametics puzzle, find the correct solution.
#
# Alphametics is a puzzle where letters in words are replaced with numbers.
#
# For example SEND + MORE = MONEY:
#
#          S E N D
#          M O R E +
#        -----------
#        M O N E Y
#
# Replacing these with valid numbers gives:
#
#          9 5 6 7
#          1 0 8 5 +
#        -----------
#        1 0 6 5 2
#
# This is correct because every letter is replaced by a different number and the
# words, translated into numbers, then make a valid sum.
#
# Each letter must represent a different digit, and the leading digit of a
# multi-digit number must not be zero.
#
# Reference:
# - https://exercism.org/tracks/python/exercises/alphametics
#

from itertools import permutations


def alphametics(puzzle: str) -> dict[str, int]:
    """
    Solves an alphametics puzzle by finding the correct digit assignments for
    each letter.

    Args:
        word (str): The alphametics puzzle as a string.

    Returns:
        dict[str, int]: A dictionary mapping each letter to its assigned digit.
    """
    equation = puzzle.replace(" ", "").split("==")
    left = equation[0].split("+")
    right = equation[1]
    letters = "".join(set(puzzle.replace(" ", "").replace("+", "").replace("=", "")))
    first_letters = "".join(set(word[0] for word in left + [right]))
    digits = range(10)

    for perm in permutations(digits, len(letters)):
        solution = dict(zip(letters, perm))
        nums_left: list[int] = []
        num_right = 0

        if any(0 == solution[letter] for letter in first_letters):
            continue

        for word in left:
            num = 0

            for c in word:
                num = num * 10 + solution[c]

            nums_left.append(num)

        for c in right:
            num_right = num_right * 10 + solution[c]

        if num_right == sum(nums_left):
            return solution

    return {}
