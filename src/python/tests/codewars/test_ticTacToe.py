from weekly_exercises.codewars.ticTacToe import isRowWinner


def test_first_example() -> None:
    board = [
        ["X", "X", "X"],
        ["O", "O", "."],
        [".", ".", "."],
    ]

    assert isRowWinner(board)


def test_second_example() -> None:
    board = [
        ["X", "O", "X"],
        ["O", "O", "O"],
        ["X", ".", "X"],
    ]

    assert isRowWinner(board)


def test_third_example() -> None:
    board = [
        ["X", "O", "."],
        [".", "X", "O"],
        [".", ".", "X"],
    ]

    assert not isRowWinner(board)


def test_fourth_example() -> None:
    board = [
        ["X", "X", "X"],
        ["X", "X", "X"],
        [".", ".", "X"],
    ]

    assert not isRowWinner(board)
