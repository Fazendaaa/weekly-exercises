from weekly_exercises.geeksforgeeks.maximizeSegments import maximizeSegments


def test_first_example() -> None:
    assert 4 == maximizeSegments(4, 2, 1, 1)


def test_second_example() -> None:
    assert 2 == maximizeSegments(5, 5, 3, 2)


def test_third_example() -> None:
    assert 0 == maximizeSegments(7, 8, 9, 10)
