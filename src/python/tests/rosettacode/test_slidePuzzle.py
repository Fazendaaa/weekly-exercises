from weekly_exercises.rosettacode.slidePuzzle import (
    slidePuzzleNonOptimal,
    slidePuzzleOptimal,
)


def test_generated_already_sorted() -> None:
    assert "Already sorted" == slidePuzzleNonOptimal(
        [
            [0, 1],
            [2, 3],
        ],
        False,
    )


def test_generated_already_sorted_alternative() -> None:
    assert "Already sorted" == slidePuzzleNonOptimal(
        [
            [0, 1],
            [2, 3],
        ],
        True,
    )


def test_generated_right_right() -> None:
    assert "rr" == slidePuzzleNonOptimal(
        [
            [1, 0],
            [2, 3],
        ],
        False,
    )


def test_generated_up_alternative() -> None:
    assert "u" == slidePuzzleNonOptimal(
        [
            [2, 1],
            [0, 3],
        ],
        True,
    )


def test_generated_right() -> None:
    assert "r" == slidePuzzleNonOptimal(
        [
            [1, 2],
            [0, 3],
        ],
        False,
    )


def test_generated_down() -> None:
    assert "d" == slidePuzzleNonOptimal(
        [
            [1, 0],
            [3, 2],
        ],
        False,
    )


def test_generated_simple() -> None:
    assert "uurrrrrr" == slidePuzzleNonOptimal(
        [
            [1, 2, 5],
            [3, 4, 8],
            [6, 7, 0],
        ],
        False,
    )


def test_generated_simple_alternative() -> None:
    assert "uull" == slidePuzzleNonOptimal(
        [
            [1, 2, 5],
            [3, 4, 8],
            [6, 7, 0],
        ],
        True,
    )


def test_first_example() -> None:
    assert "rrrulddluuuldrurdddrullulurrrddldluurddlulurruldrdrd" == slidePuzzleOptimal(
        [
            [15, 14, 1, 6],
            [9, 11, 4, 12],
            [0, 10, 7, 3],
            [13, 8, 5, 2],
        ]
    )


# def test_second_example() -> None:
#    assert "rrruldluuldrurdddluulurrrdlddruldluurddlulurruldrrdd" == slidePuzzle(
#        [
#            [0, 12, 9, 13],
#            [15, 11, 10, 14],
#            [3, 7, 2, 5],
#            [4, 8, 6, 1],
#        ]
#    )
