from weekly_exercises.exercism.spaceAge import SpaceAge


def test_age_on_earth() -> None:
    assert SpaceAge(1_000_000_000).on_earth() == 31.69


def test_age_on_mercury() -> None:
    assert SpaceAge(2_134_835_688).on_mercury() == 280.88


def test_age_on_venus() -> None:
    assert SpaceAge(189_839_836).on_venus() == 9.78


def test_age_on_mars() -> None:
    assert SpaceAge(2_129_871_239).on_mars() == 35.88


def test_age_on_jupiter() -> None:
    assert SpaceAge(901_876_382).on_jupiter() == 2.41


def test_age_on_saturn() -> None:
    assert SpaceAge(2_000_000_000).on_saturn() == 2.15


def test_age_on_uranus() -> None:
    assert SpaceAge(1_210_123_456).on_uranus() == 0.46


def test_age_on_neptune() -> None:
    assert SpaceAge(1_821_023_456).on_neptune() == 0.35
