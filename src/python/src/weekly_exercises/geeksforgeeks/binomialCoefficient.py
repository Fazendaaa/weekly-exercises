#                       Binomial Coefficient
#
# Given an integer values n and k, the task is to find the value of
# Binomial Coefficient C(n, k).
#
#   - A binomial coefficient C(n, k) can be defined as the coefficient of x^k
#     in the expansion of (1 + x)^n.
#   - A binomial coefficient C(n, k) also gives the number of ways, disregarding
#     order, that k objects can be chosen from among n objects more formally,
#     the number of k-element subsets (or k-combinations) of a n-element set.
#
# Examples
#
#   Input: n = 4, k = 2
#   Output: 6
#   Explanation: The value of 4C2 is (4 × 3) / (2 × 1) = 6.
#
#   Input: n = 5, k = 2
#   Output: 10
#   Explanation: The value of 5C2 is (5 × 4) / (2 × 1) = 10.
#
#   Input: n = 6, k = 3
#   Output: 20
#   Explanation: The value of 6C3 is (6 × 5 × 4) / (3 × 2 × 1) = 20.
#
# References:
#   - https://www.geeksforgeeks.org/dsa/binomial-coefficient-dp-9/
#

from functools import lru_cache


@lru_cache(maxsize=None)
def binomialCoefficient(
    n: int,
    k: int,
) -> int:
    """
    Calculate the binomial coefficient C(n, k) using dynamic programming.

    The binomial coefficient C(n, k) represents the number of ways to choose
    k elements from a set of n elements, or equivalently, the coefficient of
    x^k in the expansion of (1 + x)^n.

    Args:
        n (int): Total number of items
        k (int): Number of items to choose

    Returns:
        int: The binomial coefficient C(n, k)

    Base cases:
        - If k > n: Return 0 (impossible to choose more items than available)
        - If k == 0 or k == n: Return 1 (only one way to choose all or none)
        - If k == 1: Return n (n ways to choose 1 item from n items)
    """
    if k > n:
        return 0

    if k == 0 or k == n:
        return 1

    if k == 1:
        return n

    return binomialCoefficient(n - 1, k - 1) + binomialCoefficient(n - 1, k)
