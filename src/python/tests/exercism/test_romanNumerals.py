from pytest import raises
from weekly_exercises.exercism.romanNumerals import roman


def test_error() -> None:
    with raises(ValueError, match="Input cannot be zero or negative values"):
        roman(0)


def test_1_is_i() -> None:
    assert roman(1) == "I"


def test_2_is_ii() -> None:
    assert roman(2) == "II"


def test_3_is_iii() -> None:
    assert roman(3) == "III"


def test_4_is_iv() -> None:
    assert roman(4) == "IV"


def test_5_is_v() -> None:
    assert roman(5) == "V"


def test_6_is_vi() -> None:
    assert roman(6) == "VI"


def test_9_is_ix() -> None:
    assert roman(9) == "IX"


def test_16_is_xvi() -> None:
    assert roman(16) == "XVI"


def test_27_is_xxvii() -> None:
    assert roman(27) == "XXVII"


def test_48_is_xlviii() -> None:
    assert roman(48) == "XLVIII"


def test_49_is_xlix() -> None:
    assert roman(49) == "XLIX"


def test_59_is_lix() -> None:
    assert roman(59) == "LIX"


def test_66_is_lxvi() -> None:
    assert roman(66) == "LXVI"


def test_93_is_xciii() -> None:
    assert roman(93) == "XCIII"


def test_141_is_cxli() -> None:
    assert roman(141) == "CXLI"


def test_163_is_clxiii() -> None:
    assert roman(163) == "CLXIII"


def test_166_is_clxvi() -> None:
    assert roman(166) == "CLXVI"


def test_402_is_cdii() -> None:
    assert roman(402) == "CDII"


def test_575_is_dlxxv() -> None:
    assert roman(575) == "DLXXV"


def test_666_is_dclxvi() -> None:
    assert roman(666) == "DCLXVI"


def test_911_is_cmxi() -> None:
    assert roman(911) == "CMXI"


def test_1024_is_mxxiv() -> None:
    assert roman(1024) == "MXXIV"


def test_1666_is_mdclxvi() -> None:
    assert roman(1666) == "MDCLXVI"


def test_3000_is_mmm() -> None:
    assert roman(3000) == "MMM"


def test_3001_is_mmmi() -> None:
    assert roman(3001) == "MMMI"


def test_3888_is_mmmdccclxxxviii() -> None:
    assert roman(3888) == "MMMDCCCLXXXVIII"


def test_3999_is_mmmcmxcix() -> None:
    assert roman(3999) == "MMMCMXCIX"
