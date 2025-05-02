from weekly_exercises.ATMHeist import ATMHeist


def test_first_example():
    assert 8 == ATMHeist([3, 1, 3])


def test_second_example():
    assert 10 == ATMHeist([2, 3, 4, 5])


def test_thrid_example():
    assert 26 == ATMHeist([10, 10, 11, 13, 7, 8, 9])


def test_fourth_example():
    assert 34 == ATMHeist([2, 3, 4, 5, 10, 6, 7, 8, 9, 10, 11, 12, 4, 4, 2, 2, 12, 8])
