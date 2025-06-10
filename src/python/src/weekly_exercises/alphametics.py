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
    # Split the puzzle into words and the result
    words, result = puzzle.replace(" ", "").split("==")
    words = words.split("+")

    # Get the unique letters in the puzzle
    letters = set("".join(words) + result)

    # Generate all possible digit assignments for the letters
    for perm in permutations(range(10), len(letters)):
        # Skip permutations that start with 0
        if 0 == perm[letters.index(min(letters))]:
            continue

        # Create a dictionary mapping letters to digits
        d = dict(zip(letters, perm))

        # Check if the sum of the word values equals the result value
        if sum(int("".join(str(d[c]) for c in word)) for word in words) == int(
            "".join(str(d[c]) for c in result)
        ):
            return d

    return {}
