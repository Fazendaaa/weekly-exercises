from weekly_exercises.ISBN import isISBN


def test_example_truthfully():
    assert True == isISBN("3-598-21508-8")


def test_example_wrongfully():
    assert False == isISBN("3-598-21508-0")
