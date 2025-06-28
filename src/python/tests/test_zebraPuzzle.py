from weekly_exercises.zebraPuzzle import Zebra


def test_zebra_first() -> None:
    zebra = Zebra()

    zebra.houses(6)
    zebra.colors(set(["red", "green", "ivory", "yellow", "blue"]))
    zebra.nationalities(
        set(
            [
                "Englishman",
                "Spaniard",
                "Ukrainian",
                "Norwegian",
                "Japanese",
            ]
        )
    )
    zebra.animals(set(["dog", "snails", "fox", "horse", "zebra"]))
    zebra.drinks(set(["coffee", "tea", "milk", "orange juice", "water"]))
    zebra.cigars(
        set(
            [
                "Old Gold",
                "Kools",
                "Chesterfields",
                "Lucky Strike",
                "Parliament",
            ]
        )
    )
    zebra.pets(set(["fox", "horse", "snails", "dog", "zebra"]))

    zebra.solve()

    assert "Norwegian" == zebra.result()
    assert "Japanese" == zebra.result()
