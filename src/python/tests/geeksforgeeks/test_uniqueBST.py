import pytest
from weekly_exercises.geeksforgeeks.uniqueBST import uniqueBST


@pytest.mark.parametrize(
    "output, number",
    [
        (5, 3),
        (2, 2),
    ],
)
def test_examples(
    output: int,
    number: int,
) -> None:
    assert output == uniqueBST(number)
