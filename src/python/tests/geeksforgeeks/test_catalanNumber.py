import pytest
from weekly_exercises.geeksforgeeks.catalanNumber import catalanNumber


@pytest.mark.parametrize(
    "output, number",
    [
        (132, 6),
        (1430, 8),
        (42, 5),
    ],
)
def test_examples(
    output: int,
    number: int,
) -> None:
    assert output == catalanNumber(number)
