from weekly_exercises.exercism.zebraPuzzle import Zebra


def test_zebra_first() -> None:
    zebra = Zebra(
        houses=5,
        colors={"red", "green", "ivory", "yellow", "blue"},
        nationalities={
            "Englishman",
            "Spaniard",
            "Ukrainian",
            "Norwegian",
            "Japanese",
        },
        pets={"dog", "snails", "fox", "horse", "zebra"},
        drinks={"coffee", "tea", "milk", "orange juice", "water"},
        hobbies={"dancing", "painting", "reading", "football", "chess"},
    )

    zebra.relate("nationality", "Englishman", "is", "color", "red")
    zebra.relate("nationality", "Spaniard", "same_house", "pet", "dog")
    zebra.relate("color", "green", "same_house", "drink", "coffee")
    zebra.relate("nationality", "Ukrainian", "same_house", "drink", "tea")
    zebra.relate("color", "green", "right_of", "color", "ivory")
    zebra.relate("pet", "snail", "same_house", "hobby", "dancing")
    zebra.relate("color", "yellow", "same_house", "hobby", "painting")
    zebra.relate("position", 3, "same_house", "drink", "milk")
    zebra.relate("nationality", "Norwegian", "is", "position", 1)
    zebra.relate("hobby", "reading", "next_to", "pet", "fox")
    zebra.relate("hobby", "painting", "next_to", "pet", "horse")
    zebra.relate("hobby", "football", "same_house", "drink", "orange juice")
    zebra.relate("nationality", "Japanese", "same_house", "hobby", "chess")
    zebra.relate("nationality", "Norwegian", "next_to", "color", "blue")

    zebra.solve()

    assert "Norwegian" == zebra.houses
    assert "Japanese" == zebra.houses
