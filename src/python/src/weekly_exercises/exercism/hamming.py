# Hamming
#
# Introduction
#
# Your body is made up of cells that contain DNA. Those cells regularly wear out
# and need replacing, which they achieve by dividing into daughter cells. In
# fact, the average human body experiences about 10 quadrillion cell divisions
# in a lifetime!
#
# When cells divide, their DNA replicates too. Sometimes during this process
# mistakes happen and single pieces of DNA get encoded with the incorrect
# information. If we compare two strands of DNA and count the differences
# between them, we can see how many mistakes occurred. This is known as the
# "Hamming distance".
#
# The Hamming distance is useful in many areas of science, not just biology, so
# it's a nice phrase to be familiar with :)
#
# Instructions
#
# Calculate the Hamming distance between two DNA strands.
#
# We read DNA using the letters C, A, G and T. Two strands might look like this:
#
# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT
# ^ ^ ^  ^ ^    ^^
#
# They have 7 differences, and therefore the Hamming distance is 7.
#
# Implementation notes
#
# The Hamming distance is only defined for sequences of equal length, so an
# attempt to calculate it between sequences of different lengths should not
# work.
#
# Exception messages
#
# Sometimes it is necessary to raise an exception. When you do this, you should
# always include a meaningful error message to indicate what the source of the
# error is. This makes your code more readable and helps significantly with
# debugging. For situations where you know that the error source will be a
# certain type, you can choose to raise one of the built in error types, but
# should still include a meaningful message.
#
# This particular exercise requires that you use the raise statement to "throw"
# a ValueError when the strands being checked are not the same length. The tests
# will only pass if you both raise the exception and include a message with it.
#
# To raise a ValueError with a message, write the message as an argument to the
# exception type:
#
# # When the sequences being passed are not the same length.
# raise ValueError("Strands must be of equal length.")
#
# References:
# - https://exercism.org/tracks/python/exercises/hamming
#


def distance(
    first: str,
    second: str,
) -> int:
    """Calculate the Hamming distance between two DNA strands.

    The Hamming distance is the number of differences between two DNA sequences
    of equal length.

    Args:
        first (str): The first DNA sequence string containing only A,C,G,T characters
        second (str): The second DNA sequence string containing only A,C,G,T characters

    Returns:
        int: The Hamming distance (number of differences) between the sequences

    Raises:
        ValueError: If the sequences are not of equal length
        ValueError: If either sequence contains invalid DNA nucleotides (not A,C,G,T)

    Example:
        >>> distance("GGACGGATTCTG", "AGGACGGATTCT")
        9
        >>> distance("AATG", "AATG")
        0
    """
    if len(first) != len(second):
        raise ValueError("Strands must be of equal length.")

    if not all(nuc in "ACGT" for nuc in first + second):
        raise ValueError("String contains invalid DNA nucleotides")

    return sum(1 for left, right in zip(first, second) if left != right)
