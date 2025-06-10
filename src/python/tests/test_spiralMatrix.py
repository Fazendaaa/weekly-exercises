from weekly_exercises.spiralMatrix import spiralMatrix


def test_first() -> None:
    assert [] == spiralMatrix(0)


def test_second() -> None:
    assert [[1]] == spiralMatrix(1)


def test_third() -> None:
    assert [[1, 2], [4, 3]] == spiralMatrix(2)


def test_fourth() -> None:
    assert [[1, 2, 3], [8, 9, 4], [7, 6, 5]] == spiralMatrix(3)


def test_fifth() -> None:
    assert [
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7],
    ] == spiralMatrix(4)


def test_sixth() -> None:
    assert [
        [1, 2, 3, 4, 5],
        [16, 17, 18, 19, 6],
        [15, 24, 25, 20, 7],
        [14, 23, 22, 21, 8],
        [13, 12, 11, 10, 9],
    ] == spiralMatrix(5)
