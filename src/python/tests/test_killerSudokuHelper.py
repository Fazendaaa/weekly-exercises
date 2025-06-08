from weekly_exercises.killerSudokuHelper import killerSudokuHelper


def test_example() -> None:
    assert killerSudokuHelper(12, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1
