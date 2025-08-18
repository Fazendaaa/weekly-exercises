from weekly_exercises.codewars.redundantSignalTowers import SignalTowers


def test_example_case() -> None:
    assert (
        SignalTowers(
            [
                (1, 1),
                (2, 1),
                (4, 3),
            ]
        ).find_redundant_towers()
        == 1
    )
