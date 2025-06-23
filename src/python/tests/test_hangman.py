from pytest import raises
from weekly_exercises.hangman import Hangman, Status


def test_hangman_foo_one() -> None:
    word = "foo"
    hangman = Hangman(word)

    assert Status.ON_GOING == hangman.getStatus()
    assert len(word) * "_" == hangman.getMaskedWord()
    assert 9 == hangman.getRemainingGuesses()


def test_hangman_foo_two() -> None:
    word = "foo"
    hangman = Hangman(word)

    assert len(word) * "_" == hangman.getMaskedWord()


def test_hangman_foo_three() -> None:
    word = "foo"
    hangman = Hangman(word)

    for _ in range(9):
        hangman.guess("x")

    assert Status.LOSE == hangman.getStatus()

    with raises(ValueError, match="The game has already ended."):
        hangman.guess("x")


def test_hangman_foobar_one() -> None:
    word = "foobar"
    hangman = Hangman(word)

    hangman.guess("b")

    assert Status.ON_GOING == hangman.getStatus()
    assert 8 == hangman.getRemainingGuesses()
    assert (3 * "_") + "b" + (2 * "_") == hangman.getMaskedWord()

    hangman.guess("o")

    assert Status.ON_GOING == hangman.getStatus()
    assert 7 == hangman.getRemainingGuesses()
    assert (1 * "_") + (2 * "o") + "b" + (2 * "_") == hangman.getMaskedWord()


def test_hangman_foobar_two() -> None:
    word = "foobar"
    hangman = Hangman(word)

    hangman.guess("b")

    assert Status.ON_GOING == hangman.getStatus()
    assert 8 == hangman.getRemainingGuesses()
    assert (3 * "_") + "b" + (2 * "_") == hangman.getMaskedWord()

    hangman.guess("b")

    assert Status.ON_GOING == hangman.getStatus()
    assert 8 == hangman.getRemainingGuesses()
    assert (3 * "_") + "b" + (2 * "_") == hangman.getMaskedWord()


def test_hangman_hello() -> None:
    word = "hello"
    hangman = Hangman(word)

    hangman.guess("b")

    assert Status.ON_GOING == hangman.getStatus()
    assert 8 == hangman.getRemainingGuesses()
    assert len(word) * "_" == hangman.getMaskedWord()

    hangman.guess("e")

    assert Status.ON_GOING == hangman.getStatus()
    assert 7 == hangman.getRemainingGuesses()
    assert (1 * "_") + "e" + (3 * "_") == hangman.getMaskedWord()

    hangman.guess("l")

    assert Status.ON_GOING == hangman.getStatus()
    assert 6 == hangman.getRemainingGuesses()
    assert (1 * "_") + "e" + (2 * "l") + (1 * "_") == hangman.getMaskedWord()

    hangman.guess("o")

    assert Status.ON_GOING == hangman.getStatus()
    assert 5 == hangman.getRemainingGuesses()
    assert (1 * "_") + "e" + (2 * "l") + (1 * "o") == hangman.getMaskedWord()

    hangman.guess("h")

    assert Status.WIN == hangman.getStatus()
    assert 4 == hangman.getRemainingGuesses()
    assert word == hangman.getMaskedWord()

    with raises(ValueError, match="The game has already ended."):
        hangman.guess("x")


def test_hangman_aaa() -> None:
    word = "aaa"
    hangman = Hangman(word)

    for character in "bcdefghi":
        hangman.guess(character)

    hangman.guess("a")

    assert Status.WIN == hangman.getStatus()
    assert 0 == hangman.getRemainingGuesses()
    assert word == hangman.getMaskedWord()
