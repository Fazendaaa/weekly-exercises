#           Maximize the number of segments of length x, y and z
#
# Given a rod of length n, the task is to cut the rod in such a way that the
# total number of segments of length x, y, and z is maximized. The segments can
# only be of length x, y, and z.
# Note: If no segment can be cut then return 0.
#
# Reference:
#   - https://www.geeksforgeeks.org/dsa/maximize-the-number-of-segments-of-length-p-q-and-r/
#

from functools import lru_cache


@lru_cache(maxsize=None)
def __maximizeSegments__(
    length: int,
    sizeA: int,
    sizeB: int,
    sizeC: int,
) -> int:
    """
    Helper function to recursively calculate the maximum number of segments.

    Args:
        length: Current remaining length of the rod
        sizeA: Length of segment type A
        sizeB: Length of segment type B
        sizeC: Length of segment type C

    Returns:
        Maximum number of segments possible, or -1 if no valid cuts can be made
    """
    if not length:
        return 0

    if length < 0:
        return -1

    cut1 = __maximizeSegments__(length - sizeA, sizeA, sizeB, sizeC)
    cut2 = __maximizeSegments__(length - sizeB, sizeA, sizeB, sizeC)
    cut3 = __maximizeSegments__(length - sizeC, sizeA, sizeB, sizeC)
    maxCut = max(cut1, cut2, cut3)

    return -1 if -1 == maxCut else maxCut + 1


def maximizeSegments(
    length: int,
    sizeA: int,
    sizeB: int,
    sizeC: int,
) -> int:
    """
    Maximize the number of segments of length sizeA, sizeB, and sizeC from a rod of given length.

    Given a rod of length n, cuts the rod to maximize the total number of segments
    where each segment must be of length sizeA, sizeB, or sizeC.

    Args:
        length: Total length of the rod to be cut
        sizeA: Length of segment type A
        sizeB: Length of segment type B
        sizeC: Length of segment type C

    Returns:
        Maximum number of segments possible. Returns 0 if no segments can be cut.
    """
    if length < min(sizeA, sizeB, sizeC):
        return 0

    return (
        0 if -1 == (res := __maximizeSegments__(length, sizeA, sizeB, sizeC)) else res
    )
