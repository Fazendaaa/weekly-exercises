from weekly_exercises.minesweeper import minesweeper


def test_example() -> None:
    board = [
        ["·", "*", "·", "*", "·"],
        ["·", "·", "*", "·", "·"],
        ["·", "·", "*", "·", "·"],
        ["·", "·", "·", "·", "·"],
    ]
    output = [
        ["1", "*", "3", "*", "1"],
        ["1", "3", "*", "3", "1"],
        ["·", "2", "*", "2", "·"],
        ["·", "1", "1", "1", "·"],
    ]

    assert minesweeper(board) == output
