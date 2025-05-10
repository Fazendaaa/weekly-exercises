import itertools


def flatten[T](value: list[list[T]]) -> list[T]:
    """
    Flattens a list of lists into a single list.

    Args:
        value (list[list[T]]): A list of lists to be flattened.

    Returns:
        list[T]: A flattened list containing all elements from the input lists.
    """
    return list(itertools.chain(*value))
