#           Count ways to reach the nth stair using step 1, 2 or 3
#
# A child is running up a staircase with n steps and can hop either 1 step, 2
# steps, or 3 steps at a time. The task is to implement a method to count how
# many possible ways the child can run up the stairs.
#
# Examples:
#
#   Input: 4
#   Output: 7
#   Explanation: There are seven ways: {1, 1, 1, 1}, {1, 2, 1}, {2, 1, 1}, {1, 1, 2}, {2, 2}, {3, 1}, {1, 3}.
#
#   Input: 3
#   Output: 4
#   Explanation: There are four ways: {1, 1, 1}, {1, 2}, {2, 1}, {3}.
#
# References:
#   - https://www.geeksforgeeks.org/dsa/count-ways-reach-nth-stair-using-step-1-2-3/
#

from functools import lru_cache


@lru_cache(maxsize=None)
def __nthStair__(
    steps: int,
    hops: tuple[int],
) -> int:
    """
    Helper function to recursively count the number of ways to reach the nth stair.

    Args:
        steps (int): The number of steps remaining to reach the target
        hops (tuple[int]): Tuple of allowed step sizes (e.g., (1, 2, 3))

    Returns:
        int: Number of ways to reach the target from the current position

    Base cases:
        - If steps == 0: There's exactly 1 way (we've reached the target)
        - If steps < 0: There are 0 ways (we've overshot the target)
    """
    if not steps:
        return 1

    if steps < 0:
        return 0

    return sum(__nthStair__(steps - hop, hops) for hop in hops)


def nthStair(
    steps: int,
    hops: list[int],
) -> int:
    """
    Count the number of ways to reach the nth stair using given step sizes.

    A child can hop using any of the step sizes provided in the hops list.
    This function calculates all possible combinations of steps that sum to
    the target number of stairs.

    Args:
        steps (int): The target number of stairs to reach
        hops (list[int]): List of allowed step sizes (e.g., [1, 2, 3])

    Returns:
        int: Total number of different ways to reach the nth stair

    Examples:
        >>> nthStair(4, [1, 2, 3])
        7
        >>> nthStair(3, [1, 2, 3])
        4
    """
    return __nthStair__(steps, tuple(hops))
