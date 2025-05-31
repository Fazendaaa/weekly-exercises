from pytest import raises
from weekly_exercises.squareRoot import squareRoot


def test_error_squareRoot():
    with raises(ValueError, match="Invalid input of class: str"):
        squareRoot("1")


def test_first_squareRoot():
    assert squareRoot(1) == 1


def test_second_squareRoot():
    assert squareRoot(4) == 2


def test_third_squareRoot():
    assert squareRoot(4) == 2


def test_fourth_squareRoot():
    assert squareRoot(25) == 5


def test_fifth_squareRoot():
    assert squareRoot(81) == 9


def test_sixth_squareRoot():
    assert squareRoot(65025) == 255
