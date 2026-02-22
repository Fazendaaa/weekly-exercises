#                   Number of Unique BST with N Keys
#
# Given an integer n, the task is to find the total number of unique BSTs that
# can be made using values from 1 to n.
#
# Examples:
#
#   Input: n = 3
#   Output: 5
#   Explanation: For n = 3, preorder traversal of Unique BSTs are:
#
#                   3       3       2       1       1
#                  /       /       / \       \       \
#                 2       1       1   3       3       2
#                /         \                 /         \
#               1           2               2           3
#
#   Input: n = 2
#   Output: 2
#   Explanation: For n = 2, preorder traversal of Unique BSTs are:
#
#                            1           2
#                           /             \
#                          2               1
#
# References:
#   - https://www.geeksforgeeks.org/dsa/number-of-unique-bst-with-a-given-key-dynamic-programming/
#

from weekly_exercises.geeksforgeeks.binomialCoefficient import binomialCoefficient


def uniqueBST(
    number: int,
) -> int:
    """
    Calculate the number of unique Binary Search Trees (BSTs) that can be constructed with n keys.

    This function uses the Catalan number formula to compute the result. The nth Catalan number
    gives the number of structurally different BSTs that can be formed using n distinct keys.
    The formula used is: C(n) = (2n)! / ((n+1)! * n!) = C(2n, n) / (n+1)
    where C(2n, n) is the binomial coefficient.

    Args:
        number (int): The number of distinct keys (nodes) to use for constructing BSTs.
                     Must be a non-negative integer.

    Returns:
        int: The total number of unique BSTs that can be constructed using the given number of keys.

    Examples:
        >>> uniqueBST(3)
        5
        >>> uniqueBST(2)
        2
        >>> uniqueBST(0)
        1
        >>> uniqueBST(1)
        1
    """
    coefficient = binomialCoefficient(2 * number, number)

    return coefficient // (number + 1)
