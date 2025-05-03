from src.weekly_exercises.puzzleSolver import PuzzleSolver


def test_first_example():
    assert "rrruldluuldrurdddluulurrrdlddruldluurddlulurruldrrdd" == PuzzleSolver(
        [
            [15, 14, 1, 6],
            [9, 11, 4, 12],
            [0, 10, 7, 3],
            [13, 8, 5, 2],
        ]
    )


def test_second_example():
    assert "rrruldluuldrurdddluulurrrdlddruldluurddlulurruldrrdd" == PuzzleSolver(
        [
            [0, 12, 9, 13],
            [15, 11, 10, 14],
            [3, 7, 2, 5],
            [4, 8, 6, 1],
        ]
    )
