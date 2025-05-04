from weekly_exercises.armstrongNumbers import armstrongNumbers


def test_first_example():
    assert armstrongNumbers(9)


def test_second_example():
    assert not armstrongNumbers(19)


def test_third_example():
    assert armstrongNumbers(153)


def test_fourth_example():
    assert not armstrongNumbers(154)
