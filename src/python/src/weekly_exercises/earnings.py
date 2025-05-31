#                 Maximize your earnings with mandatory breaks
#
#   Description:
#
# Task
#
# You have a list of daily earnings from a freelance job. You can choose to work
# or skip those days. You can work for up to k consecutive days, but after that,
# you must take at least one break day where you earn nothing.
#
# Your task is to determine the maximum total earnings you can achieve while
# following this rule.
#
# Inputs
#
#   - earnings: an array of non-negative integers ( 0 <= length earnings < 100 ).
#   - k: an integer representing the maximum number of consecutive working days ( 1 <= k < 100 ).
#
# Output
#
#   - an integer representing the maximum earnings you can achieve while
#     respecting the mandatory break rule.
#
#   Example
#
#   For earnings = [60, 70, 80, 40, 80, 90, 100, 20], k = 3, return 480. Forgo earning 40 and 20.
#   For earnings = [45, 12, 78, 34, 56, 89, 23, 67, 91], k = 4, return 460. Forgo earning 12 and 23.
#
# Credit
#
# Original idea by @daryjoe.
#
# Reference:
#   - https://www.codewars.com/kata/66e03a09eeaad7e94d9f40a9
#


def earnings(values: list[int], k: int) -> int:
    """
    Calculate the maximum earnings by considering the mandatory break rule.

    Args:
        values (list[int]): A list of daily earnings.
        k (int): The maximum number of consecutive working days.

    Returns:
        int: The maximum total earnings achievable while respecting the mandatory break rule.
    """

    try:
        assert isinstance(values, list)
        assert isinstance(k, int)
        assert all(isinstance(value, int) for value in values)
        assert 1 <= k < 100
        assert all(0 <= value for value in values)
    except AssertionError:
        raise ValueError("Invalid input")

    length = len(values)

    if 0 == length:
        return 0

    result = [0] * (length + 1)

    for outerIndex in range(1, length + 1):
        maxValue = result[outerIndex - 1]

        for innerIndex in range(1, min(k, outerIndex) + 1):
            start = outerIndex - innerIndex
            total = sum(values[start:outerIndex])

            if outerIndex - innerIndex - 1 >= 0:
                total += result[outerIndex - innerIndex - 1]

            if total > maxValue:
                maxValue = total

        result[outerIndex] = maxValue

    return result[length]
