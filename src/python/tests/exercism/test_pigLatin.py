from weekly_exercises.exercism.pigLatin import PigLatin


def test_word_beginning_with_a() -> None:
    assert PigLatin("apple").translate() == "Appleay"


def test_word_beginning_with_e() -> None:
    assert PigLatin("ear").translate() == "Earay"


def test_word_beginning_with_i() -> None:
    assert PigLatin("igloo").translate() == "Iglooay"


def test_word_beginning_with_o() -> None:
    assert PigLatin("object").translate() == "Objectay"


def test_word_beginning_with_u() -> None:
    assert PigLatin("under").translate() == "Underay"


def test_word_beginning_with_a_vowel_and_followed_by_a_qu() -> None:
    assert PigLatin("equal").translate() == "Equalay"


def test_word_beginning_with_p() -> None:
    assert PigLatin("pig").translate() == "Igpay"


def test_word_beginning_with_k() -> None:
    assert PigLatin("koala").translate() == "Oalakay"


def test_word_beginning_with_x() -> None:
    assert PigLatin("xenon").translate() == "Enonxay"


def test_word_beginning_with_q_without_a_following_u() -> None:
    assert PigLatin("qat").translate() == "Atqay"


def test_word_beginning_with_consonant_and_vowel_containing_qu() -> None:
    assert PigLatin("liquid").translate() == "Iquidlay"


def test_word_beginning_with_ch() -> None:
    assert PigLatin("chair").translate() == "Airchay"


def test_word_beginning_with_qu() -> None:
    assert PigLatin("queen").translate() == "Eenquay"


def test_word_beginning_with_qu_and_a_preceding_consonant() -> None:
    assert PigLatin("square").translate() == "Aresquay"


def test_word_beginning_with_th() -> None:
    assert PigLatin("therapy").translate() == "Erapythay"


def test_word_beginning_with_thr() -> None:
    assert PigLatin("thrush").translate() == "Ushthray"


def test_word_beginning_with_sch() -> None:
    assert PigLatin("school").translate() == "Oolschay"


def test_word_beginning_with_yt() -> None:
    assert PigLatin("yttria").translate() == "Yttriaay"


def test_word_beginning_with_xr() -> None:
    assert PigLatin("xray").translate() == "Xrayay"


def test_y_is_treated_like_a_consonant_at_the_beginning_of_a_word() -> None:
    assert PigLatin("yellow").translate() == "Ellowyay"


def test_y_is_treated_like_a_vowel_at_the_end_of_a_consonant_cluster() -> None:
    assert PigLatin("rhythm").translate() == "Ythmrhay"


def test_y_as_second_letter_in_two_letter_word() -> None:
    assert PigLatin("my").translate() == "Ymay"


def test_a_whole_phrase() -> None:
    assert PigLatin("quick fast run").translate() == "Ickquay astfay unray"
