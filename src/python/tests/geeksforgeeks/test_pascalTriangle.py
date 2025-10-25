from weekly_exercises.geeksforgeeks.pascalTriangle import pascalsTriangle


def test_first_example() -> None:
    assert [1, 3, 3, 1] == pascalsTriangle(4)


def test_second_example() -> None:
    assert [1] == pascalsTriangle(1)
