#                   Minimum Cost to Reach the Top
#
# Given an array of integers cost[] of length n, where cost[i] is the cost of
# the ith step on a staircase. Once the cost is paid, we can either climb one or
# two steps.
# We can either start from the step with index 0, or the step with index 1. The
# task is to find the minimum cost to reach the top.
#
# Reference:
#   - https://www.geeksforgeeks.org/dsa/minimum-cost-to-reach-the-top-of-the-floor-by-climbing-stairs/
#

from functools import lru_cache


@lru_cache(maxsize=None)
def __minimumCost__(
    index: int,
    cost: tuple[int],
) -> int:
    """
    Helper function to calculate minimum cost to reach a specific step.

    Args:
        index (int): The current step index
        cost (list[int]): Array of costs for each step

    Returns:
        int: Minimum cost to reach the step at given index
    """
    return (
        cost[index]
        if not index or 1 == index
        else cost[index]
        + min(
            __minimumCost__(index - 1, cost),
            __minimumCost__(index - 2, cost),
        )
    )


def minimumCost(
    cost: list[int],
) -> int:
    """
    Find the minimum cost to reach the top of the staircase.

    You can start from step 0 or step 1, and from each step you can climb
    either 1 or 2 steps. The goal is to reach beyond the last step with
    minimum total cost.

    Args:
        cost (list[int]): Array where cost[i] represents the cost of step i

    Returns:
        int: Minimum cost to reach the top of the staircase

    Example:
        >>> minimumCost([10, 15, 20])
        15
        >>> minimumCost([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
        6
    """
    return (
        cost[0]
        if 1 == (length := len(cost))
        else min(
            __minimumCost__(length - 1, tuple(cost)),
            __minimumCost__(length - 2, tuple(cost)),
        )
    )
