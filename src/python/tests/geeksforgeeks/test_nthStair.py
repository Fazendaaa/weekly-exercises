import pytest
from weekly_exercises.geeksforgeeks.nthStair import nthStair


@pytest.mark.parametrize(
    "output, steps, hops",
    [
        (7, 4, [1, 2, 3]),
        (4, 3, [1, 2, 3]),
    ],
)
def test_examples(
    output: int,
    steps: int,
    hops: list[int],
) -> None:
    assert output == nthStair(steps, hops)
