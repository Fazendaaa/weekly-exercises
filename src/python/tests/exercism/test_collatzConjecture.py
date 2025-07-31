from pytest import raises
from weekly_exercises.exercism.collatzConjecture import collatzConjecture


def test_non_valid_input() -> None:
    with raises(ValueError, match="Only positive integers are allowed"):
        collatzConjecture(-1)


def test_example() -> None:
    assert collatzConjecture(6) == 8
