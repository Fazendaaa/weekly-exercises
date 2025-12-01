from pytest import raises
from weekly_exercises.exercism.hamming import distance


def test_empty_strands() -> None:
    assert distance("", "") == 0


def test_single_letter_identical_strands() -> None:
    assert distance("A", "A") == 0


def test_single_letter_different_strands() -> None:
    assert distance("G", "T") == 1


def test_long_identical_strands() -> None:
    assert distance("GGACTGAAATCTG", "GGACTGAAATCTG") == 0


def test_long_different_strands() -> None:
    assert distance("GGACGGATTCTG", "AGGACGGATTCT") == 9


def test_disallow_first_strand_longer() -> None:
    with raises(ValueError, match="Strands must be of equal length."):
        distance("AATG", "AAA")


def test_disallow_second_strand_longer() -> None:
    with raises(ValueError, match="Strands must be of equal length."):
        distance("ATA", "AGTG")


def test_disallow_empty_first_strand() -> None:
    with raises(ValueError, match="Strands must be of equal length."):
        distance("", "G")


def test_disallow_empty_second_strand() -> None:
    with raises(ValueError, match="Strands must be of equal length."):
        distance("G", "")
