#                               Square Root
#
#   Introduction
#
# We are launching a deep space exploration rocket and we need a way to make
# sure the navigation system stays on target.
#
# As the first step in our calculation, we take a target number and find its
# square root (that is, the number that when multiplied by itself equals the
# target number).
#
# The journey will be very long. To make the batteries last as long as possible,
# we had to make our rocket's onboard computer very power efficient.
# Unfortunately that means that we can't rely on fancy math libraries and
# functions, as they use more power. Instead we want to implement our own square
# root calculation.
#
#   Instructions
#
# Your task is to calculate the square root of a given number.
#
#   - Try to avoid using the pre-existing math libraries of your language.
#   - As input you'll be given a positive whole number, i.e. 1, 2, 3, 4…
#   - You are only required to handle cases where the result is a positive whole
# number.
#
# Some potential approaches:
#
#   - Linear or binary search for a number that gives the input number when
# squared.
#   - Successive approximation using Newton's or Heron's method.
#   - Calculating one digit at a time or one bit at a time.
#
# You can check out the Wikipedia pages on integer square root and methods of
# computing square roots to help with choosing a method of calculation.
#
#   How this Exercise is Structured in Python
#
# Python offers a wealth of mathematical functions in the form of the math
# module and built-ins such as the exponentiation operator **, pow() and sum().
# However, we'd like you to consider the challenge of solving this exercise
# without those built-ins or modules.
#
# While there is a mathematical formula that will find the square root of any
# number, we have gone the route of having only natural numbers (positive
# integers) as solutions.
#
# It is possible to compute the square root of any natural number using only
# natural numbers in the computation.
#
# References:
#   - https://exercism.org/tracks/python/exercises/square-root
#


def squareRoot(number: int) -> int:
    """
    Calculate the square root of a given number using successive approximation.

    Args:
        number (int): The number for which the square root needs to be calculated.

    Returns:
        int: The square root of the given number, rounded down to the nearest integer.
    """

    try:
        assert isinstance(number, int)
        assert number > 0
    except AssertionError:
        raise ValueError(
            f"Invalid input of class: { type(number).__name__ } or number value: { number }"
        )

    basis = number
    guess = (basis + 1) // 2

    while guess < basis:
        basis = guess
        guess = (basis + number // basis) // 2

    return basis
