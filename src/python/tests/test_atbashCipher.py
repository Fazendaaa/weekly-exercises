from weekly_exercises.atbashCipher import decode, encode


def test_first_encode() -> None:
    assert encode("test", 5) == "gvhg"


def test_second_encode() -> None:
    assert encode("x123 yes", 5) == "c123b vh"


def test_first_decode() -> None:
    assert decode("gvhg") == "test"


def test_second_decode() -> None:
    assert (
        decode("gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt")
        == "thequickbrownfoxjumpsoverthelazydog"
    )
