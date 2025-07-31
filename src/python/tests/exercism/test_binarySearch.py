from pytest import raises
from weekly_exercises.exercism.binarySearch import binarySearch


def test_first() -> None:
    assert 4 == binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)


def test_second() -> None:
    assert 3 == binarySearch([1, 3, 4, 6, 8, 9, 11], 6)


def test_third() -> None:
    assert 3 == binarySearch([1, 3, 4, 6, 8, 9, 11], 6)


def test_fourth() -> None:
    assert 0 == binarySearch([1, 3, 4, 6, 8, 9, 11], 1)


def test_sixth() -> None:
    assert 9 == binarySearch([1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 634], 144)


def test_seventh() -> None:
    assert 5 == binarySearch([1, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377], 21)


def test_eighth() -> None:
    with raises(ValueError, match="value not in array"):
        binarySearch([1, 3, 4, 6, 8, 9, 11], 7)


def test_ninth() -> None:
    with raises(ValueError, match="value not in array"):
        binarySearch([1, 3, 4, 6, 8, 9, 11], 0)


def test_tenth() -> None:
    with raises(ValueError, match="value not in array"):
        binarySearch([1, 3, 4, 6, 8, 9, 11], 13)


def test_eleventh() -> None:
    with raises(ValueError, match="value not in array"):
        binarySearch([], 1)


def test_twelfth() -> None:
    with raises(ValueError, match="value not in array"):
        binarySearch([1, 2], 0)
