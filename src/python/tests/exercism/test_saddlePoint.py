from pytest import raises
from weekly_exercises.exercism.saddlePoints import saddlePoints


def test_example() -> None:
    matrix = [[9, 8, 7, 8], [5, 3, 2, 4], [6, 6, 7, 1]]

    assert [[2, 1]] == saddlePoints(matrix)


def test_first() -> None:
    matrix = [[9, 8, 7], [5, 3, 2], [6, 6, 7]]

    assert [[2, 1]] == saddlePoints(matrix)


def test_second() -> None:
    matrix = [[4, 5, 4], [3, 5, 5], [1, 5, 4]]

    assert [[1, 2], [2, 2], [3, 2]] == saddlePoints(matrix)


def test_third() -> None:
    matrix = [[6, 7, 8], [5, 5, 5], [7, 5, 6]]

    assert [[2, 1], [2, 2], [2, 3]] == saddlePoints(matrix)


def test_fourth() -> None:
    matrix = [[8, 7, 9], [6, 7, 6], [3, 2, 5]]

    assert [[3, 3]] == saddlePoints(matrix)


def test_fifth() -> None:
    matrix = [[3, 1, 3], [3, 2, 4]]

    assert [[1, 1], [1, 3]] == saddlePoints(matrix)


def test_sixth() -> None:
    matrix = [[2], [1], [4], [1]]

    assert [[2, 1], [4, 1]] == saddlePoints(matrix)


def test_seventh() -> None:
    matrix = [[2, 5, 3, 5]]

    assert [[1, 2], [1, 4]] == saddlePoints(matrix)


def test_eighth() -> None:
    matrix = [[3, 2, 1], [0, 1], [2, 1, 0]]

    with raises(ValueError, match="irregular matrix"):
        saddlePoints(matrix)


def test_ninth() -> None:
    matrix = []

    with raises(ValueError, match="irregular matrix"):
        saddlePoints(matrix)
