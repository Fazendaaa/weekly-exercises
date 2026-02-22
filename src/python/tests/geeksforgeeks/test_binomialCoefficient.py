import pytest
from weekly_exercises.geeksforgeeks.binomialCoefficient import binomialCoefficient


@pytest.mark.parametrize(
    "output, n, k",
    [
        (6, 4, 2),
        (10, 5, 2),
        (20, 6, 3),
    ],
)
def test_examples(
    output: int,
    n: int,
    k: int,
) -> None:
    assert output == binomialCoefficient(n, k)
