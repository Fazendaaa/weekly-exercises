from weekly_exercises.slidePuzzle import slidePuzzle


def test_generated_already_sorted() -> None:
    assert "Already sorted" == slidePuzzle(
        [
            [0, 1],
            [2, 3],
        ]
    )


def test_generated_left() -> None:
    assert "l" == slidePuzzle(
        [
            [1, 0],
            [2, 3],
        ]
    )


def test_generated_up() -> None:
    assert "u" == slidePuzzle(
        [
            [2, 1],
            [0, 3],
        ]
    )


def test_generated_right() -> None:
    assert "r" == slidePuzzle(
        [
            [1, 2],
            [0, 3],
        ]
    )


def test_generated_down() -> None:
    assert "d" == slidePuzzle(
        [
            [1, 0],
            [3, 2],
        ]
    )


def test_generated_simple() -> None:
    assert "uull" == slidePuzzle(
        [
            [1, 2, 5],
            [3, 4, 8],
            [6, 7, 0],
        ]
    )


def test_first_example() -> None:
    assert "rrrulddluuuldrurdddrullulurrrddldluurddlulurruldrdrd" == slidePuzzle(
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
