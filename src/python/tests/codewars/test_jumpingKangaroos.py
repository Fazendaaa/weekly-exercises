from weekly_exercises.codewars.jumpingKangaroos import Kangaroo, Race


def test_identical() -> None:
    race = Race()
    race.addCompetitor(Kangaroo(0, 2))
    race.addCompetitor(Kangaroo(0, 2))

    assert race.meet()


def test_example() -> None:
    race = Race()
    race.addCompetitor(Kangaroo(0, 3))
    race.addCompetitor(Kangaroo(4, 2))

    assert race.meet()


def test_other_example() -> None:
    race = Race()
    race.addCompetitor(Kangaroo(0, 2))
    race.addCompetitor(Kangaroo(5, 3))

    assert not race.meet()
