from weekly_exercises.geeksforgeeks.minimumCost import minimumCost


def test_first_example() -> None:
    assert 15 == minimumCost([10, 15, 20])


def test_second_example() -> None:
    assert 6 == minimumCost([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
