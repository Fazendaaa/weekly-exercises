from pytest import raises
from weekly_exercises.exercism.phoneNumber import PhoneNumber


def test_cleans_the_number() -> None:
    number = PhoneNumber("(223) 456-7890").number

    assert number == "2234567890"


def test_cleans_numbers_with_dots() -> None:
    number = PhoneNumber("223.456.7890").number

    assert number == "2234567890"


def test_cleans_numbers_with_multiple_spaces() -> None:
    number = PhoneNumber("223 456   7890   ").number

    assert number == "2234567890"


def test_invalid_when_9_digits() -> None:
    with raises(ValueError, match="must not be fewer than 10 digits"):
        PhoneNumber("123456789")


def test_invalid_when_11_digits_does_not_start_with_a_1() -> None:
    with raises(ValueError, match="11 digits must start with 1"):
        PhoneNumber("22234567890")


def test_valid_when_11_digits_and_starting_with_1() -> None:
    number = PhoneNumber("12234567890").number

    assert number == "2234567890"


def test_valid_when_11_digits_and_starting_with_1_even_with_punctuation() -> None:
    number = PhoneNumber("+1 (223) 456-7890").number

    assert number == "2234567890"


def test_invalid_when_more_than_11_digits() -> None:
    with raises(ValueError, match="must not be greater than 11 digits"):
        PhoneNumber("321234567890")


def test_invalid_with_letters() -> None:
    with raises(ValueError, match="letters not permitted"):
        PhoneNumber("523-abc-7890")


def test_invalid_with_punctuations() -> None:
    with raises(ValueError, match="punctuations not permitted"):
        PhoneNumber("523-@:!-7890")


def test_invalid_if_area_code_starts_with_0() -> None:
    with raises(ValueError, match="area code cannot start with zero"):
        PhoneNumber("(023) 456-7890")


def test_invalid_if_area_code_starts_with_1() -> None:
    with raises(ValueError, match="area code cannot start with one"):
        PhoneNumber("(123) 456-7890")


def test_invalid_if_exchange_code_starts_with_0() -> None:
    with raises(ValueError, match="exchange code cannot start with zero"):
        PhoneNumber("(223) 056-7890")


def test_invalid_if_exchange_code_starts_with_1() -> None:
    with raises(ValueError, match="exchange code cannot start with one"):
        PhoneNumber("(223) 156-7890")


def test_invalid_if_area_code_starts_with_0_on_valid_11_digit_number() -> None:
    with raises(ValueError, match="area code cannot start with zero"):
        PhoneNumber("1 (023) 456-7890")


def test_invalid_if_area_code_starts_with_1_on_valid_11_digit_number() -> None:
    with raises(ValueError, match="area code cannot start with one"):
        PhoneNumber("1 (123) 456-7890")


def test_invalid_if_exchange_code_starts_with_0_on_valid_11_digit_number() -> None:
    with raises(ValueError, match="exchange code cannot start with zero"):
        PhoneNumber("1 (223) 056-7890")


def test_invalid_if_exchange_code_starts_with_1_on_valid_11_digit_number() -> None:
    with raises(ValueError, match="exchange code cannot start with one"):
        PhoneNumber("1 (223) 156-7890")


# Additional tests for this track
def test_area_code() -> None:
    number = PhoneNumber("2234567890")

    assert number.area_code == "223"


def test_pretty_print() -> None:
    number = PhoneNumber("2234567890")

    assert number.pretty() == "(223)-456-7890"


def test_pretty_print_with_full_us_phone_number() -> None:
    number = PhoneNumber("12234567890")

    assert number.pretty() == "(223)-456-7890"
