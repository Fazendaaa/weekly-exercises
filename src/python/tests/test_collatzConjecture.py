import pytest
from weekly_exercises.collatzConjecture import collatzConjecture


def test_non_valid_input() -> None:
    with pytest.raises(ValueError, match="Only positive integers are allowed"):
        collatzConjecture(-1)


def test_example() -> None:
    assert collatzConjecture(6) == 8
