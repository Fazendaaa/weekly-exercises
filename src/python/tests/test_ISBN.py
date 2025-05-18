from weekly_exercises.ISBN import isISBN


def test_example_truthfully() -> None:
    assert isISBN("3-598-21508-8")


def test_example_wrongfully() -> None:
    assert not isISBN("3-598-21508-0")
