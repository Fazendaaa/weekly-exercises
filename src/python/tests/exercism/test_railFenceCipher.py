from weekly_exercises.exercism.railFenceCipher import RailFence


def test_encode_with_two_rails() -> None:
    assert RailFence().encode("XOXOXOXOXOXOXOXOXO", 2) == "XXXXXXXXXOOOOOOOOO"


def test_encode_with_three_rails() -> None:
    assert (
        RailFence().encode("WEAREDISCOVEREDFLEEATONCE", 3)
        == "WECRLTEERDSOEEFEAOCAIVDEN"
    )


def test_encode_with_ending_in_the_middle() -> None:
    assert RailFence().encode("EXERCISES", 4) == "ESXIEECSR"


def test_decode_with_three_rails() -> None:
    assert RailFence().decode("TEITELHDVLSNHDTISEIIEA", 3) == "THEDEVILISINTHEDETAILS"


def test_decode_with_five_rails() -> None:
    assert RailFence().decode("EIEXMSMESAORIWSCE", 5) == "EXERCISMISAWESOME"


def test_decode_with_six_rails() -> None:
    assert (
        RailFence().decode(
            "133714114238148966225439541018335470986172518171757571896261", 6
        )
        == "112358132134558914423337761098715972584418167651094617711286"
    )
