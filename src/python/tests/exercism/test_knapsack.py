from weekly_exercises.exercism.knapsack import Knapsack


def test_knapsack_no_items() -> None:
    assert 0 == Knapsack(100, [])


def test_knapsack_too_heavy() -> None:
    assert 0 == Knapsack(10, [{"weight": 100, "value": 1}])


def test_knapsack_five_items_cannot_be_greedy_by_weight() -> None:
    assert 21 == Knapsack(
        10,
        [
            {"weight": 2, "value": 5},
            {"weight": 2, "value": 5},
            {"weight": 2, "value": 5},
            {"weight": 2, "value": 5},
            {"weight": 10, "value": 21},
        ],
    )


def test_knapsack_example() -> None:
    assert 90 == Knapsack(
        10,
        [
            {"weight": 5, "value": 10},
            {"weight": 4, "value": 40},
            {"weight": 6, "value": 30},
            {"weight": 4, "value": 50},
        ],
    )


def test_knapsack_eight_items() -> None:
    assert 900 == Knapsack(
        104,
        [
            {"weight": 25, "value": 350},
            {"weight": 35, "value": 400},
            {"weight": 45, "value": 450},
            {"weight": 5, "value": 20},
            {"weight": 25, "value": 70},
            {"weight": 3, "value": 8},
            {"weight": 2, "value": 5},
            {"weight": 2, "value": 5},
        ],
    )


def test_knapsack_fifteen_items() -> None:
    assert 1458 == Knapsack(
        750,
        [
            {"weight": 70, "value": 135},
            {"weight": 73, "value": 139},
            {"weight": 77, "value": 149},
            {"weight": 80, "value": 150},
            {"weight": 82, "value": 156},
            {"weight": 87, "value": 163},
            {"weight": 90, "value": 173},
            {"weight": 94, "value": 184},
            {"weight": 98, "value": 192},
            {"weight": 106, "value": 201},
            {"weight": 110, "value": 210},
            {"weight": 113, "value": 214},
            {"weight": 115, "value": 221},
            {"weight": 118, "value": 229},
            {"weight": 120, "value": 240},
        ],
    )
