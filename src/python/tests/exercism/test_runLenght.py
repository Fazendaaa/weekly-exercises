from weekly_exercises.exercism.runLength import decode, encode


def test_first_encode() -> None:
    assert (
        encode("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB")
        == "12WB12W3B24WB"
    )


def test_first_decode() -> None:
    assert (
        decode("12WB12W3B24WB")
        == "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    )


def test_second_encode() -> None:
    assert encode("AABCCCDEEEE") == "2AB3CD4E"


def test_second_decode() -> None:
    assert decode("2AB3CD4E") == "AABCCCDEEEE"
