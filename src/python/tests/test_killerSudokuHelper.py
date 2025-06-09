from weekly_exercises.killerSudokuHelper import killerSudokuHelper


def test_first() -> None:
    assert killerSudokuHelper(7, 3) == [(1, 2, 4)]


def test_second() -> None:
    assert killerSudokuHelper(10, 2) == [(1, 9), (2, 8), (3, 7), (4, 6)]


def test_third() -> None:
    assert killerSudokuHelper(10, 2, {1, 4}) == [(2, 8), (3, 7)]


def test_fourth() -> None:
    assert killerSudokuHelper(10, 2, {1, 2, 3, 4, 5, 6, 7, 8, 9}) == []
