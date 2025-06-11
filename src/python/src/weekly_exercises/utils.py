from itertools import chain
from math import sqrt


def flatten[T](value: list[list[T]]) -> list[T]:
    """
    Flattens a list of lists into a single list.

    Args:
        value (list[list[T]]): A list of lists to be flattened.

    Returns:
        list[T]: A flattened list containing all elements from the input lists.
    """
    return list(chain(*value))


def allDivisors(n: int, sort: bool = False) -> list[int]:
    """
    Returns a list of all divisors of a given number, including 1 and the number itself.

    This function uses the following algorithm:
    1. If n is negative, return [0].
    2. If n is 1, return [1].
    3. Otherwise, iterate from 1 to the square root of n (inclusive).
       a. If n is divisible by i, add i and n/i to the list of divisors.
       b. Use a set to remove duplicates and convert the set back to a list.
       c. Sort the list of divisors in ascending order.
       d. Return the list of divisors.

    Example:
        >>> all_divisors_ = allDivisors(12, True)
        >>> all_divisors_
        [1, 2, 3, 4, 6, 12]
    Args:
        n (int): _description_

    Returns:
        list[int]: _description_
    """

    divisors: list[int] = []

    if 0 > n:
        divisors.append(0)
    elif 1 == n:
        divisors.append(1)
    else:
        for i in range(1, int(sqrt(n)) + 1):
            if 0 == n % i:
                divisors.append(i)
                if int(n / i) != i:
                    divisors.append(int(n / i))

    if sort:
        divisors.sort()

    return divisors
