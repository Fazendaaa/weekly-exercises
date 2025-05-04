from weekly_exercises.luhn import luhn


def test_first_example():
    assert luhn("4539 3195 0343 6467")


def test_second_example():
    assert not luhn("8273 1232 7352 0569")
