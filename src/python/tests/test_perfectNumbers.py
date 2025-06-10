from pytest import raises
from weekly_exercises.perfectNumbers import perfectNumbers


def test_first() -> None:
    assert "perfect" == perfectNumbers(6)


def test_second() -> None:
    assert "perfect" == perfectNumbers(28)


def test_third() -> None:
    assert "perfect" == perfectNumbers(33550336)


def test_fourth() -> None:
    assert "abundant" == perfectNumbers(30)


def test_fifth() -> None:
    assert "abundant" == perfectNumbers(30)


def test_sixth() -> None:
    assert "abundant" == perfectNumbers(33550335)


def test_seventh() -> None:
    assert "deficient" == perfectNumbers(2)


def test_eighth() -> None:
    assert "deficient" == perfectNumbers(4)


def test_ninth() -> None:
    assert "deficient" == perfectNumbers(32)


def test_tenth() -> None:
    assert "deficient" == perfectNumbers(33550337)


def test_eleventh() -> None:
    assert "deficient" == perfectNumbers(2)


def test_twelfth() -> None:
    assert "perfect" == perfectNumbers(6)


def test_thirteen() -> None:
    with raises(
        ValueError, match="Classification is only possible for positive integers."
    ):
        perfectNumbers(0)


def test_fourteen() -> None:
    with raises(
        ValueError, match="Classification is only possible for positive integers."
    ):
        perfectNumbers(-1)
