from pytest import raises
from weekly_exercises.minesweeper import minesweeper


def test_non_valid_input() -> None:
    board = [
        ["·", "*", "·", "*", "·"],
        ["·", "·", "*", "·", "·"],
        ["·", "·", "*", "·", "·"],
        ["·", "·", "·", "·", "X"],
    ]

    with raises(ValueError, match="The board is invalid with current input."):
        minesweeper(board)


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
