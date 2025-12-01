from pytest import raises
from weekly_exercises.exercism.change import change


def test_change_for_1_cent() -> None:
    assert change([1, 5, 10, 25], 1) == [1]


def test_single_coin_change() -> None:
    assert change([1, 5, 10, 25, 100], 25) == [25]


def test_multiple_coin_change() -> None:
    assert change([1, 5, 10, 25, 100], 15) == [5, 10]


def test_change_with_lilliputian_coins() -> None:
    assert change([1, 4, 15, 20, 50], 23) == [4, 4, 15]


def test_change_with_lower_elbonia_coins() -> None:
    assert change([1, 5, 10, 21, 25], 63) == [21, 21, 21]


def test_large_target_values() -> None:
    assert change([1, 2, 5, 10, 20, 50, 100], 999) == [
        2,
        2,
        5,
        20,
        20,
        50,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
    ]


def test_possible_change_without_unit_coins_available() -> None:
    assert change([2, 5, 10, 20, 50], 21) == [2, 2, 2, 5, 10]


def test_another_possible_change_without_unit_coins_available() -> None:
    assert change([4, 5], 27) == [4, 4, 4, 5, 5, 5]


def test_a_greedy_approach_is_not_optimal() -> None:
    assert change([1, 10, 11], 20) == [10, 10]


def test_no_coins_make_0_change() -> None:
    assert change([1, 5, 10, 21, 25], 0) == []


def test_error_testing_for_change_smaller_than_the_smallest_of_coins() -> None:
    with raises(ValueError, match="can't make target with given coins"):
        change([5, 10], 3)


def test_error_if_no_combination_can_add_up_to_target() -> None:
    with raises(ValueError, match="can't make target with given coins"):
        change([5, 10], 94)


def test_cannot_find_negative_change_values() -> None:
    with raises(ValueError, match="target can't be negative"):
        change([1, 2, 5], -5)
