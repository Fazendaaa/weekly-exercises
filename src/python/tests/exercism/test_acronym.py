from weekly_exercises.exercism.acronym import abbreviate


def test_basic() -> None:
    assert abbreviate("Portable Network Graphics") == "PNG"


def test_lowercase_words() -> None:
    assert abbreviate("Ruby on Rails") == "ROR"


def test_punctuation() -> None:
    assert abbreviate("First In, First Out") == "FIFO"


def test_all_caps_word() -> None:
    assert abbreviate("GNU Image Manipulation Program") == "GIMP"


def test_punctuation_without_whitespace() -> None:
    assert abbreviate("Complementary metal-oxide semiconductor") == "CMOS"


def test_very_long_abbreviation() -> None:
    assert (
        abbreviate(
            "Rolling On The Floor Laughing So Hard That My Dogs Came Over And Licked Me"
        )
        == "ROTFLSHTMDCOALM"
    )


def test_consecutive_delimiters() -> None:
    assert abbreviate("Something - I made up from thin air") == "SIMUFTA"


def test_apostrophes() -> None:
    assert abbreviate("Halley's Comet") == "HC"


def test_underscore_emphasis() -> None:
    assert abbreviate("The Road _Not_ Taken") == "TRNT"
