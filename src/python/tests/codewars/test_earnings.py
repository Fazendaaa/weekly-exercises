from pytest import raises
from weekly_exercises.codewars.earnings import earnings


def test_error_earnings():
    with raises(ValueError, match="Invalid input"):
        earnings([], "3")


def test_first_earnings():
    assert earnings([60, 70, 80, 40, 80, 90, 100, 20], 3) == 480


def test_second_earnings():
    assert earnings([45, 12, 78, 34, 56, 89, 23, 67, 91], 4) == 460
