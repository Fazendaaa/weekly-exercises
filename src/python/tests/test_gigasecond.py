from datetime import datetime

from weekly_exercises.gigasecond import Gigasecond


def test_date_only_specification_of_time() -> None:
    assert Gigasecond(datetime(2011, 4, 25, 0, 0)).add() == datetime(
        2043, 1, 1, 1, 46, 40
    )


def test_second_test_for_date_only_specification_of_time() -> None:
    assert Gigasecond(datetime(1977, 6, 13, 0, 0)).add() == datetime(
        2009, 2, 19, 1, 46, 40
    )


def test_third_test_for_date_only_specification_of_time() -> None:
    assert Gigasecond(datetime(1959, 7, 19, 0, 0)).add() == datetime(
        1991, 3, 27, 1, 46, 40
    )


def test_full_time_specified() -> None:
    assert Gigasecond(datetime(2015, 1, 24, 22, 0)).add() == datetime(
        2046, 10, 2, 23, 46, 40
    )


def test_full_time_with_day_roll_over() -> None:
    assert Gigasecond(datetime(2015, 1, 24, 23, 59, 59)).add() == datetime(
        2046, 10, 3, 1, 46, 39
    )
